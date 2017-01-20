# -*- coding: utf-8 -*-
import numpy as np


def main():
    a = np.array([1.,2.,3.])    # ベクトルaの生成
    al = np.linalg.norm(a)      # ベクトルの長さ(ノルム)を計算
    print(al)


if __name__ == '__main__':
    main()
