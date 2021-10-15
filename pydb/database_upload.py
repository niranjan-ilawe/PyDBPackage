import psycopg2.extras as extras
import psycopg2


def batch_upload_df(conn, df, tablename, page_size=100):
    """Uploads a pandas dataframe to specificied table

    Parameters:
        conn (connection object): Connection object to the database where tablename exists
        df (DataFrame): Pandas dataframe object
        tablename (string): table where data is to be uploaded
        page_size (int): default 100, batch size of page uploads

    Returns:
        result (int): 0 if successful, 1 if error

    Notes:
        The DataFrame must have the exact columns as the table where data is to be uploaded

    """

    # Get raw data into a list of tuples
    tuples = [tuple(x) for x in df.to_numpy()]

    # This creates 'list' of '%s' equal to the number of columns
    num_of_col_list = len(df.columns) * ("%s",)
    str_replacements = ",".join(num_of_col_list)

    # create a comma separated list of column names
    cols = ",".join(list(df.columns))

    # create the actual SQL string
    query = f"INSERT INTO {tablename}({cols}) VALUES ({str_replacements})"
    cursor = conn.cursor()

    # try executing the SQL
    try:
        extras.execute_batch(cursor, query, tuples, page_size=page_size)
        conn.commit()
    # Rollback if any error is encountered
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        conn.rollback()
        cursor.close()
        return 1

    print("execute_batch() done")
    cursor.close()
    return 0
