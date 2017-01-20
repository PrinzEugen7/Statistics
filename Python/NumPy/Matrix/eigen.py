# -*- coding: utf-8 -*-
import numpy as np


def main():
    A = np.array([[1.,0.]    # 行列Aの生成
                 ,[0.,2.]])

    la, v = np.linalg.eig(A)    # 行列Aの固有値・固有ベクトル
    print(u"固有値："+str(la))
    print(u"固有ベクトル："+str(v))

if __name__ == '__main__':
    main()
