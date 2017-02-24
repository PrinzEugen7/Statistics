# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

def main():
    # 乱数を100個生成(x, y)
    x1 = np.random.randn(100)
    y1 = np.random.randn(100)
    x2 = np.random.randn(100)
    y2 = np.random.randn(100)
    # 散布図
    plt.scatter(x1,y1,c='#cc0000')
    plt.scatter(x2,y2,c='#00cc00')
    # 表示
    plt.grid()
    plt.show()

if __name__ == '__main__':
    main()
