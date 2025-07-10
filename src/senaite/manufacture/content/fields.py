from archetypes.schemaextender.field import ExtensionField
from bika.lims.browser.fields import UIDReferenceField as UIDATReferenceField
from senaite.core.browser.fields.datetime import DateTimeField
from senaite.core.schema import UIDReferenceField as UIDDXReferenceField
#from senaite.core.schema.fields import IntField
from Products.Archetypes.Field import IntegerField

class ExtATUIDReferenceField(ExtensionField, UIDATReferenceField):
    """Field Extender of core's UIDReferenceField for AT types
    """
class ExtUIDReferenceField(ExtensionField, UIDDXReferenceField):
    """Field Extender of core's UIDReferenceField for DX types
    """
class ExtDateTimeField(ExtensionField, DateTimeField):
    """Field extender of core's DateTimeField
    """
class ExtIntegerField(ExtensionField, IntegerField):
    """Field extender of core's IntegerField
    """
