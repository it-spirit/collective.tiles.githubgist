# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from collective.tiles.githubgist.testing import COLLECTIVE_TILES_GITHUBGIST_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that collective.tiles.githubgist is properly installed."""

    layer = COLLECTIVE_TILES_GITHUBGIST_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if collective.tiles.githubgist is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'collective.tiles.githubgist'))

    def test_browserlayer(self):
        """Test that ICollectiveTilesGithubgistLayer is registered."""
        from collective.tiles.githubgist.interfaces import (
            ICollectiveTilesGithubgistLayer)
        from plone.browserlayer import utils
        self.assertIn(ICollectiveTilesGithubgistLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = COLLECTIVE_TILES_GITHUBGIST_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['collective.tiles.githubgist'])

    def test_product_uninstalled(self):
        """Test if collective.tiles.githubgist is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'collective.tiles.githubgist'))

    def test_browserlayer_removed(self):
        """Test that ICollectiveTilesGithubgistLayer is removed."""
        from collective.tiles.githubgist.interfaces import \
            ICollectiveTilesGithubgistLayer
        from plone.browserlayer import utils
        self.assertNotIn(ICollectiveTilesGithubgistLayer, utils.registered_layers())
