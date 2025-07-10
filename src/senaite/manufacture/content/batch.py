from zope.interface import implements
from zope.component import adapts
from archetypes.schemaextender.interfaces import ISchemaExtender
from archetypes.schemaextender.field import ExtensionField
from Products.Archetypes.Field import StringField, IntegerField, ReferenceField
from Products.Archetypes.Widget import StringWidget, IntegerWidget, ReferenceWidget
from bika.lims.interfaces import IBatch

class StringExtensionField(ExtensionField, StringField):
    pass

class IntegerExtensionField(ExtensionField, IntegerField):
    pass

class ReferenceExtensionField(ExtensionField, ReferenceField):
    pass

class BatchSchemaExtender(object):
    implements(ISchemaExtender)
    adapts(IBatch)

    def __init__(self, context):
        self.context = context

    def getFields(self):
        return [
            IntegerExtensionField(
                name="batchSize",
                widget=IntegerWidget(
                    label=u"Batch Size",
                    description=u"Total quantity produced for this batch"
                ),
                required=False,
            ),
            IntegerExtensionField(
                name="releasedQuantity",
                widget=IntegerWidget(
                    label=u"Released Quantity",
                    description=u"Quantity released for distribution"
                ),
                required=False,
            ),
        ]
