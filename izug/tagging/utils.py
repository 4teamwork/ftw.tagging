from Acquisition import aq_base

from Products.CMFCore.utils import getToolByName
from Products.CMFPlone import utils

from izug.tagging.interfaces.tagging import ITaggable, ITagRoot


def getInterfaceRoot(context, interface):
    """Climb up the folder hierarchy and find an object that implements ISearchRoot
    """
    
    portal_url = getToolByName(context, 'portal_url')
    
    portal = portal_url.getPortalObject()
    object = context
    
    while not interface.providedBy(object) and aq_base(object) is not aq_base(portal):
        object = utils.parent(object)
    if interface.providedBy(object) and aq_base(object) is not aq_base(portal):
        return object
    else:
        return aq_base(portal)

def getTagRootTags(context):
    """Get all tags used in the current branch of the tag root
    """
       
    items = []
    catalog_tool = getToolByName(context, "portal_catalog")
    tag_root = getInterfaceRoot(context, ITagRoot)
    root_path ='/'.join(tag_root.getPhysicalPath())
    
    brains_below_tag_root = catalog_tool({'path' : root_path,
                                          'object_provides' : ITaggable.__identifier__})
    for brain in brains_below_tag_root:
        for raw_tag in brain.tags:
            tag = raw_tag.encode('utf-8')
            if tag not in items:
                items.append(tag)
    
    return items

def getBrainsByTag(context, tag):
    """Get catalog brains for objects in the current branch of the tag root by tag
    """
       
    catalog_tool = getToolByName(context, "portal_catalog")
    tag_root = getInterfaceRoot(context, ITagRoot)
    root_path ='/'.join(tag_root.getPhysicalPath())
    
    brains = catalog_tool({'path' : root_path,
                            'object_provides' : ITaggable.__identifier__,
                            'tags' : tag.decode('utf-8')})
    
    return brains
