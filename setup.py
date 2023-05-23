import os
import setuptools
from pip._internal.req import parse_requirements

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

INSTALL_REQS = parse_requirements("requirements.txt", session="hack")

try:
    REQS = [str(ir.req) for ir in INSTALL_REQS]
except AttributeError:
    REQS = [str(ir.requirement) for ir in INSTALL_REQS]

setuptools.setup(
    name='src spark app',
    version="0.0.2",
    author="Takeda",
    author_email="takeda@takeda.com",
    description="spark runner",
    include_package_data=True,
    zip_safe=False,
    install_requires=REQS,
    package_data={
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.conf'],
    },
    packages=setuptools.find_packages(include=
    [
        'src_spark_app*'
    ]),
    setup_requires=[],
    py_modules=[],
    python_requires=">=3.7"
)
