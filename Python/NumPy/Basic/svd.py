# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

def main():

    A = np.random.rand(2, 2)    # 2*2の行列Aを生成
    U, S, V = np.linalg.svd(A)  # 行列Aを特異値分解
    # 結果を表示
    print("U=\n"+str(U))
    print("S=\n"+str(S))
    print("V=\n"+str(V))

if __name__ == '__main__':
    main()
