# pydb

* v0.0.3
---
get_snowflake_connection was added to connect to the Snowflake DB

* v0.0.2
---
The *pydb* python package was created to simplify connecting to the 10X databases and also provide some basic database utilities such as database upload via python.

## Functions

Currently the *pydb* package contains 2 functions
1. get_postgres_connection
3. get_snowflake_connection
2. batch_upload_df

The usage of these functions are explained below

## Installation

To install the package in python, download the entire repo to your local folder and unzip it. Enter the PyDBPackage folder and run the commands listed below. *If installing in a virtual environment make sure the env is activated*

`python setup.py build`

and then

`python setup.py install`

The package should now be available for use in python

## Usage

1. *get_postgres_connection*

```
from pydb import initialize_db
con = get_postgres_connection(db_name="cpdda", service_name="cpdda-postgres", username="cpdda")
```

This function creates a connection to the **cpdda** database. The `db_name` variable tells the function which DB to connect to. The `service_name` and `username` are passed on to the keyring function to retrieve the password. The function returns a connection object that can be used in the python code to run queries against the database.

1. *get_snowflake_connection*

```
from pydb import initialize_db
con = get_snowflake_connection(service_name="cpdda_snowflake", username="CPD_SNOWFLAKE")
```

This function creates a connection to the **Snowflake** database. The `service_name` and `username` are passed on to the keyring function to retrieve the password. The function returns a connection object that can be used in the python code to run queries against the database.

3. *batch_upload_df*

```
from pydb import batch_upload_df
res = batch_upload_df(conn = con, df = df, tablename = 'test.ipt')
```

Given a pandas dataframe, connection object, and a name of a table in the connection database, this function will upload the dataframe to the table. The table name given needs to exist. The function is not very intelligent in terms of matching types and checking for constraints.
