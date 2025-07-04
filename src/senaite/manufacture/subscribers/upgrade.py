
from bika.lims.api import get_portal
from senaite.manufacture import is_installed
from senaite.manufacture import logger
from senaite.manufacture.setuphandlers import add_setup_folders
from senaite.manufacture.setuphandlers import setup_navigation_types
from senaite.manufacture.setuphandlers import setup_workflows


def afterUpgradeStepHandler(event):
    """Event handler that is executed after running an upgrade step of senaite.core
    """
    if not is_installed():
        return

    logger.info("Run senaite.manufacture.afterUpgradeStepHandler ...")

    portal = get_portal()
    add_setup_folders(portal)
    setup_navigation_types(portal)
    setup_workflows(portal)

    logger.info("Run senaite.manufacture.afterUpgradeStepHandler [DONE]")