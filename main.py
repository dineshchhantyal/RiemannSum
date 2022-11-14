from enum import Enum

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
from matplotlib.patches import PathPatch

LOWER_BOUND = 0
UPPER_BOUND = 100

interval_x = []
fig, ax = plt.subplots()


def draw_main_graph():

    N = 100
    x = np.linspace(LOWER_BOUND, UPPER_BOUND, N)
    x, y = x, [2 * domain ** 2 + 2 for domain in x]


    ax.plot(x, y, label = "Main plot")

def draw_interval(n = 5):
    interval_x = np.linspace(LOWER_BOUND, UPPER_BOUND, n)
    for sub_interval in interval_x:
        plt.axvline(x = sub_interval, color='lightgrey', linestyle='--' )
        plt.axhline(y=- sub_interval ** 2, color='lightgrey', linestyle='--')
    
draw_main_graph()
draw_interval()
plt.show()


class Methods(Enum):
    RIEMANN_LEFT = "RIEMANN_LEFT"
    RIEMANN_RIGHT = "RIEMANN_RIGHT"
    RIEMANN_MIDDLE = "RIEMANN_MIDDLE"


class Riemaan:
    def __init__(self, y:str, a:int , b:int, n: int, method: str):
        self.equation = y
        self.x = []
        self.y = y 
        self.a = a
        self.b = b
        self.n = n
        self.xn = []
        self.yn = []
        self.ans = 0
        self.dx = (b - a) / n
        self.calculate_x_y()
        
    def show_values(self):
        print("x", self.x)
        print("y", self.y)
        print("a", self.a)
        print("b", self.b)
        print(self)
    def f(self, x):
        return eval(self.equation)
    def calculate_x_y(self):
        self.x = [1,2,3]
        self.y = [2,3,4]
    def find_xn_yn(self):
        self.xn = [xs + i * self.dx for i, xs in enumerate(self.x)]
        #self.yn = [ys + i * self.dy for i, ys in enumerate(self.y)]
    def riemann_left(self):
        # xn = [xs + DX  for xs in x]
        print("Using left rule")
    



new = Riemaan("x**2", 1, 5, 2, Methods.RIEMANN_LEFT)
new.show_values()
new.find_xn_yn()
new.show_values()