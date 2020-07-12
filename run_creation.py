from creation import dataset_reader
import time

from classes.clickhouse import ClickHouse
from classes.postgres import Postgres

if __name__ == "__main__":
    ch = None
    pg = None
    try:
        print("Databases creation is started...\n")

        ch = ClickHouse('localhost')
        pg = Postgres('localhost', 'postgres', 'postgres')

        ch.create_table()
        pg.create_table()
        
        for file in dataset_reader.get_csv_files():
            start_time = time.time()
            dataset = dataset_reader.read_dataset(file)
            print("Created dataset: {} sec. from {}".format(time.time() - start_time, file))
       
            start_time = time.time()
            ch.insert_data(dataset)
            print("Inserted to ClickHouse: {} sec. ".format(time.time() - start_time))

            start_time = time.time()
            pg.insert_data(dataset)
            print("Inserted to Postgres: {} sec. ".format(time.time() - start_time))
            
    except Exception as exc:
        print(exc)
    
    finally:
        print("\nDatabases creation is finished")
        ch.close_connect()
        if pg:
            pg.close_connect()

    input()
