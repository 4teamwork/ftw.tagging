from ftw.tagging import utils
from ftw.tagging.interfaces.tagging import ITaggable, ITagRoot
from ftw.testing import MockTestCase


class TestUtils(MockTestCase):

    def setUp(self):
        portal_url = self.stub()
        self.mock_tool(portal_url, 'portal_url')
        self.portal = self.stub()
        self.expect(portal_url.getPortalObject()).result(self.portal)

    def test_getInterfaceRoot(self):
        root = self.providing_stub([ITagRoot])

        obj = self.set_parent(
            self.stub(),
            self.set_parent(
                self.stub(),
                self.set_parent(
                    root,
                    self.portal)))

        self.replay()

        self.assertEqual(utils.getInterfaceRoot(obj, ITagRoot), root)

    def test_getInterfaceRoot_when_root_reached(self):
        obj = self.set_parent(
            self.stub(),
            self.portal)

        self.replay()

        self.assertEqual(utils.getInterfaceRoot(obj, ITagRoot), self.portal)


    def test_getTagRootTags(self):
        brain1 = self.stub()
        self.expect(brain1.tags).result(('foo', 'bar', u'\xe4', '\xc3\xa4'))
        brain2 = self.stub()
        self.expect(brain2.tags).result(('bar', u'baz'))
        brain3 = self.stub()
        self.expect(brain3.tags).result(None)

        root = self.providing_stub([ITagRoot])
        obj = self.set_parent(self.stub(), root)
        self.expect(root.getPhysicalPath()).result(['', 'path', 'to', 'root'])

        catalog = self.stub()
        self.mock_tool(catalog, 'portal_catalog')
        query = {'path': '/path/to/root',
                 'object_provides': ITaggable.__identifier__}
        self.expect(catalog(query)).result([brain1, brain2])

        self.replay()

        self.assertEqual(set(utils.getTagRootTags(obj)),
                         set(['foo', 'bar', 'baz', '\xc3\xa4']))
