# -*- coding: utf-8 -*-
import numpy as np


def main():
    A = np.array([[1.,0.]               # 行列Aの生成
                 ,[0.,2.]])
    invA = np.linalg.inv(A)             # Aの逆行列
    print( "invA=\n" + str(invA) )      # 計算結果の表示

if __name__ == '__main__':
    main()
