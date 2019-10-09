Overview
========

``ftw.tagging`` extends Plone content types with a tags field using
schemaextender for Archetype or a behavior for Dexterity.

It's possible to define tag roots to restrict tags to a part of the
site. If no tag root is set, the Plone-root will also be your tag-root.

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

Enable tagging on your DX types with a behavior:

::

  <property name="behaviors" purge="False">
    <element value="ftw.tagging.behavior.ITagging" />
  </property>


Optionally use a behavior to define tag roots:

::

  <property name="behaviors" purge="False">
    <element value="ftw.tagging.interfaces.tagging.ITagRoot" />
  </property>


Tag Cloud
---------

You can show the tag-cloud by adding the tag-cloud portlet provided by this
package.


Compatibility
=============

Runs with `Plone <http://www.plone.org/>`_ `4.3` and `5.1`.


Links
=====

- Github: https://github.com/4teamwork/ftw.tagging
- Issues: https://github.com/4teamwork/ftw.tagging/issues
- Pypi: http://pypi.python.org/pypi/ftw.tagging
- Continuous integration: https://jenkins.4teamwork.ch/search?q=ftw.tagging


Copyright
=========

This package is copyright by `4teamwork <http://www.4teamwork.ch/>`_.

``ftw.tagging`` is licensed under GNU General Public License, version 2.
