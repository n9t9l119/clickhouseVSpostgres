from prettytable import PrettyTable

from graphic import Graph


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



