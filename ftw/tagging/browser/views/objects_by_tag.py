from Acquisition import aq_inner
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from ftw.tagging.utils import getBrainsByTag


class ObjectsByTagView(BrowserView):
    template = ViewPageTemplateFile('objects_by_tag.pt')

    def __call__(self):
        context = aq_inner(self.context).aq_explicit
        request = self.request

        self.brains = []
        tag = getattr(request, 'tag', None)
        if tag is not None:
            self.brains = getBrainsByTag(context, tag)

        return self.template()
