from pathlib import Path

from setuptools import setup, find_packages

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="owasp-dependency-track-client",
    description="Inofficial OWASP Dependency Track API Python client",
    long_description=long_description,
    long_description_content_type="text/markdown",
    version="0.0.1",
    url="https://github.com/mreiche/owasp-dependency-track-python-client",
    author="Mike Reiche",
    packages=find_packages(),
    install_requires=["httpx>=0.23.0"],
)
