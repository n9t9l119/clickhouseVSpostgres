from databases_creation import dataset_reader
import time

from databases_classes.clickhouse import ClickHouse
from databases_classes.postgres import Postgres


if __name__ == "__main__":
    ch = None
    pg = None
    try:
        ch = ClickHouse('localhost')
        pg = Postgres('localhost', 'postgres', 'postgres')

        dataset = dataset_reader.read_dataset()

        ch.create_and_insert(dataset)
        pg.create_and_insert(dataset)

        print("finished creation")

    except Exception as exc:
        print(exc)
    
    finally:
        ch.close_connect()
        if pg:
            pg.close_connect()

    input()
