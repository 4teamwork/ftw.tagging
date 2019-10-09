from ftw.tagging.behavior import ITagging
from ftw.tagging.interfaces.tagging import ITaggable
from plone.dexterity.utils import safe_utf8
from plone.indexer import indexer
from zope.interface import Interface


@indexer(Interface)
def tags(obj):
    if not ITaggable(obj, None):
        return None

    behavior = ITagging(obj, None)
    if behavior:
        return map(safe_utf8, behavior.tags)

    return None
