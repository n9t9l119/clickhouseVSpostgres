from psycopg2.extras import execute_values


def create_table(pg_cursor):
    pg_cursor.execute('''CREATE TABLE IF NOT EXISTS benchmark
                       ( id int, 
                        col1 text,
                        col2 text,
                        col3 text,
                        col4 text,
                        col5 text
                      )''')


def insert_data(pg_cursor, tuple_lst):
    for i in range(1, 11):
        print(i * 10000)
        execute_values(pg_cursor, "INSERT INTO benchmark (id, col1, col2, col3, col4, col5) VALUES %s",
                       tuple_lst[(i - 1) * 10000:i * 10000])


def post(pg_cursor, tuple_lst):
    create_table(pg_cursor)
    insert_data(pg_cursor, tuple_lst)

    # pg_cursor.execute('''SELECT t.id, Count(*)
    # FROM (SELECT id FROM benchmark) as t
    # GROUP BY t.id
    # HAVING Count(*) = 1''')
    #
    # pg_cursor.execute('''SELECT Count(*) FROM benchmark''')
    # pg_cursor.fetchall()
