# a function that returns a dict of five number summary of given dataset: min, max, Q1, Q2, Q3

import numpy as np
from matplotlib import pyplot as plt


def five_num_summary(dataset):
    return {
        "min": np.min(dataset),
        "max": np.max(dataset),
        "Q1": np.quantile(dataset, 0.25),
        "Q2": np.quantile(dataset, 0.5),
        "Q3": np.quantile(dataset, 0.75)
    }


# a function that plots five number summary of given dataset on a histogram: min, max, Q1, Q2, Q3
def plot_five_num_summary(dataset, num_bins):
    plt.hist(dataset, bins=num_bins)
    plt.axvline(five_num_summary(dataset)["min"], label="min", c='#218380')
    plt.axvline(five_num_summary(dataset)["max"], label="max", c='#342E37')
    plt.axvline(five_num_summary(dataset)["Q1"], label="Q1", c='#FBB13C')
    plt.axvline(five_num_summary(dataset)["Q2"], label="Q2", c='#D90429')
    plt.axvline(five_num_summary(dataset)["Q3"], label="Q3", c='#540D6E')
    plt.legend()
    plt.show()