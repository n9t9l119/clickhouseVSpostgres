from creation import dataset_reader
import time

from classes.clickhouse import ClickHouse
from classes.postgres import Postgres

if __name__ == "__main__":
    ch = None
    pg = None
    try:
        print("Started creation")

        ch = ClickHouse('localhost')
        pg = Postgres('localhost', 'postgres', 'postgres')

        dataset = []
        start_time = time.time()
        for file in dataset_reader.get_csv_files():
            dataset.extend(dataset_reader.read_dataset(file))
        print("Created dataset: {} sec. ".format(time.time() - start_time))
       
        start_time = time.time()
        ch.create_and_insert(dataset)
        print("Inserted to ClickHouse: {} sec. ".format(time.time() - start_time))

        start_time = time.time()
        pg.create_and_insert(dataset)
        print("Inserted to Postgres: {} sec. ".format(time.time() - start_time))
    except Exception as exc:
        print(exc)
    
    finally:
        print("Finished creation")
        ch.close_connect()
        if pg:
            pg.close_connect()

    input()
