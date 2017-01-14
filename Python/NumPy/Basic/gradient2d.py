# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

def main():

    x = np.arange(0, 10.1, 0.5)
    y = np.arange(0, 10.1, 0.5)
    (xm, ym) = np.meshgrid(x, y)        # グリッドの作成
    (xq,yq) = (5, 5)                    # 電荷の座標
    r = np.sqrt((xq-xm)**2+(yq-ym)**2)  # 電荷との距離
    k = 9.0*10**9                       # 比例定数k
    q = 1                               # 電荷
    E = (k*q)/r**2                      # 2変数の関数(電場E(x,y)
    (Ey,Ex) = np.gradient(E ,.2, .2)    # Eの勾配を計算
    Ex[Ex>0.5],Ey[Ey>0.5] = 0.5, 0.5    # 勾配の上限下限
    Ex[Ex<-0.5],Ey[Ey<-0.5] = -0.5, -0.5
    # 結果を表示
    plt.quiver(xm,ym,-Ex,-Ey,angles="xy",headwidth=3,scale=20,color="#444444")
    plt.xlim([0, 10])
    plt.ylim([0, 10])
    plt.grid()
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
