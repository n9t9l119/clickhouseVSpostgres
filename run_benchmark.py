from benchmark import check_time
from classes.clickhouse import ClickHouse
from classes.postgres import Postgres

from graphic import Graph

if __name__ == "__main__":
    ch = None
    pg = None
    try:
        print("Benchmark is started...")

        ch = ClickHouse('localhost')
        pg = Postgres('localhost', 'postgres', 'postgres')

        pg_results = []
        ch_results = []

        for file in check_time.find_query_files():
            results = check_time.run_benchmark(pg, ch, file)

            ch_results.append(results[0])
            pg_results.append(results[1])

    except Exception as exc:
        print(exc)

    finally:
        print("\nBenchmark is finished")
        ch.close_connect()
        if pg:
            pg.close_connect()

    test = [ch_results, pg_results]
    print (test)
    graph = Graph(test)
    graph.create_graph()

input()
