import matplotlib.pyplot as plt

# figsize specifies width and height of the plot
def boxplot(x, labels, xlabel='', ylabel='', title='', figsize=(7,6)):
    plt.figure(figsize=figsize)
    plt.boxplot(x, labels=labels)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()