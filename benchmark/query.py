import time
import glob

import output


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


def send_requests(pg, ch, file):
    times_pg = run_query(pg, file)
    times_ch = run_query(ch, file)

    ch_time = [min(times_ch), mean(times_ch), max(times_ch)]
    pg_time = [min(times_pg), mean(times_pg), max(times_pg)]

    return ch_time, pg_time


def run_benchmark(pg, ch, files):
    ch_results = []
    pg_results = []

    for file in files:
        benchmark_results = send_requests(pg, ch, file)

        ch_results.append(benchmark_results[0])
        pg_results.append(benchmark_results[1])

        output.print_table(file, benchmark_results[0], benchmark_results[1])

    output.show_graphs([ch_results, pg_results])
