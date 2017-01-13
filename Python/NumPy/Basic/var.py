# -*- coding: utf-8 -*-
import numpy as np

def main():
    # データ(気温)
    data = np.array([31,30,27,25,29,34,32,31,30,29])
    var = np.var(data)          # 分散を計算
    print(u"分散："+str(var))   # 結果を表示

if __name__ == '__main__':
    main()
