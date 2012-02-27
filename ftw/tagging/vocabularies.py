from ftw.tagging.utils import getTagRootTags
from zope.interface import alsoProvides
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary


def tagVocabulary(context):
    """Vocabulary factory for tags within a given section of the site,
    delimited by an ITagRoot interface
    """

    return SimpleVocabulary.fromValues(getTagRootTags(context))

alsoProvides(tagVocabulary, IVocabularyFactory)
