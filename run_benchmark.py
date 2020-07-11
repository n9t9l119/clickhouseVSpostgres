import time, glob

from classes.postgres import Postgres
from classes.clickhouse import ClickHouse
from benchmark import check_time

if __name__ == "__main__":
    ch = None
    pg = None
    try:
        print("Started benchmark")
        
        ch = ClickHouse('localhost')
        pg = Postgres('localhost', 'postgres', 'postgres')

        for file in check_time.find_query_files():
            print(check_time.run_benchmark(pg, ch, file))

    except Exception as exc:
        print(exc)
    
    finally:
        print("Finished benchmark")
        ch.close_connect()
        if pg:
            pg.close_connect()

input()
