from ftw.builder import builder_registry
from ftw.builder.portlets import PlonePortletBuilder
from ftw.tagging.portlets import tags


class TagCloudPortletBuilder(PlonePortletBuilder):
    assignment_class = tags.Assignment

builder_registry.register('tag cloud portlet', TagCloudPortletBuilder)
