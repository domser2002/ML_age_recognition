import numpy
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

def histogram(data,title,xlabel,ylabel,filename):
    fig, ax = plt.subplots()
    for axis in [ax.xaxis, ax.yaxis]:
        axis.set_major_locator(ticker.MaxNLocator(integer=True))
    plt.bar(numpy.array(list(range(1, len(data) + 1))), numpy.array(data))
    ymin=min(data)
    ymax=max(data)
    plt.ylim(ymin, ymax)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.savefig(filename)