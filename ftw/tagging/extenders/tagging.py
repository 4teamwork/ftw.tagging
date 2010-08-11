from zope.component import adapts
from zope.interface import implements

from Products.Archetypes import atapi

from archetypes.schemaextender.field import ExtensionField
from archetypes.schemaextender.interfaces import ISchemaExtender, \
        IBrowserLayerAwareExtender

from ftw.tagging.interfaces.tagging import ITaggable
from ftw.tagging.browser.interfaces import IFtwTaggingLayer
from ftw.tagging import taggingMessageFactory as _


class LinesExtensionField(ExtensionField, atapi.LinesField):
    """LinesField for use with archetypes.schemaextender
    """


class TaggableExtender(object):
    adapts(ITaggable)
    implements(ISchemaExtender, IBrowserLayerAwareExtender)

    fields = []
    layer = IFtwTaggingLayer

    fields.append(LinesExtensionField('tags',
          multiValued=True,
          languageIndependent=False,
          # This is necessary to make the field indexable
          storage=atapi.AttributeStorage(),
          vocabulary_factory=u"Tag Vocabulary",
          widget=atapi.LinesWidget(label=_(u"label_taggable_extender_tags",
                                         default=u"Tags"),
                                 description=_(u"help_taggable_extender_tags",
                                               default=u""),
                                   ),
          ),
    )

    def __init__(self, context):
        self.context = context

    def getFields(self):
        return self.fields
