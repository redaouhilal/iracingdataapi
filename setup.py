import setuptools

from pathlib import Path
readme = Path("README.md")
long_description = readme.read_text(encoding="utf-8") if readme.exists() else ""

setuptools.setup(
    name="iracingdataapi",
    version="1.2.3",
    author="Jason Dilworth",
    author_email="hello@jasondilworth.co.uk",
    description="A simple wrapper around the iRacing General Data API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jasondilworth56/iracingdataapi",
    project_urls={
        "Bug Tracker": "https://github.com/jasondilworth56/iracingdataapi/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=["requests"],
)
