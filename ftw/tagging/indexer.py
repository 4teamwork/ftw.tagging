from ftw.tagging.behavior import ITagging
from ftw.tagging.interfaces.tagging import ITaggable
from plone.dexterity.interfaces import IDexterityContent
from plone.indexer import indexer
from zope.interface import Interface


@indexer(Interface)
def tags(obj):
    if not ITaggable(obj, None):
        return None

    if IDexterityContent.providedBy(obj):
        behavior = ITagging(obj, None)
        if behavior:
            return tuple(behavior.tags)
    elif 'tags' in obj.Schema().keys():
        return obj.Schema()['tags'].get(obj)

    return None
