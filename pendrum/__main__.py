from numpy import sin, cos
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import matplotlib.animation as animation

from pendrum import physical_const as pc

L1 = 1.0  # length of pendulum 1 in m
L2 = 1.0  # length of pendulum 2 in m
M1 = 1.0  # mass of pendulum 1 in kg
M2 = 1.0  # mass of pendulum 2 in kg


def derivs(y, t):
    g = pc.GRAVITATIONAL_ACCELERATION
    dydx = np.zeros_like(y)
    dydx[0] = y[1]

    del_ = y[2] - y[0]
    den1 = (M1 + M2)*L1 - M2*L1*cos(del_)*cos(del_)
    dydx[1] = (M2*L1*y[1]*y[1]*sin(del_)*cos(del_) +
               M2*g*sin(y[2])*cos(del_) +
               M2*L2*y[3]*y[3]*sin(del_) -
               (M1 + M2)*g*sin(y[0]))/den1

    dydx[2] = y[3]

    den2 = (L2/L1)*den1
    dydx[3] = (-M2*L2*y[3]*y[3]*sin(del_)*cos(del_) +
               (M1 + M2)*g*sin(y[0])*cos(del_) -
               (M1 + M2)*L1*y[1]*y[1]*sin(del_) -
               (M1 + M2)*g*sin(y[2]))/den2

    return dydx

# create a time array from 0..100 sampled at 0.05 second steps
dt = 0.05
t = np.arange(0.0, 20, dt)

# th1 and t
# w10 and w20 are the initial angular velocities (degrees per second) 
th1 = 120.0 
w1 = 0.0
th2 = -10.0
w2 = 0.0 # initial y 
y = np.radians([th1, w1, th2, w2]) 
# integrate your ODE using SciPy.integrate. 
y = integrate.odeint(derivs, y, t) 






x1 = L1*sin(y[:, 0]) # リストの0番目、θ１を取り出しています。 
y1 = -L1*cos(y[:, 0]) 
x2 = L2*sin(y[:, 2]) + x1# リストの2番目、θ2を取り出しています。 
y2 = -L2*cos(y[:, 2]) + y1 
fig = plt.figure() 
ax = fig.add_subplot(111, autoscale_on=False, xlim=(-2, 2), ylim=(-2, 2)) 
ax.set_aspect('equal') 
ax.grid() 
line, = ax.plot([], [], 'o-', lw=2) # タイマーを表示するために追加されました 
time_template = 'time = %.1fs' 
time_text = ax.text(0.05, 0.9,'', transform=ax.transAxes) 
def init(): 
    line.set_data([], []) #　これもタイマー用の初期化 
    time_text.set_text('') 
    return line, time_text 

def animate(i): 
    thisx = [0, x1[i], x2[i]] 
    thisy = [0, y1[i], y2[i]] 
    line.set_data(thisx, thisy) # タイマー更新用 
    time_text.set_text(time_template % (i*dt)) 
    return line, time_text 

ani = animation.FuncAnimation(fig, animate, np.arange(1, len(y)), interval=25, blit=True, init_func=init) 
plt.show()