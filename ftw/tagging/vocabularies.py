from binascii import b2a_qp
from ftw.tagging.utils import getTagRootTags
from Products.CMFPlone.utils import safe_unicode
from zope.interface import alsoProvides
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary


def tagVocabulary(context):
    """Vocabulary factory for tags within a given section of the site,
    delimited by an ITagRoot interface

    Inspired by "plone.app.vocabularies.catalog.KeywordsVocabulary" for the
    encoding stuff.
    """

    root_tags = getTagRootTags(context)

    def safe_encode(term):
        if isinstance(term, unicode):
            # no need to use portal encoding for transitional encoding from
            # unicode to ascii. utf-8 should be fine.
            term = term.encode('utf-8')
        return term

    # Vocabulary term tokens *must* be 7 bit values, term titles *must* be unicode.
    items = [
        SimpleTerm(tag, b2a_qp(safe_encode(tag)), safe_unicode(tag))
        for tag in root_tags
    ]
    return SimpleVocabulary(items)


alsoProvides(tagVocabulary, IVocabularyFactory)
