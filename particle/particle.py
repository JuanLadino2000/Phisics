
# coding: utf-8


import numpy as np
class particle:
    def __init__(self,name,x0,y0,v0,alpha0,m0=1,t0=0.):
        self.label = name
        self.m = m0
        self.t = t0
        self.x = x0
        self.y = y0
        self.vx = v0 * np.cos(np.radians(alpha0))
        self.vy = v0 * np.sin(np.radians(alpha0))
    def __str__(self):
        strng = self.label + "\n"
        strng += "m = {}, t = {}\n".format(self.m,self.t)
        strng += "r = ({:.4f},{:.4f})\n".format(self.x, self.y)
        strng += "v = ({:.4f},{:.4f})\n".format(self.vx,self.vy)
        return strng

    

