from Products.CMFCore.utils import getToolByName

from ftw.tagging.config import INDEXES, METADATA
from Products.ZCatalog.Catalog import CatalogError


def setupVarious(context):
    """
    Setup various settings.
    """
    if context.readDataFile('ftw.tagging_various.txt') is None:
        return
    site = context.getSite()


def setupFinal(context):
    """
    Final setup steps.
    """
    if context.readDataFile('ftw.tagging_final.txt') is None:
        return
    out = []
    site = context.getSite()


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
