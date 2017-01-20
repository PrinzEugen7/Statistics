# -*- coding: utf-8 -*-
import numpy as np


def main():
    A = np.array([[1.,0.,0.]            # 行列Aの生成
                 ,[0.,1.,1.]
                 ,[0.,1.,1.]])

    rankA = np.linalg.matrix_rank(A)    # 行列AのRank(階数)を計算
    print(rankA)


if __name__ == '__main__':
    main()
