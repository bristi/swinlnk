from setuptools import setup
from swinlnk import __version__, __author__, __email__

def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='swinlnk',
      version=__version__,
      description='Create windows shortcuts (.lnk files) from anywhere',
      long_description=readme(),
      # Complete list of available classifiers:
      # https://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries',
      ],
      keywords='lnk',
      url='http://github.com/bristi/swinlnk',
      author=__author__,
      author_email=__email__,
      license='MIT',
      packages=['swinlnk'],
      install_requires=[
      ],
      setup_requires=[
          'pytest-runner',
      ],
      tests_require=[
          'pytest',
      ],
      include_package_data=True,
      zip_safe=False)