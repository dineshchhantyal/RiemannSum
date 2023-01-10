from enum import Enum
import functools

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import  Rectangle




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
        self.mid_points = []
        self.calculate_x_y()
        self.draw_main_graph()
        self.find_xn_yn()
        self.draw_sub_area()
        self.show_graph()
        self.evaluate_ans()
        
    def show_values(self):
        print({
            "x": self.x,
            "y": self.y,
            "xn": self.xn,
            "yn": self.yn,
            "dx": self.dx,
            "n": self.n,
            "a": self.LOWER_BOUND,
            'b': self.UPPER_BOUND,
            'mid_points': self.mid_points,
            "method": self.METHOD,
            "ans": self.ans,
            "equation": self.equation,
            "number_of_section": self.NUMBER_OF_SECTION
        })
           
    def f(self, x):
        return self.equation(x)
    def calculate_x_y(self):
        self.x = np.linspace(self.LOWER_BOUND - 2 , self.UPPER_BOUND + 2, (self.UPPER_BOUND - self.LOWER_BOUND) * self.NUMBER_OF_SECTION)
        self.y = [self.f(x) for x in self.x]
    def find_xn_yn(self):
        self.xn = [self.LOWER_BOUND + i * self.dx for i in range(self.n + 1)]
        self.yn = [self.f(xs) for xs in self.xn]
        self.draw_interval()
        
    def riemann_left(self):
        Area = self.dx * functools.reduce(lambda a, b: a+b, self.yn[:-1])
        print("Using left rule")
        return Area
    def riemann_right(self):
        Area = self.dx * (functools.reduce(lambda a, b: a+b, self.yn[1:]))
        print("Using right rule")
        return Area
    
    def riemann_middle(self):
        self.mid_points = [(self.xn[i] + self.xn[i + 1]) / 2 for i in range(len(self.xn) - 1)]
        Area = self.dx * (functools.reduce(lambda a, b: a+b, [self.f(x) for x in self.mid_points]))
        print("Using middle rule")
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
                ax.annotate(str(round(self.dx * self.yn[i])), (x, self.yn[i]))
        elif self.METHOD == RIEMANN_RIGHT:
            for i, x in enumerate(self.xn):
                if i == 0:
                    continue;
                ax.add_patch(Rectangle((x, 0), - self.dx, self.yn[i], color = "yellow"))
                ax.annotate(str(round(self.dx * self.yn[i])), (x, self.yn[i]))
        else:
            for i, x in enumerate(self.mid_points):
                ax.add_patch(Rectangle((self.xn[i], 0), self.dx, self.f(x), color = "yellow"))
                ax.annotate(str(round(self.dx * self.f(x))), (x, self.f(x)))
            
    def evaluate_ans(self):
        ans = 0
        if self.METHOD == RIEMANN_LEFT:
            ans = self.riemann_left()
        elif self.METHOD == RIEMANN_RIGHT:
            ans = self.riemann_right()
        else:
            ans = self.riemann_middle()
            
        print(f"Area using {self.METHOD} is ", ans)
        
    def show_graph(self):
        plt.show()


new = Riemaan("x**2", 1, 5, 4
             , RIEMANN_LEFT)

