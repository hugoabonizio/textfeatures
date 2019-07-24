import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="textfeatures",
    version="0.1.0",
    author="Hugo Abonizio",
    author_email="hugo.abonizio@gmail.com",
    description="A package to extract textual features",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hugoabonizio/textfeatures",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)