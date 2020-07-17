import logging

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
        self.rects_amount = None
        self.annotation = [[[], [], []], [[], [], []]]

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

    @private
    def set_ylim(self):
        max_value = 0
        for rect in self.rects_values:
            for value in rect:
                if value[self.rects_amount - 1] > max_value:
                    max_value = value[self.rects_amount - 1]
        return max_value

    @private
    def clear_labels(self):
        for i in range(len(self.rects_values)):
            for k in range(self.rects_amount):
                self.annotation[i][k].remove()

    @private
    def set_labels(self, graph_num=0):
        for type_num, bd_type in enumerate(self.comparing_type):
            for rect_id in range(3):
                height = self.rects_values[type_num][graph_num][rect_id]
                self.annotation[type_num][rect_id] = self.ax.annotate('{}'.format(round(height, 3)),
                                                                      xy=(bd_type[rect_id].get_x() + self.bar_width / 2,
                                                                          height),
                                                                      xytext=(0, 3),
                                                                      textcoords="offset points",
                                                                      ha='center', va='bottom')

    def update_labels(self, graph_num):
        self.clear_labels()
        self.set_labels(graph_num)

    def create_graph(self):
        self.graphs_amount = len((self.rects_values[0]))
        self.rects_amount = len(self.labels)
        plt.ylim([0, self.set_ylim() * 1.1])

        x = np.arange(self.rects_amount)
        self.ax.set_xticks(x)
        self.ax.set_xticklabels(self.labels)
        self.set_signatures()
        self.comparing_type = [self.ax.bar(x - self.bar_width / 2, self.rects_values[0][0], self.bar_width,
                                           label='Clickhouse'),
                               self.ax.bar(x + self.bar_width / 2, self.rects_values[1][0], self.bar_width,
                                           label='Postgres')]
        self.ax.legend(loc='upper left')
        self.set_labels()

        self.fig.canvas.mpl_connect('scroll_event', self.onscroll)
        plt.show()

    def update_graph(self, graph_id):
        for type_id, type in enumerate(self.comparing_type):
            for rect_id in range(self.rects_amount):
                type[rect_id].set_height(self.rects_values[type_id][graph_id][rect_id])
        self.ax.set_ylabel('Query %s' % self.graph_id)
        plt.draw()

    def onscroll(self, event):
        if event.button == 'up':
            graph_id = self.get_prev_id()
        else:
            graph_id = self.get_next_id()
        self.update_labels(graph_id)
        self.update_graph(graph_id)


matplotlib.rcParams['toolbar'] = 'None'

# rects_values = [[[4, 17, 10],
#                  [10, 14, 10],
#                  [10, 4, 18],
#                  [15, 28, 7]],
#                 [[5, 10, 50],
#                  [20, 4, 20],
#                  [10, 14, 10],
#                  [25, 18, 10]]]
#
# graph = Graph(rects_values)
# graph.create_graph()
