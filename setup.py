from setuptools import setup, find_packages

VERSION="0.1"

setup(
    name="dotamatch",
    version=VERSION,

    description="Python bindings for the Dota 2 match API",
    author="Mac Chapman",
    author_email="mac@veryhappythings.co.uk",
    url="http://www.veryhappythings.co.uk",

    install_requires = [
        "requests",
    ],
    entry_points = {
    },
    zip_safe=False,
    include_package_data=True,
    packages=find_packages(),
    package_data = {
    },
    data_files = [
    ],

    keywords = [
    ],
    classifiers = [
    ],
)

