import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="todocmd",
    version="1.0.0",
    description="simple todo command line   application",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/ppmadalin/todocmd.madalinpopa.com",
    author="Madalin Popa",
    author_email="contact@madalinpopa.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["src"],
    include_package_data=True,
    install_requires=["pytest"],
    console=["termctrl.py"],
)
