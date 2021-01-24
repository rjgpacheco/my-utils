import datetime
import sys
from datetime import datetime
from io import StringIO
from pathlib import Path

import matplotlib
import matplotlib.ticker as mtick
import numpy as np
import pandas as pd
import pytz
import seaborn as sns
from matplotlib import pyplot as plt
from matplotlib.ticker import FuncFormatter

plt.style.use("fivethirtyeight")
#  _ = plt.box(False)

norm = lambda X: [x / sum(X) for x in X]

#  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Default colors
#  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
COLOR_PLOT_FACECOLOR = "#FFFFFF"
COLOR_LEGEND_FACECOLOR = "#F4F2F0"

DEFAULT_HEIGHT = 9
DEFAULT_WIDTH = DEFAULT_HEIGHT * 16 / 9
DEFAULT_DPI = 96 * 3
TITLE_PAD = 65
DEFAULT_PLOT_ARGS = {"linewidth": 2}

#  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#  Axis formatters
#  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
def millions(x, pos):
    "The two args are the value and tick position"
    return "%1.0f" % (x * 1e-6)


def billions(x, pos):
    "The two args are the value and tick position"
    return "%1.0f" % (x * 1e-9)


def trillions(x, pos):
    "The two args are the value and tick position"
    return "%1.0f" % (x * 1e-12)


#  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Figure Manipulaton
#  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
def format_ax(ax):
    ax.spines["bottom"].set_color(COLOR_PLOT_FACECOLOR)
    ax.spines["top"].set_color(COLOR_PLOT_FACECOLOR)
    ax.spines["right"].set_color(COLOR_PLOT_FACECOLOR)
    ax.spines["left"].set_color(COLOR_PLOT_FACECOLOR)
    ax.set_facecolor(COLOR_PLOT_FACECOLOR)
    return ax


def figure_initialization_(dpi=DEFAULT_DPI, h=DEFAULT_HEIGHT, w=DEFAULT_WIDTH, **kwargs):
    args = {
        "dpi": dpi,
        "figsize": (w, h),
        "facecolor": COLOR_PLOT_FACECOLOR,
        "edgecolor": COLOR_PLOT_FACECOLOR,
        "frameon": True,
    }

    fig, ax = plt.subplots(**args, **kwargs)
    ax.spines["bottom"].set_color(COLOR_PLOT_FACECOLOR)
    ax.spines["top"].set_color(COLOR_PLOT_FACECOLOR)
    ax.spines["right"].set_color(COLOR_PLOT_FACECOLOR)
    ax.spines["left"].set_color(COLOR_PLOT_FACECOLOR)

    return fig, ax


def set_legend(ax, loc="upper center", ncol=9, bbox_to_anchor=(0.5, 1.10), **kwargs):
    ax.legend(
        loc=loc,
        ncol=ncol,
        bbox_to_anchor=bbox_to_anchor,
        facecolor=COLOR_LEGEND_FACECOLOR,
        **kwargs
    )


def save_fig(fig, filepath):
    fig.savefig(
        filepath,
        format=format,
        bbox_inches="tight",
        facecolor=COLOR_PLOT_FACECOLOR,
        edgecolor=COLOR_PLOT_FACECOLOR,
        dpi=fig.dpi,
    )
    return None
