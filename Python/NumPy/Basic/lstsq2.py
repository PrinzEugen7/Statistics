# -*- coding: utf-8 -*-
import numpy as np

# 偏回帰係数の計算
def stat(o, e):

    e = np.vstack([np.ones(e.shape[1]), e]) # 定数項, 説明変数
    return np.linalg.lstsq(e.T, o)[0]       # 偏回帰係数


def main():

    # 定量データ
    y = (45, 38, 41, 34, 59, 47, 35, 43, 54, 52)
    x1 = (17.5, 17.0, 18.5, 16.0, 19.0, 19.5, 16.0, 18.0, 19.0, 19.5)
    x2 = (30, 25, 20, 30, 45, 35, 25, 35, 35, 40)

    obj = np.array(y)        # 目的変数
    exp = np.array([x1, x2]) # 説明変数

    # 偏回帰係数の計算
    b, a1, a2 = stat(obj, exp)

    # 求めた係数を表示
    print("a1 = "+str(a1))
    print("a2 = "+str(a2))
    print("b = "+str(b))

if __name__ == '__main__':
    main()
