# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

def main():

    x = np.arange(-3.14, 3.14, 0.25)        # xの値を生成
    sin = np.sin(x)                         # sin(x)の計算
    plt.plot(x, sin, "r-",lw=2, alpha=0.7)  # グラフ表示
    plt.grid()                              # グリッドの表示
    plt.show()                              # グラフの描画


if __name__ == '__main__':
    main()
