from zope.interface import implements
from Acquisition import aq_inner
from plone.portlets.interfaces import IPortletDataProvider
from plone.app.portlets.portlets import base
from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName

from zope import schema
from zope.formlib import form
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFPlone import PloneMessageFactory as _
from zope.component import getMultiAdapter, queryMultiAdapter, getUtility
from Products.CMFPlone.browser.interfaces import ISitemapView

from izug.tagging.utils import getInterfaceRoot, getTagRootTags
from izug.tagging.interfaces.tagging import ITaggable, ITagRoot

from izug.tagging import taggingMessageFactory as _


class ITagsPortlet(IPortletDataProvider):

    maxsize = schema.ASCIILine(title=_(u'Max. Fontsize'),
                       description=_(u'Size in em'),
                       required=True,
                       default='2')

    minsize = schema.ASCIILine(title=_(u'Min. Fontsize'),
                       description=_(u'Size in em'),
                       required=True,
                       default='0.7')

class Assignment(base.Assignment):
    implements(ITagsPortlet)
    
    def __init__(self, maxsize='2',minsize='0.7'):
        self.maxsize = maxsize
        self.minsize = minsize

    @property
    def title(self):
        return "Tag Cloud Portlet"

class Renderer(base.Renderer):
    def __init__(self, context, request, view, manager, data):
        self.context = context
        self.data = data

        tags = getTagRootTags(context)
        tag_root = getInterfaceRoot(context, ITagRoot)
        root_path ='/'.join(tag_root.getPhysicalPath())
        
        catalog_tool = getToolByName(context, "portal_catalog")
        query = {}
        query['object_provides'] = ITaggable.__identifier__
        query['path'] = root_path
        
        tag_occurrence = {}
        for tag in tags:
            query['tags'] = tag.decode('utf-8')
            tag_occurrence[tag] = len(catalog_tool(query))
        
        weight_list = tag_occurrence.values()
        weight_list.sort()
        
        if weight_list:
            minimal = weight_list[:1][0]
            maximal = weight_list[-1:][0]
            
            maxsize = float(self.data.maxsize)
            minsize = float(self.data.minsize)
           
            tag_cloud = []
            
            for tag in tags:
                try:
                    size = float((maxsize * (tag_occurrence[tag] - minimal))) / float((maximal - minimal))
                except ZeroDivisionError:
                    size = 1
                if tag_occurrence[tag] <= minimal or size < minsize:
                    size = float(self.data.minsize)
                
                info = dict(title=tag,
                            font_size=round(size, 1))
                tag_cloud.append(info)
            
            tag_cloud.sort(lambda x, y: cmp(x['title'], y['title']))
            self.tag_cloud = tag_cloud
        else:
            self.tag_cloud = []
       
        self.tag_root = tag_root.absolute_url()
        
    render = ViewPageTemplateFile('tags.pt')

class AddForm(base.AddForm):
    form_fields = form.Fields(ITagsPortlet)
    label = _(u"Add Tag Cloud Portlet")
    description = _(u"This portlet displays a Tag Cloud for Tags within the current Tag Root.")

    def create(self, data):
        return Assignment(maxsize=data.get('maxsize', '2'),
                          minsize=data.get('minsize', '0.7'))

class EditForm(base.EditForm):
    form_fields = form.Fields(ITagsPortlet)
    label = _(u"Edit Tag Cloud Portlet")
    description = _(u"This portlet displays a Tag Cloud for Tags within the current Tag Root.")
