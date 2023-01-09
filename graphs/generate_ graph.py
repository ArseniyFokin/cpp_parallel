"""
Создание графиков
"""
from typing import List

from matplotlib import pyplot as plt, ticker


def get_graph(sub_plt, threads: List[int], seconds: List[float], plt_title: str, x_label: str = None, y_label: str = None):
    sub_plt.xaxis.set_major_locator(ticker.MaxNLocator(integer=True))
    sub_plt.yaxis.set_major_locator(ticker.MaxNLocator(integer=True))
    sub_plt.plot(threads, seconds, marker='o')
    sub_plt.set_title(plt_title)
    sub_plt.set_xlabel(x_label or 'Threads')
    sub_plt.set_ylabel(y_label or 'Seconds')

    return sub_plt


def get_open_mp():
    _, sub_plt = plt.subplots()
    size_matrix = 1500
    count_thread = range(1, 9)
    times = [14.9935, 8.2823, 5.55732, 4.03902, 3.7224, 3.68607, 3.57816, 3.5225]
    get_graph(sub_plt, count_thread, times, f'Matrix: {size_matrix}x{size_matrix}')
    plt.savefig('./graphs/open_mp.png')


def get_mpi():
    _, sub_plt = plt.subplots()
    size_matrix = 2000
    count_thread = range(1, 5)
    times = [29.6113, 17.1521, 13.452, 13.0561]
    get_graph(sub_plt, count_thread, times, f'Matrix: {size_matrix}x{size_matrix}')
    plt.savefig('./graphs/mpi.png')


def get_cuda():
    size_matrix = 1024
    fig, sub_plts = plt.subplots(nrows=3, ncols=1, figsize=(10,16))
    get_graph(sub_plts[0], [64, 128, 256, 512], [73.3202, 36.563, 18.53, 10.0764], f'Blocks = 2, Matrix: {1024}x{1024}')
    get_graph(sub_plts[1], [8, 16, 32, 64, 128], [36.1093, 18.1891, 9.23977, 4.70499, 2.97855], f'Blocks = 32, Matrix: {2948}x{2048}')
    get_graph(sub_plts[2], [2, 3, 4], [51.9329, 34.7437, 21.2197], f'Threads = 1024, Matrix: {4096}x{4096}', x_label='Blocks')

    plt.savefig('./graphs/cuda.png')


get_open_mp()
get_mpi()
get_cuda()
