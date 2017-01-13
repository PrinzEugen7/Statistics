# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

def main():

    A = np.random.rand(2, 2)    # 2*2の行列Aを生成
    Q, R = np.linalg.qr(A)      # 行列AをQR分解
    # 結果を表示
    print("A=\n"+str(A))
    print("Q=\n"+str(Q))
    print("R=\n"+str(R))
    print("Q*R=\n"+str(Q.dot(R)))

if __name__ == '__main__':
    main()
