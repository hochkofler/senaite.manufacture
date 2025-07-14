from zope.interface import implements, implementer
from zope.component import adapts
from archetypes.schemaextender.interfaces import ISchemaExtender, IBrowserLayerAwareExtender, IOrderableSchemaExtender
from archetypes.schemaextender.field import ExtensionField
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
                required=False,
            )

ReleasedQuantity = IntegerExtensionField(
                name="releasedQuantity",
                widget=IntegerWidget(
                    label=u"Released Quantity",
                    description=u"Quantity released for distribution"
                ),
                required=False,
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
