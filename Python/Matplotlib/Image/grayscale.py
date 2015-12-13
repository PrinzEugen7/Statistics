# -*- coding: utf-8 -*-
import cv2
import matplotlib.pyplot as plt

def main():
    gray = cv2.imread("test.jpg",0) # 画像の取得
    plt.imshow(th)              # 画像貼り付け
    plt.grid()
    plt.gray()
    plt.show()                  # グラフ表示

if __name__ == '__main__':
    main()
