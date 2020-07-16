import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from accessify import private



class Graph:
    def __init__(self, rects_values):
        self.rects_values = rects_values

        self.fig, self.ax = plt.subplots()

        self.bar_width = 0.35
        self.graph_id = 0
        self.comparing_type = None
        self.graphs_amount = None

        self.labels = ['min', 'mean', 'max']

    @private
    def get_next_id(self):
        self.graph_id += 1
        if self.graph_id == self.graphs_amount:
            self.graph_id = 0
        return self.graph_id

    @private
    def get_prev_id(self):
        self.graph_id -= 1
        if self.graph_id == -1:
            self.graph_id = self.graphs_amount - 1
        return self.graph_id

    @private
    def set_signatures(self):
        self.fig.canvas.set_window_title('Time for queries')
        self.ax.set_title('Time for 100 repeats in seconds\n')
        self.ax.set_ylabel('Query %s' % self.graph_id)
        self.ax.set_xlabel('scroll to see more')

    def create_graph(self):
        plt.ylim([0, 0.5])

        self.graphs_amount = len((self.rects_values[0]))

        x = np.arange(len(self.labels))
        self.ax.set_xticks(x)
        self.ax.set_xticklabels(self.labels)
        self.set_signatures()
        self.comparing_type = [self.ax.bar(x - self.bar_width / 2, self.rects_values[0][0], self.bar_width,
                                           label='Clickhouse'),
                               self.ax.bar(x + self.bar_width / 2, self.rects_values[1][0], self.bar_width,
                                           label='Postgres')]
        self.ax.legend()

        self.fig.canvas.mpl_connect('scroll_event', self.onscroll)
        plt.show()

    def update_graph(self, graoh_id):
        for type_id, type in enumerate(self.comparing_type):
            for rect_id in range(len(self.rects_values[0][0])):
                type[rect_id].set_height(self.rects_values[type_id][graoh_id][rect_id])
        self.ax.set_ylabel('Query %s' % self.graph_id)
        plt.draw()

    def onscroll(self, event):
        print("%s %s" % (event.button, event.step))
        if event.button == 'up':
            graph_id = self.get_prev_id()
            self.update_graph(graph_id)
        else:
            graph_id = self.get_next_id()
            self.update_graph(graph_id)


matplotlib.rcParams['toolbar'] = 'None'

rects_values = [[[4, 17, 10],
                 [10, 14, 10],
                 [15, 28, 7]],
                [[5, 10, 30],
                 [20, 4, 20],
                 [25, 18, 10]]]

# graph = Graph(rects_values)
# graph.create_graph()
