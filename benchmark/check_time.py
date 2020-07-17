import glob
import time
from prettytable import PrettyTable

from graphic import Graph


def mean(lst):
    sum = 0
    for t in lst:
        sum += t
    return sum / len(lst)


def run_query(db_class, file):
    times_lst = []
    with open(file) as query_file:
        query = query_file.read()
        for i in range(0, 100):
            start_time = time.time()
            db_class.execute_query(query)
            times_lst.append(time.time() - start_time)
    return times_lst


def find_query_files():
    for file in glob.glob("sql\\*.sql"):
        yield file


def print_table(file, chs, pgs):
    columns = ["", 'Clickhouse', "Postgres"]
    rows = ['Min', chs[0], pgs[0],
            'Mean', chs[1], pgs[1],
            'Max', chs[2], pgs[2]]
    table = PrettyTable(columns)

    while rows:
        table.add_row(rows[:3])
        rows = rows[3:]

    benchmark_num = "\nResults of " + file[4:]
    print(benchmark_num.center(20))

    print(table)


def show_graphs(results):
    graph = Graph(results)
    graph.create_graph()


def run_benchmark(pg, ch, files):
    pg_results = []
    ch_results = []

    for file in files:
        times_pg = run_query(pg, file)
        times_ch = run_query(ch, file)

        ch_time = [min(times_ch), mean(times_ch), max(times_ch)]
        pg_time = [min(times_pg), mean(times_pg), max(times_pg)]

        ch_results.append(ch_time)
        pg_results.append(pg_time)

        print_table(file, ch_time, pg_time)
    show_graphs([ch_results, pg_results])

