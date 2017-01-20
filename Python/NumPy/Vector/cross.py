# -*- coding: utf-8 -*-
import numpy as np


def main():
    a = np.array([1.,2.,3.])    # ベクトルaの生成
    b = np.array([4.,5.,6.])    # ベクトルbの生成
    c = np.cross(a,b)           # ベクトルaとbの内積
    print(c)


if __name__ == '__main__':
    main()
