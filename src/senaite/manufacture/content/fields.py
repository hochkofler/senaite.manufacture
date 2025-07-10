from archetypes.schemaextender.field import ExtensionField
from bika.lims.browser.fields import UIDReferenceField as UIDATReferenceField
from senaite.core.schema.uidreferencefield import UIDReferenceField as UIDDXReferenceField
from senaite.core.schema.datetimefield import DatetimeField
from senaite.core.schema.fields import IntField

class ExtATUIDReferenceField(ExtensionField, UIDATReferenceField):
    """Field Extender of core's UIDReferenceField for AT types
    """
class ExtUIDReferenceField(ExtensionField, UIDDXReferenceField):
    """Field Extender of core's UIDReferenceField for DX types
    """
class ExtDateTimeField(ExtensionField, DatetimeField):
    """Field extender of core's DateTimeField
    """
class ExtIntegerField(ExtensionField, IntField):
    """Field extender of core's IntegerField
    """
