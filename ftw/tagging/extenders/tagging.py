from Products.Archetypes import atapi
from archetypes.schemaextender.field import ExtensionField
from archetypes.schemaextender.interfaces import IBrowserLayerAwareExtender
from archetypes.schemaextender.interfaces import ISchemaExtender
from ftw.tagging import taggingMessageFactory as _
from ftw.tagging.browser.interfaces import IFtwTaggingLayer
from ftw.tagging.interfaces.tagging import ITaggable
from zope.component import adapts
from zope.interface import implements


class LinesExtensionField(ExtensionField, atapi.LinesField):
    """LinesField for use with archetypes.schemaextender
    """


class TaggableExtender(object):
    adapts(ITaggable)
    implements(ISchemaExtender, IBrowserLayerAwareExtender)

    fields = []
    layer = IFtwTaggingLayer

    fields.append(
        LinesExtensionField(
            'tags',
            multiValued=True,
            languageIndependent=False,
            vocabulary_factory="tags",
            accessor='tags',
            vocab_source='special_tag_source',

            # This is necessary to make the field indexable
            storage=atapi.AttributeStorage(),

            widget=atapi.KeywordWidget(
                label=_(u"label_taggable_extender_tags",
                        default=u"Tags"),
                description=_(u"help_taggable_extender_tags",
                              default=u""),
                vocab_source='special_tag_source',
                roleBasedAdd=False,
                ),
            ),
        )

    def __init__(self, context):
        self.context = context

    def getFields(self):
        return self.fields
