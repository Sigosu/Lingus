import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Lingus",
    version="0.0.1",
    author="Sigosu",
    author_email="s.sigosu@gmail.com",
    description="Unofficial Duolingo API package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Sigosu/Lingus",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.9",
)