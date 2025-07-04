import re
from bika.lims import api
from bika.lims.utils import t as _t
from bika.lims.utils import to_utf8
from senaite.core.catalog import SETUP_CATALOG
from senaite.manufacture import messageFactory as _
from zope.interface import Invalid


def translate(i18n_message, mapping=None):
    """Translates a message and handles mapping
    """
    return to_utf8(_t(_(i18n_message, mapping=mapping)))


def is_valid_code(value):
    """Return whether the value can be used as code, without special characters
    except '-', '.' and without empties
    """
    if not value:
        return False
    regex = r'^[a-zA-Z0-9.-]*$'
    if re.match(regex, value):
        return True
    return False


def check_title(title, context, portal_type=None, catalog=SETUP_CATALOG):
    """Raises an Invalid exception if the product title passed-in is not valid
    or not unique
    """
    if not is_valid_code(title):
        raise Invalid(_("Code cannot contain special characters or spaces"))

    if not portal_type:
        portal_type = api.get_portal_type(context)

    query = {"portal_type": portal_type}
    for brain in api.search(query, catalog):
        obj = api.get_object(brain)
        if obj.title == title:
            if obj != context:
                raise Invalid(_("Code must be unique"))