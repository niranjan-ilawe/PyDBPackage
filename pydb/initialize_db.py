import psycopg2
import sys

def initialize_db(db_name):

    conn = None
    dbs = {
        'personal': {
            "host"      : "localhost",
            "database"  : "niranjan.ilawe",
            "user"      : "niranjan.ilawe",
            "password"  : ""
        },
        'postgres': {
            "host"      : "cpdda.c7qfiffzqhfr.us-west-2.rds.amazonaws.com",
            "database"  : "cpdda",
            "user"      : "cpdda",
            "password"  : ">TKd=lN7>jUiXTK.pSKV"
        }
    }

    try:
        print(f'Connecting to the {db_name} database...')
        conn = psycopg2.connect(**dbs[db_name])
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        sys.exit(1) 
    print("Connection successful")
    return conn
