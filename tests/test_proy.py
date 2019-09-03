
# coding: utf-8

import sys
sys.path.insert(0,"../")
#print(sys.path)
import particle.particle as pt

#BEGINNIG-OG-EXECUTION
delta = 0.01
x0,y0,v0,a0 = 0., .5, 1., 45

ball = pt.particle("Ball",x0,y0,v0,a0)
print(ball)

# implement Euler with a = -g
# compare to algebraic solution
# x = x0 + v0x * t
# y = y0 + v0y * t + a * t**2/"

#END-OF-EXECUTIION


