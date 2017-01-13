# -*- coding: utf-8 -*-
import numpy as np

def main():
    # データ(気温)
    data = np.array([31,30,27,25,29,34,32,31,30,29])
    ave = np.average(data)      # 平均を計算
    print(u"平均："+str(ave))   # 結果を表示

if __name__ == '__main__':
    main()
