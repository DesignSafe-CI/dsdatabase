# DS Database

[![build and test](https://github.com/DesignSafe-CI/dsdatabase/actions/workflows/build-test.yml/badge.svg)](https://github.com/DesignSafe-CI/dsdatabase/actions/workflows/build-test.yml)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE.md)

`dsdatabase` is a library that simplifies accessing databases on [DesignSafe](https://designsafe-ci.org) via [Jupyter Notebooks](https://jupyter.designsafe-ci.org).

## Features

Connects to SQL databases on DesignSafe:

| Database | dbname | env_prefix |
|----------|--------|------------|
| NGL | `ngl`| `NGL_` |
| Earthake Recovery | `eq` | `EQ_` |
| Vp | `vp` | `VP_` |

Define the following environment variables:
```
{env_prefix}DB_USER
{env_prefix}DB_PASSWORD
{env_prefix}DB_HOST
{env_prefix}DB_PORT
```

For e.g., to add the environment variable `NGL_DB_USER` edit `~/.bashrc`, `~/.zshrc`, or a similar shell-specific configuration file for the current user and add `export NGL_DB_USER="dspublic"`.

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
from dsdatabase.db import DSDatabase

db = DSDatabase("ngl")
sql = 'SELECT * FROM SITE'
df = db.read_sql(sql)
print(df)

# Optionally, close the database connection when done
db.close()
```