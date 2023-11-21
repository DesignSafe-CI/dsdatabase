# DS Database

[![build and test](https://github.com/DesignSafe-CI/dsdatabase/actions/workflows/build-test.yml/badge.svg)](https://github.com/DesignSafe-CI/dsdatabase/actions/workflows/build-test.yml)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE.md)

`dsdatabase` is a library that simplifies accessing databases on [DesignSafe](https://designsafe-ci.org) via [Jupyter Notebooks](https://jupyter.designsafe-ci.org).

## Features

Connects to SQL databases on DesignSafe:

| Database | dbname |
|----------|--------|
| NGL | `ngl`|
| Earthake Recovery | `eq` |
| Vp | `vp` |


## Installation

Install `dsdatabase` via pip

```shell
pip3 install dsdatabase
```

To install the current development version of the library use:

```shell
pip install git+https://github.com/DesignSafe-CI/dsdatabase.git --quiet
```

## Example usage:
```python
db = DSDatabase(dbname="ngl")

# Optionally, close the database connection when done
db.close()
```