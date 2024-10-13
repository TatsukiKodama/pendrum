import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import matplotlib.animation as animation

import setting as s
from pendrum import list_utils as lu


# 時間ステップと時間
dt = 0.01
t = np.arange(0.0, 20, dt)

# 微分方程式を解く
initial_condition: list = lu.combine(s.INIT_ANGLE, s.INIT_ANGULER_VELOCITY)
y = np.radians(initial_condition) 
y = integrate.odeint(s.derivs, y, t) 

######################### 描画 #########################

# 座標
x1 = s.L[0]*np.sin(y[:, 0]) 
y1 = -s.L[0]*np.cos(y[:, 0]) 
x2 = s.L[1]*np.sin(y[:, 2]) + x1
y2 = -s.L[1]*np.cos(y[:, 2]) + y1 

# figインスタンスを生成
fig = plt.figure() 
ax = fig.add_subplot(111, autoscale_on=False, xlim=(-2, 2), ylim=(-2, 2)) 
ax.set_aspect('equal') 
ax.grid() 
line, = ax.plot([], [], 'o-', lw=2) 
time_template = 'time = %.1fs' 
time_text = ax.text(0.05, 0.9,'', transform=ax.transAxes) 
def init(): 
    line.set_data([], []) #　これもタイマー用の初期化 
    time_text.set_text('') 
    return line, time_text 

def animate(i): 
    thisx = [0, x1[i], x2[i]] 
    thisy = [0, y1[i], y2[i]] 
    line.set_data(thisx, thisy) 
    time_text.set_text(time_template % (i*dt)) 
    return line, time_text 

ani = animation.FuncAnimation(fig, animate, np.arange(1, len(y)), interval=25, blit=True, init_func=init) 
plt.show()