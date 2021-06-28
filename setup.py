import setuptools

requirements = []
with open('requirements.txt') as rtxt:
    requirements = rtxt.read().splitlines()

dependencies = []
with open('dependencies.txt') as dtxt:
    dependencies = dtxt.read().splitlines()

setuptools.setup(
    name="Guilded-Bot",
    version="1.0.0",
    author="GigaClub",
    author_email="business@GigaClub.net",
    url="https://github.com/gigaclub/Guilded-Bot",
    packages=setuptools.find_packages(),
    python_requires=">=3.9",
    install_requires=requirements,
    dependency_links=dependencies
)