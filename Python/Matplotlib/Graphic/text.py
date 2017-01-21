# -*- coding: utf-8 -*-
import matplotlib
import matplotlib.pyplot as plt

def main():
    fig = plt.figure()
    ax = fig.add_subplot(111)
    # 長方形を2つ作成
    rect1 = matplotlib.patches.Rectangle((-1,1),0.5,0.5)
    rect2 = matplotlib.patches.Rectangle((1,2),0.5,0.5)
    ax.add_patch(rect1)
    ax.add_patch(rect2)
    # テキストを挿入
    plt.text(-1,1.6,"Rectangle1",fontsize=17)
    plt.text(1,2.6,"Rectangle2",fontsize=17)
    # グラフの設定
    plt.xlim([-3, 3])
    plt.ylim([0, 6])
    plt.grid()
    plt.show()

if __name__ == '__main__':
    main()
