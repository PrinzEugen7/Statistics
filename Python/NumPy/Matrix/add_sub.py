# -*- coding: utf-8 -*-
import numpy as np


def main():
    A = np.array([[1,0,0]   # 行列Aの生成
                 ,[0,1,0]
                 ,[0,0,1]])

    B = np.array([[2,0,0]   # 行列Bの生成
                 ,[0,2,0]
                 ,[0,0,2]])

    C = A + B               # 行列の和
    print(C)
    
    C = A - B               # 行列の差
    print(C)

if __name__ == '__main__':
    main()
