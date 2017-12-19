from ftw.builder import Builder
from ftw.builder import create
from ftw.builder.content import register_dx_content_builders
from ftw.tagging.tests import FunctionalTestCase
from ftw.tagging.tests import utils
from ftw.tagging.utils import getTagRootTags
from ftw.testbrowser import browsing
from plone import api
from plone.app.testing import applyProfile


class TestTagsDexterity(FunctionalTestCase):

    def setUp(self):
        super(TestTagsDexterity, self).setUp()
        self.grant('Manager')
        applyProfile(self.portal, 'plone.app.contenttypes:default')
        register_dx_content_builders(force=True)

    def test_tags_indexer(self):
        utils.add_behaviors('Document', 'ftw.tagging.behavior.ITagging')

        document = create(Builder('document')
                          .titled(u'My Document')
                          .having(tags=['Foo', u'B\xe4\xe4']))

        catalog = api.portal.get_tool('portal_catalog')
        rid = catalog.getrid('/'.join(document.getPhysicalPath()))
        index_data = catalog.getIndexDataForRID(rid)
        self.assertEqual(
            {'Foo', u'B\xe4\xe4'},
            set(index_data['tags'])
        )

        self.assertEqual(
            {'Foo', 'B\xc3\xa4\xc3\xa4'},
            set(getTagRootTags(document))
        )

    @browsing
    def test_tags_widget(self, browser):
        utils.add_behaviors('Document', 'ftw.tagging.behavior.ITagging')

        document = create(Builder('document')
                          .titled(u'My Document'))

        browser.login().visit(document, view='edit')

        browser.fill({'form.widgets.ITagging.tags_new': u'Foo\nB\xe4\xe4'}).save()

        catalog = api.portal.get_tool('portal_catalog')
        rid = catalog.getrid('/'.join(document.getPhysicalPath()))
        index_data = catalog.getIndexDataForRID(rid)

        self.assertEqual(
            {'B\xc3\xa4\xc3\xa4', 'Foo'},
            set(index_data['tags'])
        )
        self.assertEqual(
            {'B\xc3\xa4\xc3\xa4', 'Foo'},
            set(getTagRootTags(document))
        )

    def test_plone_is_tag_root(self):
        utils.add_behaviors('Document', 'ftw.tagging.behavior.ITagging')

        root1 = create(Builder('folder').titled(u'Tag Root 1'))
        document1 = create(Builder('document')
                           .titled(u'Document in Tag Root 1')
                           .within(root1)
                           .having(tags=['Foo']))

        root2 = create(Builder('folder').titled(u'Tag Root 2'))
        document2 = create(Builder('document')
                           .titled(u'Document in Tag Root 2')
                           .within(root2)
                           .having(tags=['Bar']))

        self.assertEqual(
            {'Foo', 'Bar'},
            set(getTagRootTags(document1))
        )
        self.assertEqual(
            {'Foo', 'Bar'},
            set(getTagRootTags(document2))
        )

    def test_folders_are_tag_roots(self):
        utils.add_behaviors('Folder', 'ftw.tagging.interfaces.tagging.ITagRoot')
        utils.add_behaviors('Document', 'ftw.tagging.behavior.ITagging')

        root1 = create(Builder('folder').titled(u'Tag Root 1'))
        document1 = create(Builder('document')
                           .titled(u'Document in Tag Root 1')
                           .within(root1)
                           .having(tags=['Foo']))

        root2 = create(Builder('folder').titled(u'Tag Root 2'))
        document2 = create(Builder('document')
                           .titled(u'Document in Tag Root 2')
                           .within(root2)
                           .having(tags=['Bar']))

        self.assertEqual(
            ['Foo'],
            getTagRootTags(document1)
        )
        self.assertEqual(
            ['Bar'],
            getTagRootTags(document2)
        )
