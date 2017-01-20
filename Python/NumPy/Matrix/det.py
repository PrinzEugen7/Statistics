# -*- coding: utf-8 -*-
import numpy as np


def main():
    A = np.array([[2.,1.,1.]    # 行列Aの生成
                 ,[1.,2.,1.]
                 ,[1.,1.,1.]])

    detA = np.linalg.det(A)     # 行列式の計算
    print(detA)


if __name__ == '__main__':
    main()
