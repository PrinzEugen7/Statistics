# -*- coding: utf-8 -*-
import numpy as np

def main():
    # 配列の宣言・初期化
    A = np.array([[1, 2]])
    B = np.array([[3, 4], [5, 6]])
    C = np.vstack([A, B])
    # 画面出力
    print(C)

if __name__ == '__main__':
    main()
