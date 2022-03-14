import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="designsafe_db",
    version="0.0.3",
    author="Scott J. Brandenberg",
    author_email="sjbrandenberg@ucla.edu",
    description="DesignSafe relational database connection scripts",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sjbrandenberg/designsafe_db",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Public License version 3",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'pymysql',
        'pandas',
        'sqlalchemy'
      ],
)
