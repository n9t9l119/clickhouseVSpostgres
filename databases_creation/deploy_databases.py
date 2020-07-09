import dataset_reader, time

from postgres_creation import Postges
from clickhouse_creation import ClickHouse

if __name__ == "__main__":
    try:
        ch = ClickHouse('localhost')
        pg = Postges('localhost', 'postgres', 'postgres')

        # start_time = time.time()
        # dataset = dataset_reader.read_dataset()
        # print("create csv tuple v1: %s sec. " % (time.time() - start_time))

        # start_time = time.time()
        # dataset = dataset_reader.read_dataset2()
        # print("create csv tuple v2: %s sec. " % (time.time() - start_time))

        start_time = time.time()
        dataset = dataset_reader.read_dataset()
        print("create csv tuple v3: %s sec. " % (time.time() - start_time))

        start_time = time.time()
        ch.create_and_insert(dataset)
        print("insert ch: %s sec. " % (time.time() - start_time))

        start_time = time.time()
        pg.create_and_insert(dataset)
        print("insert pg: %s sec. " % (time.time() - start_time))

        # start_time = time.time()
        # pg.create_and_insert2(dataset)
        # print("insert pg: %s sec. " % (time.time() - start_time))

        ch.close_connect()
        pg.close_connect()

    except Exception as exc:
        print(exc)

    input()
