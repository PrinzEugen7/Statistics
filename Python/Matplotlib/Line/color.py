# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

def main():
    x = [1,2,3,4]                       # xの値
    y = [1,2,3,4]                       # yの値
    plt.plot(x,y,"-o",color="#ff0000")  # 直線を引く
    plt.show()                          # グラフ表示

if __name__ == '__main__':
    main()
