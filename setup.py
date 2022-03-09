import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="designsafe_db",
    version="0.0.2",
    author="Scott J. Brandenberg",
    author_email="sjbrandenberg@ucla.edu",
    description="DesignSafe relational database connection scripts",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sjbrandenberg/DesignSafe_db_scripts",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
