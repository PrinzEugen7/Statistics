# -*- coding: utf-8 -*-
import numpy as np


def main():
    a = np.array([1.,2.,3.])    # ベクトルaの生成
    b = a / np.linalg.norm(a)   # ベクトルの正規化
    print(b)


if __name__ == '__main__':
    main()
