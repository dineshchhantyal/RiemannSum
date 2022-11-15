from enum import Enum
import functools

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
from matplotlib.patches import PathPatch, Rectangle




interval_x = []
fig, ax = plt.subplots()



RIEMANN_LEFT = "RIEMANN_LEFT"
RIEMANN_RIGHT = "RIEMANN_RIGHT"
RIEMANN_MIDDLE = "RIEMANN_MIDDLE"


class Riemaan:
    def __init__(self, y:str, a:int , b:int, n: int, method: str):
        self.equation = lambda x : x ** 2
        self.x = []
        self.y = y 
        self.LOWER_BOUND = a
        self.UPPER_BOUND = b
        self.n = n
        self.xn = []
        self.yn = []
        self.ans = 0
        self.dx = (b - a) / n
        self.NUMBER_OF_SECTION = 10
        self.METHOD = method
        self.calculate_x_y()
        self.draw_main_graph()
        self.find_xn_yn()
##        self.draw_sub_area()
        self.show_graph()
        self.evaluate_ans()
        
    def show_values(self):
        print("x", self.x)
        print("y", self.y)
        print("method", self.METHOD)
        print("a", self.LOWER_BOUND)
        print("b", self.UPPER_BOUND)
        print("xn", self.xn)
        print("yn", self.yn)
    
    def f(self, x):
        return self.equation(x)
    def calculate_x_y(self):
        self.x = np.linspace(self.LOWER_BOUND - 2 , self.UPPER_BOUND + 2, (self.UPPER_BOUND - self.LOWER_BOUND) * self.NUMBER_OF_SECTION)
        self.y = [self.f(x) for x in self.x]
    def find_xn_yn(self):
        self.xn = [self.LOWER_BOUND + i * self.dx for i in range(self.n + 1)]
        self.yn = [self.f(xs) for i, xs in enumerate(self.xn)]
        self.draw_interval()
        
    def riemann_left(self):
        Area = self.dx * (functools.reduce(lambda a, b: a+b, self.yn[:len(self.yn) - 1 ]))
        print("Using left rule")
        return Area
    def riemann_right(self):
        Area = self.dx * (functools.reduce(lambda a, b: a+b, self.yn[1:]))
        print("Using right rule")
        return Area
    
    def draw_main_graph(self):
        ax.plot(self.x, self.y, label = "Main plot")
    
    def draw_interval(self):
        for i, sub_interval in enumerate(self.xn):
            plt.axvline(x = sub_interval, color='lightgrey', linestyle='--' )
            plt.axhline(y = self.yn[i], color='lightgrey', linestyle='--')
    def draw_sub_area(self):
        if self.METHOD == RIEMANN_LEFT:
            print("I'm running")
            for i, x in enumerate(self.xn):
                if i == len(self.xn) - 1:
                    break;
                ax.add_patch(Rectangle((x, 0), self.dx, self.yn[i], color = "yellow"))
                ax.annotate(str(self.dx * self.yn[i]) + " sq. units" , (x, self.yn[i]))
        elif self.METHOD == RIEMANN_RIGHT:
            for i, x in enumerate(self.xn):
                if i == 0:
                    continue;
                ax.add_patch(Rectangle((x, 0), self.dx, self.yn[i], color = "yellow"))
                ax.annotate(str(self.dx * self.yn[i]) + " sq. units" , (x, self.yn[i]))
            
    def evaluate_ans(self):
        ans = 0
        if self.METHOD == RIEMANN_LEFT:
            ans = self.riemann_left()
        elif self.METHOD == RIEMANN_RIGHT:
            ans = self.riemann_right()
            
        print(f"Area using {self.METHOD} is ", ans)
        
    def show_graph(self):
        plt.show()


new = Riemaan("x**2", 1, 5, 99999
             , RIEMANN_LEFT)

