# -*- coding: utf-8 -*-
import numpy as np

def main():
    # 配列の宣言・初期化
    A = np.array([[1, 2],[3, 4]])
    B = np.array([[5, 6], [7, 8]])
    C = A * B
    # 画面出力
    print(C)

if __name__ == '__main__':
    main()
