from zope.component import adapts
from zope.interface import implements

from Products.Archetypes import atapi

from archetypes.schemaextender.field import ExtensionField
from archetypes.schemaextender.interfaces import ISchemaExtender, IBrowserLayerAwareExtender

from Products.AddRemoveWidget import AddRemoveWidget

from izug.tagging.interfaces.tagging import ITaggable
from izug.tagging.browser.interfaces import IIzugTaggingLayer
from izug.tagging import taggingMessageFactory as _


class LinesExtensionField(ExtensionField, atapi.LinesField):
    """LinesField for use with archetypes.schemaextender
    """
    
class TaggableExtender(object):
    adapts(ITaggable)
    implements(ISchemaExtender, IBrowserLayerAwareExtender)
    
    fields = []
    layer = IIzugTaggingLayer

    fields.append(LinesExtensionField('tags',
                                      multiValued=True,
                                      languageIndependent=False,
                                      storage=atapi.AttributeStorage(), # This is necessary to make the field indexable
                                      vocabulary='getAllTags',
                                      widget=AddRemoveWidget(label=_(u"label_taggable_extender_tags", default=u"Tags"),
                                                               description=_(u"help_taggable_extender_tags", default=u""),
                                                               ),
                                      ),
    )
    
    def __init__(self, context):
        self.context = context
        
    def getFields(self):
        return self.fields
