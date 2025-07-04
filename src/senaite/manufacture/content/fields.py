from archetypes.schemaextender.field import ExtensionField
from bika.lims.browser.fields import UIDReferenceField
from senaite.core.browser.fields.datetime import DateTimeField


class ExtUIDReferenceField(ExtensionField, UIDReferenceField):
    """Field Extender of core's UIDReferenceField for AT types
    """


class ExtDateTimeField(ExtensionField, DateTimeField):
    """Field extender of core's DateTimeField
    """