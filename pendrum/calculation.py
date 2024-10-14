import numpy as np
def give_xy_coordinate(L: list, y: any):
    '''
    N重振り子について、それぞれの質点の角度を座標に置き換える関数
    注意）汎用的な関数ではない

    引数）
    L: 腕の長さのリスト
    y: 角度のリスト（numpyで微分方程式を解いているのでyの列に注意）
    '''
    # それぞれの粒子に対して座標を初期化
    x_i = list(np.zeros(len(L)))
    y_i = list(np.zeros(len(L)))

    x_i[0] = L[0]*np.sin(y[:, 0])
    y_i[0] = -L[0]*np.cos(y[:, 0])
    for i in range(1, len(L)):
        x_i[i] = L[i]*np.sin(y[:, 2*i]) + x_i[i-1]
        y_i[i] = -L[i]*np.cos(y[:, 2*i]) + y_i[i-1]
    return x_i, y_i