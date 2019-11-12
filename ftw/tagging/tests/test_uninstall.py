from ftw.testing import IS_PLONE_5
from ftw.testing.genericsetup import GenericSetupUninstallMixin
from ftw.testing.genericsetup import apply_generic_setup_layer
from unittest import TestCase
from unittest import skipUnless


@apply_generic_setup_layer
@skipUnless(IS_PLONE_5, 'Test the uninstall profile for Plone 5')
class TestGenericSetupUninstall(TestCase, GenericSetupUninstallMixin):
    package = 'ftw.tagging'
    skip_files = ('viewlets.xml',)
