import re
from setuptools import setup

version = ''
with open('janda/__init__.py') as f:
    version = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)


requirements = []
with open('requirements.txt') as f:
    requirements = f.read().splitlines()


if not version:
    raise RuntimeError('version is not set')

readme = ''
with open('README.md', encoding="utf8") as f:
    readme = f.read()

setup(
    name='janda',
    author='sinkaroid',
    author_email='anakmancasan@gmail.com',
    version=version,
    long_description=readme,
    url='https://github.com/sinkaroid/janda',
    project_urls={
        "Documentation": "https://sinkaroid.github.io/janda",
        "Issue tracker": "https://github.com/sinkaroid/janda/issues/new/choose",
        "Funding": "https://paypal.me/sinkaroid",
    },
    packages=['janda', 'janda.utils'],
    license='MIT',
    classifiers=[
        "Framework :: AsyncIO",
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        "Natural Language :: English",
        "Operating System :: OS Independent",
        'Programming Language :: Python :: 3.7',
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Artistic Software",
        "Topic :: Games/Entertainment",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Build Tools",

    ],
    description='A featureful Python library covers most popular doujin API',
    include_package_data=True,
    keywords=['doujinshi', 'library', 'hentai', 'api', 'nhentai',
              'pururin', 'hentaifox', 'hentai2read', 'simply-hentai', 'qhentai', 'asmhentai'],
    install_requires=requirements
)
