import psycopg2, random, string
from clickhouse_driver import Client
from psycopg2.extras import execute_values


def random_word(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


pg_con = psycopg2.connect(dbname='postgres', user='postgres', host='localhost')
pg_con.autocommit = True
pg_cursor = pg_con.cursor()

ch_cursor = Client(host='localhost')

pg_cursor.execute('''CREATE TABLE IF NOT EXISTS benchmark
                   ( id int, 
                    col1 text,
                    col2 text,
                    col3 text,
                    col4 text,
                    col5 text
                  )''')

ch_cursor.execute('''CREATE TABLE IF NOT EXISTS benchmark
                   ( id Int32, 
                    col1 String,
                    col2 String,
                    col3 String,
                    col4 String,
                    col5 String
                  )Engine=Log()''')

tuple_lst = []

for i in range(0, 1000000):
    tuple_lst.append(
        (random.randint(0, 100000), random_word(10), random_word(15), random_word(20), random_word(25), random_word(30)))
    if i % 100000 == 0:
        print(i)

for i in range(1, 11):
    print(i * 100000)
    execute_values(pg_cursor, "INSERT INTO benchmark (id, col1, col2, col3, col4, col5) VALUES %s",
                   tuple_lst[(i - 1) * 100000:i * 100000])

ch_cursor.execute('INSERT INTO benchmark (id, col1, col2, col3, col4, col5) VALUES', tuple_lst)

ch_cursor.execute('''SELECT t.id, Count(*)
FROM (SELECT id FROM benchmark) as t
GROUP BY t.id
HAVING Count(*) == 1''')

pg_cursor.execute('''SELECT t.id, Count(*)
FROM (SELECT id FROM benchmark) as t
GROUP BY t.id
HAVING Count(*) = 1''')

pg_cursor.fetchall()
ch_cursor.execute('''SELECT Count(*) FROM benchmark''')
pg_cursor.execute('''SELECT Count(*) FROM benchmark''')
pg_cursor.fetchall()
