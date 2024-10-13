'''
設定ファイル
（まだ２質点のみ）
'''

import numpy as np
from pendrum import physical_const as pc

g = pc.GRAVITATIONAL_ACCELERATION

# parameters
M = [1.0, 1.0]
L = [1.0, 1.0]
INIT_ANGLE = [120, -10]
INIT_ANGULER_VELOCITY = [0, 0]

# 微分方程式
def derivs(y: list, t: float):
    dydx = np.zeros_like(y) # 0.に初期化
    Mtot = M[0] + M[1]
    del_theta = y[0] - y[2]
    A = np.array([[Mtot*L[0]**2, M[1]*L[0]*L[1]*np.cos(del_theta)], 
                    [M[1]*L[0]*L[1]*np.cos(del_theta), M[1]*L[1]**2]])
    v = np.array([-M[1]*L[0]*L[1]*dydx[2]**2*np.sin(del_theta) - Mtot*g*L[0]*np.sin(y[0]), 
                    M[1]*L[0]*L[1]*dydx[0]**2*np.sin(del_theta) - M[1]*g*L[1]*np.sin(y[2])])
    lhs = np.linalg.inv(A) @ v

    dydx[0] = y[1] # dot{theta1}
    dydx[1] = lhs[0] # ddot{theta1}
    dydx[2] = y[3] # dot{theta2}
    dydx[3] = lhs[1] # dot{theta2}

    return dydx