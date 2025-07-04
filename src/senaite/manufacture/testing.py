# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import senaite.manufacture


class SenaiteManufactureLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=senaite.manufacture)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'senaite.manufacture:default')


SENAITE_MANUFACTURE_FIXTURE = SenaiteManufactureLayer()


SENAITE_MANUFACTURE_INTEGRATION_TESTING = IntegrationTesting(
    bases=(SENAITE_MANUFACTURE_FIXTURE,),
    name='SenaiteManufactureLayer:IntegrationTesting',
)


SENAITE_MANUFACTURE_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(SENAITE_MANUFACTURE_FIXTURE,),
    name='SenaiteManufactureLayer:FunctionalTesting',
)


SENAITE_MANUFACTURE_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        SENAITE_MANUFACTURE_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='SenaiteManufactureLayer:AcceptanceTesting',
)
