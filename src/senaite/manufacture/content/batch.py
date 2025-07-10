from zope.interface import implements
from zope.component import adapts
from archetypes.schemaextender.interfaces import ISchemaExtender
from bika.lims.interfaces import IBatch
from fields import ExtIntegerField
from senaite.manufacture import messageFactory as _

class BatchSchemaExtender(object):
    implements(ISchemaExtender)
    adapts(IBatch)

    def __init__(self, context):
        self.context = context

    def getFields(self):
        return [
            ExtIntegerField(
                title=_(
                    u"title_batch_size",
                    default=u"Batch Size",
                ),
                description=_(
                    u"description_batch_size",
                    default=u"Batch size in units",
                ),
                required=True,
            ),
        ]
