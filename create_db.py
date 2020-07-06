import psycopg2
from clickhouse_driver import Client
from tuple import create_tuple

from postgres_creation import post
from clickhouse_creation import click

pg_con = psycopg2.connect(dbname='postgres', user='postgres', host='localhost')
pg_con.autocommit = True
pg_cursor = pg_con.cursor()

ch_cursor = Client(host='localhost')

# ch_cursor.execute('''DROP TABLE benchmark''')
# pg_cursor.execute('''DROP TABLE benchmark''')

tuple_lst = create_tuple()


click(ch_cursor, tuple_lst)
post(pg_cursor, tuple_lst)
