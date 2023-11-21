import matplotlib.pyplot as plt
from boxplot import boxplot as b


def boxplot(data, title):
    data1 = data[0]
    for i in range(1, 10):
        data1.extend(data[i])
    data2 = data[84]
    for i in range(85, 100):
        data2.extend(data[i])
    b(x=[data1, data2], labels=["1-10", "85-100"], xlabel="", ylabel="", title=title)
