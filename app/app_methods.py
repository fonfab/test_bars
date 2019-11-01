import sqlite3


def do_request_sql(sql_statement):
    result = "none"
    try:
        conn = sqlite3.connect('db.sqlite3')

        cursor = conn.cursor()

        cursor.execute(sql_statement)
        result = cursor.fetchall()
    except sqlite3.DatabaseError as err:
        print("Error: ", err)
    else:
        conn.commit()

    return result
