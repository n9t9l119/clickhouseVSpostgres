def create_table(ch_cursor):
    ch_cursor.execute('''CREATE TABLE IF NOT EXISTS benchmark
                       ( id Int32, 
                        col1 String,
                        col2 String,
                        col3 String,
                        col4 String,
                        col5 String
                      )Engine=Log()''')


def insert_data(ch_cursor, tuple_lst):
    ch_cursor.execute('INSERT INTO benchmark (id, col1, col2, col3, col4, col5) VALUES', tuple_lst)


def click(ch_cursor, tuple_lst):
    create_table(ch_cursor)
    insert_data(ch_cursor, tuple_lst)

    # ch_cursor.execute('''SELECT t.id, Count(*)
    # FROM (SELECT id FROM benchmark) as t
    # GROUP BY t.id
    # HAVING Count(*) == 1''')
    #
    # ch_cursor.execute('''SELECT Count(*) FROM benchmark''')
