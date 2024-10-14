'''
設定ファイル
（まだ２質点のみ）
'''

import numpy as np
from pendrum import phys_const as pc
from pendrum import math_const as mc
from pendrum import list_utils as lu

g: float = pc.GRAVITATIONAL_ACCELERATION
pi: float = mc.PI

# ===== 設定パラメタ===== #

# 粒子数
PARTICLE_NUMBER: int = 2

# 質量のリスト
M: list = [1.0, 1.0]

# 振り子の腕の長さのリスト
L: list = [1.0, 1.0]

# 振り子の角度の初期条件
INIT_ANGLE: list = [pi/12, -pi/12]

# 振り子の角速度の初期条件
INIT_ANGULER_VELOCITY: list = [0,  0]

# 時間の設定
MAX_TIME = 20
MIN_TIME = 0.0
DELTA_TIME = 0.05
INIT_CONDITIN: list = lu.combine(INIT_ANGLE, INIT_ANGULER_VELOCITY)

# ===== 微分方程式 =====
def derivs(y: list, t: float) -> list:
    dydx = np.zeros_like(y) # 0.に初期化
    Mtot = sum(M) # 全質量
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