# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import (
    applyProfile,
    FunctionalTesting,
    IntegrationTesting,
    PloneSandboxLayer,
)
from plone.testing import z2

import acentoweb.corpuslse


class AcentowebCorpuslseLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=acentoweb.corpuslse)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'acentoweb.corpuslse:default')


ACENTOWEB_CORPUSLSE_FIXTURE = AcentowebCorpuslseLayer()


ACENTOWEB_CORPUSLSE_INTEGRATION_TESTING = IntegrationTesting(
    bases=(ACENTOWEB_CORPUSLSE_FIXTURE,),
    name='AcentowebCorpuslseLayer:IntegrationTesting',
)


ACENTOWEB_CORPUSLSE_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(ACENTOWEB_CORPUSLSE_FIXTURE,),
    name='AcentowebCorpuslseLayer:FunctionalTesting',
)


ACENTOWEB_CORPUSLSE_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        ACENTOWEB_CORPUSLSE_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='AcentowebCorpuslseLayer:AcceptanceTesting',
)
