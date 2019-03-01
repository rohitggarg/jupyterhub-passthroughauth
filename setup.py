from setuptools import setup, find_packages
from os import path
from io import open

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='jupyterhub-passthrough',
    version='0.0.1',
    description='Pass-through authentication for jupyterhub, enabling direct access to the session of a particular locked down user.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/rohitggarg/jupyterhub-passthrough',
    author='Rohit Garg',
    author_email='rohitgarg19@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: JupyterHub Users',
        'Topic :: Software Development :: JupyterHub :: Login :: Guest Access',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='jupyter jupyterhub login autologin pass through guest access',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    python_requires='>=2.7, <4',
    install_requires=['jupyterhub'],
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },
    project_urls={
        'Bug Reports': 'https://github.com/rohitggarg/jupyterhub-passthrough/issues',
        'Funding': 'https://donate.pypi.org',
        'Say Thanks!': 'https://github.com/rohitggarg/jupyterhub-passthrough',
        'Source': 'https://github.com/rohitggarg/jupyterhub-passthrough',
    },
)
