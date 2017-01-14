# -*- coding: utf-8 -*-
import numpy as np

def main():
    # データ
    data = np.array([31,30,27,25,29,34,32,31,30,29])
    median = np.median(data)        # 中央値を計算
    print(u"中央値："+str(median))  # 表示

if __name__ == '__main__':
    main()
