from zope.interface import Interface

from ftw.tagging import taggingMessageFactory as _

class ITaggable(Interface):
    """Marker interface for types that can be tagged
    """

class ITagRoot(Interface):
    """Marker interface that delimits ranges where tags are valid
    """
