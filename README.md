# pydb
* v0.0.1
---
The *pydb* python package was created to simplify connecting to the **cpdda** database and also provide some basic database utilities such as database upload via python.

## Functions

Currently the *pydb* package contains 2 functions
1. initialize_db
2. batch_upload_df

The usage of these functions are explained below

## Installation

To install the package in python, download the entire repo to your local folder and unzip it. Enter the PyDBPackage folder and run the commands listed below. *If installing in a virtual environment make sure the env is activated*

`python setup.py build`

and then

`python setup.py install`

The package should now be available for use in python

## Usage

1. *initialize_db*

```
from pydb import initialize_db
con = initialize_db(dbname = "postgres")
```

This function creates a connection to the **cpdda** database. The `dbname` variable tells the function which DB to connect to. The function returns a connection object that can be used in the python code to run queries against the database.

2. *batch_upload_df*

```
from pydb import batch_upload_df
res = batch_upload_df(conn = con, df = df, tablename = 'test.ipt')
```

Given a pandas dataframe, connection object, and a name of a table in the connection database, this function will upload the dataframe to the table. The table name given needs to exist. The function is not very intelligent in terms of matching types and checking for constraints.
