# -*- coding: utf-8 -*-
import numpy as np

def main():
    # 配列の宣言・初期化
    A = np.array([[1, 2],[3, 4]])
    B = A.astype('float64')
    # 画面出力
    print(B.dtype)

if __name__ == '__main__':
    main()
