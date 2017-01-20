# -*- coding: utf-8 -*-
import matplotlib
import matplotlib.pyplot as plt

def main():
    fig = plt.figure()
    ax = fig.add_subplot(111)
    # 5点(0.1,0.1),(0.1,0.6),(0.7,0.8),(0.6,0.4),(0.6,0.1)を通る多角形を描画
    poly = plt.Polygon(((0.1,0.1),(0.1,0.6),(0.7,0.8),(0.6,0.4),(0.6,0.1)),fc="#770000")
    ax.add_patch(poly)
    plt.show()

if __name__ == '__main__':
    main()
