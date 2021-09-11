import os, re

from distutils.command.install import INSTALL_SCHEMES
for scheme in INSTALL_SCHEMES.values():
    scheme['data'] = scheme['purelib']

from setuptools import setup

version_re = re.compile("""__version__[\s]+=[\s]*['|"](.*)['|"]""")

prjdir = os.path.dirname(__file__)

with open('jc/__init__.py', 'r', encoding="utf-8") as f:
    content = f.read()
    match =version_re.search(content)
    version = match.group(1)

def read(filename):
    return open(os.path.join(prjdir, filename)).read()

long_description = read('README.md')

setup(
    name='justconnect',
    incude_package_data=True,
    version=version,
    description=('A Lazy SSH Command Line Helper'),
    long_description='',
    url='https://github.com/addy3494/jc',
    author='addy3494',
    author_email='adithya3494@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Terminals',
    ],
    py_modules = ['jc',],
    package = ['jc',],
    install_requires = [
        'plumbum>=1.7.0',
        'pyfzf>=0.2.2',
    ],
)
