import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
from scipy.optimize import curve_fit
import os
import datetime
from app.pp_font import science_layout, pp_font

def plot_data(x, y, fig, ax):
    "Plot x and y data in a nice format"
    ax.scatter(x, y, label='data', color='black', marker='x')
    pass

def linear_fit(x, y, fig, ax):
    "Make a linear fit and plot the result into the given axes."
    popt, pcov = curve_fit(linear, x, y)
    ax.plot(x, np.array(linear(x, popt[0], popt[1])), label='linear fit', color='blue')
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

def save(fig, savepath):
    "Check if save path exist, if not create it, and finally save the fig there."
    n=savepath[::-1].find('\\')  # find last occurence of '\'
    savefolder = savepath[:len(savepath)-n]
    if not os.path.exists(savefolder):
        os.mkdir(savefolder)
    fig.tight_layout()
    fig.savefig(savepath)

def plot_and_fit(x, y, savepath):
    fig, ax = plt.subplots()
    plot_data(x, y, fig, ax)
    popt, pcov = linear_fit(x=mdates.date2num(x), y=y, fig=fig, ax=ax)
    ax.legend()
    make_date_label(fig, ax)
    science_layout(ax)
    pp_font(ax, x_label='Datum', y_label='Gewicht [kg]')
    save(fig=fig, savepath=savepath)
    return round(popt[0]*7, 3)


def test():
    fig, ax = plt.subplots()
    x = np.array([datetime.date(2023, 2, 7), datetime.date(2023, 6, 5), datetime.date(2023, 9, 30)])
    y = np.array([80., 65., 40.])
    plot_data(x, y, fig, ax)
    make_date_label(fig, ax)
    linear_fit(x=mdates.date2num(x), y=y, fig=fig, ax=ax)
    fig.savefig("test.png")

def savetest():
    fig, ax = plt.subplots()
    save(fig, savepath=r'C:\Users\Benja\Code\Python\Webside - Fitness\app\static\images\test\savetest.png')

