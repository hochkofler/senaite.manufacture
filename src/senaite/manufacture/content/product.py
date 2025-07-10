# ===========================
# content/product.py
# ===========================
from AccessControl import ClassSecurityInfo
from bika.lims import api
from bika.lims.interfaces import IDeactivable
from senaite.core.content.base import Item
from plone.supermodel import model
from plone.autoform import directives
from senaite.core.catalog import SETUP_CATALOG
from senaite.manufacture.interfaces import IProduct
from zope import schema
from zope.interface import implementer, invariant, Invalid
from senaite.core.z3cform.widgets.uidreference import UIDReferenceWidgetFactory
from senaite.core.schema import UIDReferenceField
from senaite.manufacture.utils import check_title
from senaite.manufacture import messageFactory as _
from Products.CMFCore import permissions
from plone.app.dexterity.behaviors.metadata import IBasic


class IProductSchema(model.Schema):
    """Custom schema for Product content type"""

    title = schema.TextLine(
        title=_(
            u"title_product",
            default=u"Code",
        ),
        required=True,
    )
    
    description = schema.Text(
        title=_(
            "title_product_description",
            default="Description"
        ),
        required=True,
    )

    directives.widget(
        "sample_matrix",
        UIDReferenceWidgetFactory,
        catalog=SETUP_CATALOG,
        query={
            "is_active": True,
            "sort_on": "title",
            "sort_order": "ascending",
        },
    )
    sample_matrix = UIDReferenceField(
        title=_(
            u"label_product_samplematrix",
            default=u"Sample Matrix"
        ),
        description=_(
            u"description_product_samplematrix",
            default=u"Select the sample matrix for this product"
        ),
        allowed_types=("SampleMatrix", ),
        multi_valued=False,
        required=True,
    )

    minimum_unit = schema.TextLine(
        title=_(
            u"title_product_minimum_unit",
            default=u"Minimum Unit",
        ),
        required=True,
    )

    primary_presentation = schema.Int(
        title=_(
            u"title_product_primary_presentation",
            default=u"Primary Presentation",
        ),
        description=_(
            u"description_product_primary_presentation",
            default=u"Primary presentation of the product in minimum unit, e.g. 10 tablets, 1 bottle, etc.",
        ),
        required=True,
    )

    secondary_presentation = schema.Int(
        title=_(
            u"title_product_secondary_presentation",
            default=u"Secondary Presentation",
        ),
        description=_(
            u"description_product_secondary_presentation",
            default=u"Secondary presentation of the product in minimum unit, e.g. 100 tablets, 10 bottles, etc.",
        ),
        required=True,
    )

    @invariant
    def validate_title(data):
        """Checks if the title for this product is unique
        """
        title = data.title.strip()

        # https://community.plone.org/t/dexterity-unique-field-validation
        context = getattr(data, "__context__", None)
        if context is not None:
            if context.title == title:
                # nothing changed
                return
            raise Invalid(_("The product code cannot be changed"))

        check_title(title, context, portal_type="Product")

@implementer(IProductSchema, IProduct, IDeactivable)
class Product(Item):
    # Catalogs where this type will be catalogued
    _catalogs = [SETUP_CATALOG]
    security = ClassSecurityInfo()
    exclude_from_nav = True

    @security.private
    def accessor(self, fieldname):
        """Return the field accessor for the fieldname
        """
        schema = api.get_schema(self)
        if fieldname not in schema:
            return None
        return schema[fieldname].get

    @security.private
    def mutator(self, fieldname):
        """Return the field mutator for the fieldname
        """
        schema = api.get_schema(self)
        if fieldname not in schema:
            return None
        return schema[fieldname].set
    
    @security.protected(permissions.View)
    def getSampleMatrix(self):
        accessor = self.accessor("sample_matrix")
        return accessor(self)