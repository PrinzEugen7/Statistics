# -*- coding: utf-8 -*-
import matplotlib
import matplotlib.pyplot as plt

def main():
    fig = plt.figure()
    ax = fig.add_subplot(111)
    # 中心(0.2,0.2)で半径0.2の円を描画
    circle = plt.Circle((0.2,0.2),0.2,fc="#770000")
    ax.add_patch(circle)
    plt.show()

if __name__ == '__main__':
    main()
