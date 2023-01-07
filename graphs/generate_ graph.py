"""
Создание графиков
"""
from typing import List

from matplotlib import pyplot as plt, ticker


def save_graph(threads: List[int], seconds: List[float], title: str, size_matrix: int):
    _, sub_plt = plt.subplots()
    sub_plt.xaxis.set_major_locator(ticker.MaxNLocator(integer=True))
    sub_plt.yaxis.set_major_locator(ticker.MaxNLocator(integer=True))
    sub_plt.plot(threads, seconds)
    plt.title(f'Matrix: {size_matrix}x{size_matrix}')
    plt.xlabel('Count thread')
    plt.ylabel('Seconds')

    plt.savefig(title)


def get_open_mp():
    size_matrix = 1500
    count_thread = range(1, 9)
    times = [14.9935, 8.2823, 5.55732, 4.03902, 3.7224, 3.68607, 3.57816, 3.5225]
    save_graph(count_thread, times, './graphs/open_mp.png', size_matrix)


def get_mpi():
    size_matrix = 2000
    count_thread = range(1, 5)
    times = [29.6113, 17.1521, 13.452, 13.0561]
    save_graph(count_thread, times, './graphs/mpi.png', size_matrix)


get_open_mp()
get_mpi()
