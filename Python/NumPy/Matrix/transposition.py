# -*- coding: utf-8 -*-
import numpy as np

def main():
    A = np.array([[1.,2.]   # 行列Aの生成
                 ,[3.,4.]])
    B = A.T                 # 行列Aの転置
    print(B)

if __name__ == '__main__':
    main()
