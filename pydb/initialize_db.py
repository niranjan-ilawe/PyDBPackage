import psycopg2
import sys
import keyring


def get_postgres_connection(db_name, service_name, username):
    """Returns a connection object for the specified postgres database

    Parameters:
        db_name (str): Name of the postgres database
        service_name (str): Service name passed on to the keyring function to get the password
        username (str): username passed on to the keyring function to get the password

    Returns:
        conn: Connection object to the specified postgres

    Notes:
        The access credentials to the postgres database must be stored locally in a keyring.
        For details on how to save a password in the keyring can be found here: https://pypi.org/project/keyring/
    """

    conn = None

    password = keyring.get_password(service_name=service_name, username=username)

    dbs = {
        "personal": {
            "host": "localhost",
            "database": "niranjan.ilawe",
            "user": username,
            "password": password,
        },
        "cpdda": {
            "host": "cpdda.c7qfiffzqhfr.us-west-2.rds.amazonaws.com",
            "database": "cpdda",
            "user": username,
            "password": password,
        },
    }

    try:
        print(f"Connecting to the {db_name} database...")
        conn = psycopg2.connect(**dbs[db_name])
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        sys.exit(1)
    print("Connection successful")
    return conn
