from zope.interface import implements, implementer
from zope.component import adapts
from archetypes.schemaextender.interfaces import IBrowserLayerAwareExtender, IOrderableSchemaExtender
from archetypes.schemaextender.field import ExtensionField
from plone.autoform import directives
from senaite.core.catalog import SETUP_CATALOG
from senaite.core.schema import UIDReferenceField
from senaite.manufacture import messageFactory as _
from senaite.core.z3cform.widgets.uidreference import UIDReferenceWidgetFactory
from Products.Archetypes.Field import StringField, IntegerField, ReferenceField
from Products.Archetypes.Widget import IntegerWidget, ReferenceWidget
from bika.lims.interfaces import IBatch
from senaite.manufacture.interfaces import ISenaiteManufactureLayer

class StringExtensionField(ExtensionField, StringField):
    pass

class IntegerExtensionField(ExtensionField, IntegerField):
    pass

class ReferenceExtensionField(ExtensionField, ReferenceField):
    pass

BatchSize = IntegerExtensionField(
                name="batchSize",
                widget=IntegerWidget(
                    label=u"Batch Size",
                    description=u"Total quantity produced for this batch"
                ),
                required=True,
            )

ReleasedQuantity = IntegerExtensionField(
                name="releasedQuantity",
                widget=IntegerWidget(
                    label=u"Released Quantity",
                    description=u"Quantity released for distribution"
                ),
                required=False,
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
            u"label_batch_product",
            default=u"Product"
        ),
        allowed_types=("Product", ),
        multi_valued=False,
        required=True,
    )

@implementer(IOrderableSchemaExtender, IBrowserLayerAwareExtender)
class BatchSchemaExtender(object):
    """Schema extender for the Batch content type."""
    adapts(IBatch)
    layer = ISenaiteManufactureLayer

    def __init__(self, context):
        self.context = context

    def getOrder(self, schematas):
        return schematas
    
    def getFields(self):
        return [
            BatchSize,
            ReleasedQuantity,
        ]
