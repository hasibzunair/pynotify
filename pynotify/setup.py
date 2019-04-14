import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pynotify",
    version="0.0.4",
    author="Hasib Zunair",
    author_email="hasibzunair@gmail.com",
    description="A Python package to send emails like a human.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hasibzunair/pynotify",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
