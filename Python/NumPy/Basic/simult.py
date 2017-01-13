# -*- coding: utf-8 -*-
import numpy as np


def main():

    A = np.array([[1.,3.]    # 行列Aの生成
                 ,[4.,2.]])
    B = np.array([1.,1.])   # 行列Bの生成

    X = np.linalg.solve(A, B)
    # 計算結果の表示
    print( "X=\n" + str(X) )


if __name__ == '__main__':
    main()
