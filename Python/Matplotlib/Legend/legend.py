# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

def main():
    x = np.linspace(0,3,4)  # xの値域(0, 1, 2, 3)
    y1 = x + 1              # 直線1の式
    y2 = x                  # 直線2の式
    plt.plot(x,y1,"r-",label="l1")  # 直線1を引く(凡例の表記は「l1」)
    plt.plot(x,y2,"g-",label="l2")  # 直線2を引く(凡例の表記は「l2」)
    plt.legend(loc=2)               # 凡例の位置
    plt.show()                      # グラフ表示

if __name__ == '__main__':
    main()
