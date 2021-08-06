import psycopg2.extras as extras
import psycopg2

def batch_upload_df(conn, df, tablename, page_size=100):

    tuples = [tuple(x) for x in df.to_numpy()]
    num_of_col_list = len(df.columns)*("%s",)
    str_replacements = ",".join(num_of_col_list)
    cols = ','.join(list(df.columns))
    query  = f"INSERT INTO {tablename}({cols}) VALUES ({str_replacements})"
    cursor = conn.cursor()
    try:
        extras.execute_batch(cursor, query, tuples, page_size=page_size)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        conn.rollback()
        cursor.close()
        return 1
    print("execute_batch() done")
    cursor.close()
    return 0
