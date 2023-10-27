# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 10:12:43 2021

@author: Menings
"""

import matplotlib.pyplot as plt

def pp_font(ax, x_label_size=15, x_label='', y_label_size=True, y_label='',
            x_tick_size=15, y_tick_size=True,
            x_offsetText=15, y_offsetText=True,
            x_nbins=False, y_nbins=False):
    """Make the fonts of given ax readable in Powerpoint."""
    # determine each value
    if y_label_size is True:
        y_label_size = x_label_size

    if y_tick_size is True:
        y_tick_size = x_tick_size

    if y_offsetText is True:
        y_offsetText = x_offsetText

    if y_nbins is True:
        y_nbins = x_nbins

    # actual changes to ax
    if x_tick_size is not False:
        ax.set_xlabel(xlabel=x_label, fontsize=x_label_size)
    if y_tick_size is not False:
        ax.set_ylabel(ylabel=y_label, fontsize=y_label_size)

    if x_tick_size is not False:
        for label in ax.get_xticklabels():
            label.set_fontsize(x_tick_size)
    if y_tick_size is not False:
        for label in ax.get_yticklabels():
            label.set_fontsize(y_tick_size)

    if x_offsetText is not False:
        ax.xaxis.offsetText.set_fontsize(x_offsetText)
    if y_offsetText is not False:
        ax.yaxis.offsetText.set_fontsize(y_offsetText)

    if x_nbins is not False:
        ax.locator_params(axis='x', nbins=x_nbins)
    if y_nbins is not False:
        ax.locator_params(axis='y', nbins=y_nbins)
    return

# %% typical scientific layout


def science_layout(ax):
    """Make ticks on top and right and put all ticks inside."""
    ax.xaxis.set_ticks_position('both')
    ax.yaxis.set_ticks_position('both')
    ax.tick_params(direction='in')
    return