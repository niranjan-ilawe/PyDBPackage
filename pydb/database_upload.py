import psycopg2.extras as extras
import psycopg2


def batch_upload_df(
    conn, df, tablename, page_size=100, insert_type="insert_only", key_cols="wo"
):
    """Uploads a pandas dataframe to specificied table

    Parameters:
        conn (connection object): Connection object to the database where tablename exists
        df (DataFrame): Pandas dataframe object
        tablename (str): table where data is to be uploaded
        page_size (int): Default 100, batch size of page uploads
        insert_type (str): Can take "insert_only" (just inserts),
                           "update" (overwrites existing data and adds new data based on the key_cols),
                           "refresh" (deletes everything in the table and inserts new data)
        key_cols (str): Column to be considered as the PK for getting unique rows

    Returns:
        result (int): 0 if successful, 1 if error

    Notes:
        The DataFrame must have the exact columns as the table where data is to be uploaded

    """

    if len(df) < 1:
        print("Empty dataframe. Nothing to upload")
        return 0

    cursor = conn.cursor()

    if insert_type == "update":
        new_wo = tuple(df.wo.unique().astype(str))

        if len(new_wo) <= 1:
            cursor.execute(f"DELETE FROM {tablename} WHERE {key_cols} = '{new_wo[0]}';")
            conn.commit()
        else:
            cursor.execute(f"DELETE FROM {tablename} WHERE {key_cols} IN {new_wo};")
            conn.commit()

    if insert_type == "refresh":
        cursor.execute(f"DELETE FROM {tablename};")
        conn.commit()

    # Get raw data into a list of tuples
    tuples = [tuple(x) for x in df.to_numpy()]

    # This creates 'list' of '%s' equal to the number of columns
    num_of_col_list = len(df.columns) * ("%s",)
    str_replacements = ",".join(num_of_col_list)

    # create a comma separated list of column names
    cols = ",".join(list(df.columns))

    # create the actual SQL string
    query = f"INSERT INTO {tablename}({cols}) VALUES ({str_replacements})"

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

    print("Data uploaded successfully")
    cursor.close()
    return 0
