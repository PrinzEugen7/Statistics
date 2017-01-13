# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

def main():

    A = np.array([[2.,0.]    # 行列Aの生成
                 ,[0.,5.]])
    L = np.linalg.cholesky(A)      # 行列AをQR分解
    # 結果を表示
    print("A=\n"+str(A))
    print("L=\n"+str(L))
    print("L*L^T=\n"+str(L.dot(L.T)))

if __name__ == '__main__':
    main()
