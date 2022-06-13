import json
import persist.mongodb as db
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt


def polynomial_analysis():
    data = json.dumps(db.search())
    panda_data = pd.read_json(data)
    sns.set_theme(style="whitegrid")
    sns.lmplot(x="time", y="priceUsd", data=panda_data, height=5, aspect=2 / 1, order=3, ci=None, scatter_kws={"s": 30})
    plt.savefig('pictures/polynomial_analysis.png')


if __name__ == '__main__':
    polynomial_analysis()

