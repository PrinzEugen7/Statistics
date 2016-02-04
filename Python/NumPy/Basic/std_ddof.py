# -*- coding: utf-8 -*-
import numpy as np

def main():

    data = np.array([31,30,27,25,29,34,32,31,30,29])    # データ
    std = np.std(data, ddof=1)              # 不偏標準偏差を計算
    print(std)   # 結果を表示

if __name__ == '__main__':
    main()
