# this is solution from wave motion from notes of mine from 29^th april 22 5^th page.

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('seaborn')
fig = plt.figure()
ax = fig.add_subplot(1,1,1)

# Data
L, b_m, T, rho = 1, -np.pi*0.5, 1000, 10
v = np.sqrt(T/rho)

# structure of wave by fourier decomposition of desired wave format
def C_m_struct(max_NM):
    c = []
    for i in range(max_NM):
        k = (2*i+1)/2*L
        co1 = ((2*np.pi)/L)-k
        co2 = ((2*np.pi)/L)+k
        cm = -(2/L)*((1/co1)*np.sin(co1*L/2)-(1/co2)*np.sin(co2*L/2))
        c.append(cm)
    return c
C_m = C_m_struct(100)           # It's funny but  wave speed depend on your processor, mine is to slow :(

# solution of wave equation with special boundary conditions where psi(0)=0 and d(psi(L))/dx=0
def psi(x,time,a):
    solution = 0
    for t,at in enumerate(a):
        term1 = np.sin(((v*(2*t+1)*np.pi*time)/2*L)+b_m)
        term2 = np.sin(((2*t+1)*np.pi*x)/2*L)
        solution+=at*term1*term2
    return solution
time_interval = np.arange(0,10,0.001)


def animation(i):
    w = []
    for x in np.arange(0,L,0.01):
        w.append(psi(x,i,C_m))
    ax.clear()
    ax.plot(np.arange(0,L,0.01),w)
    ax.set(xlim=(0,L),ylim=(-4,4))


live_plot = FuncAnimation(fig, func=animation, frames=time_interval, interval=60)
plt.show()
