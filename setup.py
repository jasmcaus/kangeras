#pylint:disable=implicit-str-concat

from setuptools import setup, find_packages
import io 

# Repository on PyPi.org = https://pypi.org/project/canaro/

VERSION = '1.0.2'

NAME = 'canaro'
AUTHOR = 'Jason Dsouza'
AUTHOR_EMAIL = 'jasmcaus@gmail.com'
AUTHOR_LONG = AUTHOR + ' <' + AUTHOR_EMAIL + '>'
LICENSE = 'MIT'
URL = 'https://github.com/jasmcaus/canaro'
DOWNLOAD_URL = 'https://pypi.org/project/canaro/'
PACKAGES = find_packages()
KEYWORDS = [
    'computer vision', 'deep learning', 'tensorflow', 'keras', 'convolutional neural networks', 'opencv', 'matplotlib'
]
INSTALL_REQUIRES = [
    'tensorflow'
]
DESCRIPTION = """ A Python library including support for Deep Learning models built using the Keras framework."""
LONG_DESCRIPTION = io.open('LONG_DESCRIPTION.md', encoding='utf-8').read()
# CONTRIBUTORS = io.open('CONTRIBUTORS.md', encoding='utf-8').read()
CLASSIFIERS = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Intended Audience :: Education',
    'Intended Audience :: Science/Research',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3 :: Only',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Operating System :: MacOS :: MacOS X',
    'Operating System :: Microsoft :: Windows',
    'License :: OSI Approved :: MIT License',
]

VERSION_PY_TEXT =\
"""
# This file is automatically generated during the generation of setup.py
# Copyright 2020, canaro
author = '%(author)s'
version = '%(version)s'
full_version = '%(full_version)s'
release = %(isrelease)s
contributors = %(contributors)s
"""

def get_contributors_list(filename='CONTRIBUTORS'):
    contr = [] 
    with open(filename, "r") as a:
        for line in a:
            line = line.strip()
            # line = "'" + line + "'"
            contr.append(line)
    return contr

def write_version(filename='canaro/_meta.py'):
    print('[INFO] Writing _meta.py')
    TEXT = VERSION_PY_TEXT
    FULL_VERSION = VERSION
    ISRELEASED = True
    CONTRIBUTORS = get_contributors_list()

    a = open(filename, 'w')
    try:
        a.write(TEXT % {'author': AUTHOR,
                        'version': VERSION,
                       'full_version': FULL_VERSION,
                       'isrelease': str(ISRELEASED),
                       'contributors': CONTRIBUTORS })
    finally:
        a.close()


def setup_package():
    # Rewrite the version file everytime
    write_version()

    setup(
        name=NAME,
        version=VERSION,
        author=AUTHOR,
        author_email=AUTHOR_EMAIL,
        maintainer=AUTHOR,
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        long_description_content_type='text/markdown',
        url = URL,
        download_url = DOWNLOAD_URL,
        project_urls={
            'Bug Tracker': URL + '/issues',
            'Documentation': URL + '/blob/master/DOCS.md',
            'Source Code': URL,
        },
        packages=find_packages(),
        license=LICENSE,
        install_requires=INSTALL_REQUIRES,
        keywords=KEYWORDS,
        classifiers= [x for x in CLASSIFIERS if x]
    )


if __name__ == '__main__':
    setup_package()