import dataset_reader, time

from database_classes.postgres import Postges
from database_classes.clickhouse import ClickHouse

if __name__ == "__main__":
    try:
        ch = ClickHouse('localhost')
        pg = Postgres('localhost', 'postgres', 'postgres')

        start_time = time.time()
        dataset = dataset_reader.read_dataset()
        print("reading dataset: %s sec. " % (time.time() - start_time))

        start_time = time.time()
        ch.create_and_insert(dataset)
        print("insert ch: %s sec. " % (time.time() - start_time))

        start_time = time.time()
        pg.create_and_insert(dataset)
        print("insert pg: %s sec. " % (time.time() - start_time))

        ch.close_connect()
        pg.close_connect()

    except Exception as exc:
        print(exc)

    input()
