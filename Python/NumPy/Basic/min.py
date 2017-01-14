# -*- coding: utf-8 -*-
import numpy as np

def main():
    # データ
    data = np.array([31,30,27,25,29,34,32,31,30,29])
    min = np.amin(data)         # 最小値を計算
    print(u"最小値："+str(min))    # 結果を表示

if __name__ == '__main__':
    main()
