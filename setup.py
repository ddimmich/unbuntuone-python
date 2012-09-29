import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()
LICENSE = open(os.path.join(here, 'LICENSE.txt')).read()

requires = [
        'python-oauth2',
        'httplib2',
        'watchdog',
    ]

setup(name='ubuntuone',
      version='1.0',
      description='A python library/tool to download files from ubuntu',
      long_description=README + '\n\n' +  CHANGES,
      classifiers=[
      'Development Status :: 5 - Production/Stable',
      'Environment :: Web Environment',
      'Intended Audience :: Developers',
      'License :: OSI Approved :: BSD License',
      'Programming Language :: Python',
      'Programming Language :: Python :: 2.6',
      'Programming Language :: Python :: 2.7',
      'Topic :: Internet :: WWW/HTTP :: ubuntu one',
        ],
      author='Damian Dimmich, Tauri-Tec Ltd',
      author_email='damian@tauri-tec.com',
      url='http://www.tauri-tec.com/',
      license='BSD',
      keywords='web ubuntu one ubuntoone',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      test_suite='ubuntuone',
      install_requires=requires,
      entry_points="""\
      """,
      )

