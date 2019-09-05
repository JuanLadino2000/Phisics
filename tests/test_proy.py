# coding: utf-8

import sys
sys.path.insert(0,"../")
import particle as pt
import matplotlib.pyplot as plt
import numpy as np

GRAV = 1

def exact_sol(x0,y0,v0,a0,t):
    v0x = v0 * np.cos(np.radians(a0))
    v0y = v0 * np.sin(np.radians(a0))
    x = x0 + v0x*t
    y = y0 + v0y*t -1/2*GRAV*(t**2)
    return y

deltat = 0.1
m,t0,x0,y0,v0,a0 = 1.,0.,0.,0.,1.,45

ball = pt.Particle("Ball",x0,y0,v0,a0)

xpos,ypos,time = [],[],[]
xexact,yexact = [],[]


while y0 >= 0:
    x,y,vx,vy,t = ball.get_state()
    ypos.append(ball.y)
    time.append(ball.t)
    ball.step(deltat)

    #xpos.append(ball.x)


    #exacx.append(a)    #print("pos: ({},{})\n".format(ball.x,ball.y))
    #print("time: {}".format(ball.t))
    #print("-----------------------------------------------------")
    y0 = y

yexact = [exact_sol(x0,y0,v0,a0,t) for t in time]

fig, ax = plt.subplots()
ax.plot(time, ypos)
ax.plot(time, yexact)
ax.set(xlabel='time (s)', ylabel='voltage (mV)',
       title='About as simple as it gets, folks')
ax.grid()
plt.show()
