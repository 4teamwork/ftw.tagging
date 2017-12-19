from plone import api
import transaction
from zope.component import getUtility
from zope.schema.interfaces import IVocabularyFactory


def add_behaviors(type_to_configure, *additional_behaviors):
    fti = api.portal.get().portal_types.get(type_to_configure)
    behaviors = list(fti.behaviors)
    behaviors += list(additional_behaviors)
    fti.behaviors = tuple(set(behaviors))
    transaction.commit()


def terms_for(vocabulary_name, context):
    factory = getUtility(IVocabularyFactory,
                         name=vocabulary_name)
    return dict([(term.value, term.title)
                 for term in factory(context)])
