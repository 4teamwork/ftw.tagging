from setuptools import setup, find_packages
import os

version = '0.2-dev'
maintainer = 'Mathias Leimgruber'

setup(name='izug.tagging',
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
      keywords='izug tagging plone',
      author='%s, 4teamworkk GmbH' % maintainer,
      author_email='mailto:info@4teamwork.ch',
      url='http://psc.4teamwork.ch/4teamwork/kunden/izug/izug.tagging/',
      license='GPL2',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['izug'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
#          'archetypes.schemaextender',
#          'Products.AddRemoveWidget',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
