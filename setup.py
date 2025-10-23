
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="alphax_time",
    version="0.1.0",
    description="Multi-country flextime & attendance engine for ERPNext HRMS",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Neotec Integrated Solutions",
    author_email="support@neotec.example",
    license="MIT",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
)
