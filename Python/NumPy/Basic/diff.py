# -*- coding: utf-8 -*-
import numpy as np

def main():

    y = [1., 2., 3., 4., 5., 5.5, 7., 9.]
    diff_y = np.diff(y)                     # yの差分を計算
    print("y="+str(y))                    # 結果を表示
    print("diff(y)="+str(diff_y))


if __name__ == '__main__':
    main()
