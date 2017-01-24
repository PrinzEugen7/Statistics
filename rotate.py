# -*- coding: utf-8 -*-
import numpy as np

def rotate_x(deg):
    # degreeをradianに変換
    r = np.radians(deg)
    C = np.cos(r)
    S = np.sin(r)
    # x軸周りの回転行列
    R_x = np.matrix((
        (1, 0, 0),
        (0, C, -S),
        (0, S, C)
    ))

    return R_x


def main():
    # 元の行列
    a = np.array((1,1,0))
    # 回転行列の生成
    Rx = rotate_x(90)
    # 回転後のベクトルを計算
    b = np.dot(Rx,a)
    # 整数型に変換
    b = np.array(b,dtype=np.uint8)
    print("a=" + str(a))
    print("R=" + str(Rx))
    print("b=" + str(b[0]))


if __name__ == '__main__':
    main()
