from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='izug.tagging',
      version=version,
      description="Tagging add-on for iZug",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='izug tagging plone',
      author='Christian Schneider, 4teamworkk GmbH',
      author_email='christian.schneider@4teamwork.ch',
      url='https://svn.4teamwork.ch/repos/zug/izug.tagging',
      license='Copyright 2009, 4teamwork GmbH',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['izug'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
