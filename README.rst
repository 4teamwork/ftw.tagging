Overview
========

``ftw.tagging`` extends Plone content types with a tags field using
schemaextender. Further it's possible to define tag roots to restrict
tags to a part of the site.

A tag cloud portlet is provided that shows a tag cloud for the current
tag root.

As an example, ``ftw.tagging`` is used by ``ftw.blog`` for tagging blog entries.


Install
=======

- Add ``ftw.tagging`` to your buildout configuration:

::

  [instance]
  eggs =
    ftw.tagging

- Run buildout

- Install ``ftw.tagging`` in portal_setup


Usage
=====

Implement tagging interfaces for your content types.
If no tag root is set, Plone-root will also be your tag-root.

::

  <class class="path.to.my.class">
      <implements interface="ftw.tagging.interfaces.tagging.ITaggable" />
  </class>
  <class class=".blog.Blog">
      <implements interface="ftw.tagging.interfaces.tagging.ITagRoot" />
  </class>


You can show the tag-cloud by adding the tag-cloud portlet provided by this
package.


Links
=====

- Package repository: https://github.com/4teamwork/ftw.tagging
- Issue tracker: https://github.com/4teamwork/ftw.tagging/issues
- Package on pypi: http://pypi.python.org/pypi/ftw.tagging
- Continuous integration: https://jenkins.4teamwork.ch/search?q=ftw.tagging


Copyright
=========

This package is copyright by `4teamwork <http://www.4teamwork.ch/>`_.

``ftw.tagging`` is licensed under GNU General Public License, version 2.
