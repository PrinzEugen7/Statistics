# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

def main():
    x = np.linspace(0,3,4)          # xの値域(0, 1, 2, 3)
    y = x + 1                       # 直線の式
    plt.plot(x,y,"ro",label="y")    # 直線を引く
    plt.legend(numpoints=1)         # 凡例(点1つ)
    plt.show()                      # グラフ表示

if __name__ == '__main__':
    main()
