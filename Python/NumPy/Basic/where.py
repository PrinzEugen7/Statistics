# -*- coding: utf-8 -*-
import numpy as np

def main():

    y = np.array([8,9,10,11,15,18,22,21,20,29])    # データ(気温)
    y2 = y[ np.where((y>=10)&(y<20)) ]
    # 結果を表示
    print(u"10以上20未満のデータは："+str(y2))


if __name__ == '__main__':
    main()
