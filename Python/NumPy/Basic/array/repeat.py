# -*- coding: utf-8 -*-
import numpy as np

def main():
    # 配列の宣言・初期化
    A = np.repeat([1, 2, 3, 4], 3)
    B = np.array([1, 2, 3, 4]*3)
    # 画面出力
    print(A)
    print(B)

if __name__ == '__main__':
    main()
