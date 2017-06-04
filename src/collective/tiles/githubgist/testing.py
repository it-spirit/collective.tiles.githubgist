# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import collective.tiles.githubgist


class CollectiveTilesGithubgistLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.app.mosaic
        self.loadZCML(package=plone.app.mosaic)
        self.loadZCML(package=collective.tiles.githubgist)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'plone.app.mosaic:default')
        applyProfile(portal, 'collective.tiles.githubgist:default')


COLLECTIVE_TILES_GITHUBGIST_FIXTURE = CollectiveTilesGithubgistLayer()


COLLECTIVE_TILES_GITHUBGIST_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_TILES_GITHUBGIST_FIXTURE,),
    name='CollectiveTilesGithubgistLayer:IntegrationTesting'
)


COLLECTIVE_TILES_GITHUBGIST_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_TILES_GITHUBGIST_FIXTURE,),
    name='CollectiveTilesGithubgistLayer:FunctionalTesting'
)


COLLECTIVE_TILES_GITHUBGIST_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        COLLECTIVE_TILES_GITHUBGIST_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='CollectiveTilesGithubgistLayer:AcceptanceTesting'
)
