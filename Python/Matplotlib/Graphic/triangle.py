# -*- coding: utf-8 -*-
import matplotlib
import matplotlib.pyplot as plt

def main():
    fig = plt.figure()
    ax = fig.add_subplot(111)
    # 3点(0.1,0.1),(0.1,0.6),(0.6,0.1)を通る三角形を描画
    tri = plt.Polygon(((0.1,0.1),(0.1,0.6),(0.6,0.1)),fc="#770000")
    ax.add_patch(tri)
    plt.show()

if __name__ == '__main__':
    main()
