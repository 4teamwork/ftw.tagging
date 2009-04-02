from zope.component import getUtility
from zope.component import getMultiAdapter

from Products.CMFCore.utils import getToolByName
from Products.CMFEditions.setuphandlers import DEFAULT_POLICIES

from izug.tagging.config import PRODUCT_DEPENDENCIES

from plone.portlets.interfaces import IPortletAssignmentMapping
from plone.portlets.interfaces import IPortletManager
from plone.portlets.interfaces import ILocalPortletAssignmentManager
from plone.app.portlets import portlets


from izug.tagging.config import INDEXES, METADATA
from Products.ZCatalog.Catalog import CatalogError


class TaggingGenerator:
    def installProducts(self, portal):
        """QuickInstaller install of required Products"""
        quickinstaller_tool = getToolByName(portal, 'portal_quickinstaller')
        for dependency in PRODUCT_DEPENDENCIES:
            quickinstaller_tool.installProduct(dependency)


def setupVarious(context):
    """
    Setup various settings.
    """
    if context.readDataFile('izug.tagging_various.txt') is None:
        return
    site = context.getSite()
    gen = TaggingGenerator()
    gen.installProducts(site)
    

def setupFinal(context):
    """
    Final setup steps.
    """
    if context.readDataFile('izug.tagging_final.txt') is None:
        return
    out = []
    site = context.getSite()
    
    gen = TaggingGenerator()



def add_indexes(site):
    """Add our indexes to the catalog.

    Doing it here instead of in profiles/default/catalog.xml means we
    do not need to reindex those indexes after every reinstall.
    """

    context = site.getSite()
    catalog = getToolByName(context, 'portal_catalog')
    indexes = catalog.indexes()
    
    
    for name, meta_type in INDEXES:
        if name not in indexes:
            catalog.addIndex(name, meta_type)
        if name in METADATA:
            try:
                catalog.manage_addColumn(name)
            except CatalogError:
                pass
