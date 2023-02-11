from setuptools import setup, find_packages


def readme(): 
    with open('README.md') as f:
        return f.read()


def version():
    with open('metacatalog_api/__version__.py') as f:
        code = f.read()
        loc = dict()
        exec(code, loc, loc)
        return loc['__version__']


def requirements():
    with open('requirements.txt') as f:
        return f.read().splitlines()


setup(
    name='metacatalog_api',
    author='Mirko Mälicke',
    author_email='mirko.maelicke@kit.edu',
    version=version(),
    description='Lightweight FastAPI server for metacatalog',
    long_description=readme(),
    long_description_content_type='text/markdown',
    install_requires=requirements(),
    packages=find_packages()
)