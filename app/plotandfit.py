import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
from scipy.optimize import curve_fit
import os
import datetime

def plot_data(x, y, fig, ax):
    "Plot x and y data in a nice format"
    ax.scatter(x, y, label='data', color='blue')
    pass

def linear_fit(x, y, fig, ax):
    "Make a linear fit and plot the result into the given axes."
    popt, pcov = curve_fit(linear, x, y)
    ax.plot(x, np.array(linear(x, popt[0], popt[1])), label='linear fit', color='red')
    return popt, np.sqrt(np.diag(pcov))

def make_date_label(fig, ax):
    "Make the label for a date-axis"
    #ax.xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
    #ax.xaxis.set_major_locator(mdates.DayLocator())
    #fig.autofmt_xdate()
    for label in ax.get_xticklabels():
        label.set_rotation(30)
    pass

def linear(x, a, b):
    return a*x + b

def test():
    fig, ax = plt.subplots()
    x = np.array([datetime.date(2023, 2, 7), datetime.date(2023, 6, 5), datetime.date(2023, 9, 30)])
    y = np.array([80., 65., 40.])

    plot_data(x, y, fig, ax)
    make_date_label(fig, ax)
    linear_fit(x=mdates.date2num(x), y=y, fig=fig, ax=ax)

    fig.savefig("test.png")