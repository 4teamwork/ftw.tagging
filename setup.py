from setuptools import setup, find_packages
import os

version = open('ftw/tagging/version.txt').read().strip()
maintainer = 'Mathias Leimgruber'

tests_require = [
    'collective.testcaselayer',
    ]

setup(name='ftw.tagging',
      version=version,
      description="Tagging add-on for iZug (Maintainer: %s)" % maintainer,
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='ftw tagging plone',
      author='%s, 4teamworkk GmbH' % maintainer,
      author_email='mailto:info@4teamwork.ch',
      maintainer=maintainer,
      url='http://psc.4teamwork.ch/4teamwork/kunden/ftw/ftw.tagging/',
      license='GPL2',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['ftw'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'archetypes.schemaextender',
          'Products.AddRemoveWidget',
      ],
      
      tests_require=tests_require,
      extras_require=dict(tests=tests_require),
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
