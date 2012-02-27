Overview
========

Tagging Add-on for Plone.


Install
======

- Add ``ftw.tagging`` to yout buidlout configuration

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
- Continuous integration: https://jenkins.4teamwork.ch/job/ftw.tagging/

Maintainer
==========

This package is produced and maintained by `4teamwork GmbH <http://www.4teamwork.ch/>`_.
