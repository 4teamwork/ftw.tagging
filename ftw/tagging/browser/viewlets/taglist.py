from Acquisition import aq_inner

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase

from ftw.tagging.interfaces.tagging import ITagRoot
from ftw.tagging.utils import getInterfaceRoot


class TagListViewlet(ViewletBase):
    index = ViewPageTemplateFile('taglist.pt')

    def update(self):
        context = aq_inner(self.context).aq_explicit
        self.tags = getattr(context, 'tags', [])
        self.tag_root_url = getInterfaceRoot(context, ITagRoot).absolute_url()
