# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

def main():
    x = [1, 2, 3, 4, 5]
    y = [4, 5, 6, 7, 8]

    plt.barh(x, y, align="center")           # 中央寄せで棒グラフ作成
    plt.yticks(x, ["A","B","C", "D", "E"])  # X軸のラベル
    plt.show()

if __name__ == '__main__':
    main()
