import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np

def draw_histogram(files):
    # extract file names
    names = [files[x]['a']['n'] for x in files]

    # extract names of photos and from them extract age
    photo_names = [x for x in names if x.startswith('photo')]
    photo_ages = [int(x.split(' ')[3]) for x in photo_names]

    # load utc and wiki count distribution
    # and add counts from drive
    # then save result to rozklad_utc_wiki_scraping.csv
    dist = pd.read_csv('rozklad_utc_wiki.csv')
    dist = dist.drop('Unnamed: 0', axis=1)
    keys, values = Counter(photo_ages).keys(), list(Counter(photo_ages).values())
    for count, key in enumerate(keys):
        dist.loc[key - 1]['count'] += values[count]
    dist.to_csv('rozklad_utc_wiki_scraping.csv')

    # plot final distribution barplot
    # and line y = 500
    # then save plot to jpg file
    plt.bar(np.array(dist['age']), np.array(dist['count']))
    plt.plot(np.array([1, 100]), np.array([500, 500]), color='red')
    plt.ylim(0,800)
    plt.title('Liczba zdjęć w całym datasecie (UTK + Wiki + web scraping)')
    plt.xlabel('Wiek')
    plt.ylabel('Liczba zdjęć')
    plt.savefig('rozklad.jpg')
    return