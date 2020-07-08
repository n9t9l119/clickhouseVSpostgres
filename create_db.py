from csv_tuple import create_csv_tuple3
from csv_tuple import create_csv_tuple2
from csv_tuple import create_csv_tuple

from postgres_creation import Postges
from clickhouse_creation import ClickHouse

import time

ch = ClickHouse()
pg = Postges()

start_time = time.time()
dataset = create_csv_tuple()
print("create csv tuple v1: %s sec. " % (time.time() - start_time))

start_time = time.time()
dataset = create_csv_tuple2()
print("create csv tuple v2: %s sec. " % (time.time() - start_time))

start_time = time.time()
dataset = create_csv_tuple3()
print("create csv tuple v3: %s sec. " % (time.time() - start_time))

start_time = time.time()
ch.create_and_insert(dataset)
print("insert ch: %s sec. " % (time.time() - start_time))

start_time = time.time()
pg.create_and_insert(dataset)
print("insert pg: %s sec. " % (time.time() - start_time))

start_time = time.time()
pg.create_and_insert2(dataset)
print("insert pg: %s sec. " % (time.time() - start_time))

ch.close_connect()
pg.close_connect()
