from setuptools import setup


with open("README.md") as readme:
    README = readme.read()
setup(
    name='laevitas-sdk',
    version='1.0.1',
    packages=['laevitas'],
    url='https://github.com/Elyesbdakhlia',
    download_url='https://github.com/Laevitas/laevitas-python-sdk/archive/refs/tags/1.0.0.tar.gz',
    license='apache-2.0',
    author='Elyes',
    author_email='elyes@laevitas.ch',
    description='SDK',
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    install_requires=[
                       'requests',
                   ]

)
