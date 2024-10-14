import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import matplotlib.animation as animation

import setting as s
from pendrum import list_utils as lu
from pendrum import calculation as calc

# Listの数と系の状態が整合しているか？
result = lu.is_list(s.M, s.L)
if (result == False): exit()
result = lu.check_lists_length(s.PARTICLE_NUMBER, s.M, s.L)
if (result == False): exit()

# 計算部分
t = np.arange(s.MIN_TIME, s.MAX_TIME, s.DELTA_TIME)
y = integrate.odeint(s.derivs, s.INIT_CONDITIN, t) 

# 座標を与える
x_i, y_i = calc.give_xy_coordinate(s.L, y)

# 描画
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
    thisx = [0, x_i[0][i], x_i[1][i]] 
    thisy = [0, y_i[0][i], y_i[1][i]] 
    line.set_data(thisx, thisy) 
    time_text.set_text(time_template % (i*s.DELTA_TIME)) 
    return line, time_text 

line, time_text = animate(0)
print(f'{line}, {time_text}')
exit()
ani = animation.FuncAnimation(fig, animate, np.arange(1, len(y)), interval=25, blit=True, init_func=init) 
plt.show()