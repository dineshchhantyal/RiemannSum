import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
from matplotlib.patches import PathPatch

LOWER_BOUND = 0
UPPER_BOUND = 100

interval_x = []
fig, ax = plt.subplots()

def draw_main_graph():

    N = 900
    x = np.linspace(LOWER_BOUND, UPPER_BOUND, N)
    x, y = x, -x**2


    ax.plot(x, y, label = "Main plot")

def draw_interval(n = 4):
    interval_x = np.linspace(LOWER_BOUND, UPPER_BOUND, n)
    for sub_interval in interval_x:
        plt.axvline(x = sub_interval, color='lightgrey', linestyle='--' )
        plt.axhline(y=- sub_interval ** 2, color='lightgrey', linestyle='--')
    
draw_main_graph()
draw_interval()
plt.show()
