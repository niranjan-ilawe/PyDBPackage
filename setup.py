from setuptools import setup

setup(
    name="pydb",
    version="0.0.2",
    description="Python package for querying 10X DBs",
    url="https://github.com/niranjan-ilawe/PyDBPackage",
    author="niranjan.ilawe",
    author_email="niranjan.ilawe@10xgenomics.com",
    license="MIT",
    packages=["pydb"],
    install_requires=["psycopg2-binary", "keyring"],
    dependency_links=["http://github.com"],
    zip_safe=False,
)
