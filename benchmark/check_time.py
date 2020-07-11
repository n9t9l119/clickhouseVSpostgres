import glob
import time
from prettytable import PrettyTable


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


def run_benchmark(pg, ch, file):
    times_pg = run_query(pg, file)
    times_ch = run_query(ch, file)

    columns = ["", 'Clickhouse', "Postgres"]
    rows = ['min', min(times_ch), min(times_pg),
            'mean', mean(times_ch), mean(times_pg),
            'max', max(times_ch), max(times_pg)]
    table = PrettyTable(columns)

    while rows:
        table.add_row(rows[:3])
        rows = rows[3:]

    benchmark_num = "Results of " + file

    print(benchmark_num.center(20))
    print(table)

#     return '''Results of {0}
#         Clickhouse
#         min: {1:.4}
#         max: {2:.4}
#         mean: {3:.4}
#     Postgres:
#         min: {4:.4}
#         max: {5:.4}
#         mean: {6:.4}
# '''.format(file, min(times_ch), max(times_ch), mean(times_ch), min(times_pg), max(times_pg), mean(times_pg))
