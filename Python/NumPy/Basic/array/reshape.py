# -*- coding: utf-8 -*-
import numpy as np

def main():
    # 1次元配列の宣言・初期化
    x = np.array([1, 2, 3, 4, 5, 6])
    # 配列の次元を変更(行数2, 列数3の2次元配列に変換)
    X = x.reshape(2, 3)
    # 画面出力
    print(X)

if __name__ == '__main__':
    main()
