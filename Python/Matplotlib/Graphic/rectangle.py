# -*- coding: utf-8 -*-
import matplotlib
import matplotlib.pyplot as plt

def main():
    fig = plt.figure()
    ax = fig.add_subplot(111)
    # 始点(0.2,0.2)で幅が0.2, 高さが0.4の長方形を描画
    rect = plt.Rectangle((0.2,0.2),0.2,0.4,fc="#770000")
    ax.add_patch(rect)
    plt.show()

if __name__ == '__main__':
    main()
