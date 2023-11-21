import os


def apply(fun, dir):
    data=[0]*100
    for i in range(0,100):
        path=os.path.join(dir, str(i + 1))
        if os.path.exists(path):
            data[i]=fun(path)
    return data


def boxplot_apply(fun, dir):
    data = []
    for i in range(0,100):
        data.append([])
        path=os.path.join(dir, str(i + 1))
        if os.path.exists(path):
            for img in os.listdir(path):
                data[i].append(fun(os.path.join(path, img)))
    return data 
