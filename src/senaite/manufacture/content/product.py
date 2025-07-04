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
from senaite.manufacture.content.fields import ExtUIDReferenceField
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
    
    directives.mode(title='add')
    description = schema.Text(
        title=_(
            "title_product_description",
            default="Description"
        ),
        required=True,
    )


@implementer(IProductSchema, IProduct, IDeactivable)
class Product(Item):
    # Catalogs where this type will be catalogued
    _catalogs = [SETUP_CATALOG]