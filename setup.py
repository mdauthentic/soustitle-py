import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="soustitle-py",
    version="0.0.1",
    author="Muideen Lawal",
    author_email="muideen.lawal320@gmail.com",
    description="A simple python srt parser",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mdauthentic/soustitle-py",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)