import time, glob

from databases_classes.postgres import Postgres
from databases_classes.clickhouse import ClickHouse


def mean(lst):
    sum = 0
    for t in lst:
        sum += t
    return sum / len(lst)


def run_benchmark(db_class, file):
    times_lst = []
    with open(file) as query_file:
        query = query_file.read()
        for i in range(0, 100):
            start_time = time.time()
            res = db_class.execute_query(query)
            times_lst.append(time.time() - start_time)

            if i % 10 == 0:
                print(res)

    return times_lst


def find_query_files():
    for file in glob.glob("*.sql"):
        yield file


def processing(pg, ch, file):
    times_pg = run_benchmark(pg, file)
    times_ch = run_benchmark(ch, file)

    print("Results of {}".format(file))
    print("\tClickhouse:")
    print("\t\tmin: {:.4}".format(min(times_ch)))
    print("\t\tmax: {:.4}".format(max(times_ch)))
    print("\t\tmean: {:.4}".format(mean(times_ch)))

    print("\tPostgres:")
    print("\t\tmin: {:.4}".format(min(times_pg)))
    print("\t\tmax: {:.4}".format(max(times_pg)))
    print("\t\tmean: {:.4}".format(mean(times_pg)))


if __name__ == "__main__":
    try:
        ch = ClickHouse('localhost')
        pg = Postgres('localhost', 'postgres', 'postgres')

        for file in find_query_files():
            processing(pg, ch, file)

        ch.close_connect()
        pg.close_connect()
    except Exception as exc:
        print(exc)

input()
