from setuptools import setup, find_packages
import os

version = '2.0.0'
maintainer = 'Mathias Leimgruber'

tests_require = [
    'collective.testcaselayer',
    'ftw.builder',
    'ftw.testbrowser',
    'ftw.testing',
    'plone.app.contenttypes',
    ]


setup(name='ftw.tagging',
      version=version,
      description="Tagging add-on for Plone",
      long_description=open("README.rst").read() + "\n" + \
          open(os.path.join("docs", "HISTORY.txt")).read(),

      # Get more strings from
      # http://www.python.org/pypi?%3Aaction=list_classifiers

      classifiers=[
        'Framework :: Plone',
        'Framework :: Plone :: 4.3',
        'Framework :: Plone :: 5.1',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],

      keywords='ftw tagging plone',
      author='4teamwork AG',
      author_email='mailto:info@4teamwork.ch',
      maintainer=maintainer,
      url='https://github.com/4teamwork/ftw.tagging',
      license='GPL2',

      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['ftw'],
      include_package_data=True,
      zip_safe=False,

      install_requires=[
        'setuptools',

        # Zope
        'Acquisition',
        'Zope2',
        'zope.component',
        'zope.formlib',
        'zope.i18nmessageid',
        'zope.interface',
        'zope.schema',

        # Plone
        'Plone',
        'Products.CMFCore',
        'Products.CMFPlone',
        'ftw.keywordwidget',
        'ftw.profilehook',
        'ftw.upgrade',
        'plone.api',
        'plone.app.layout',
        'plone.app.portlets',
        'plone.portlets',
        'plone.theme',

        ],
      tests_require=tests_require,
      extras_require=dict(tests=tests_require),

      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
