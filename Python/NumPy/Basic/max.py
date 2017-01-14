# -*- coding: utf-8 -*-
import numpy as np

def main():
    # データ
    data = np.array([31,30,27,25,29,34,32,31,30,29])    
    max = np.amax(data)            # 最大値を計算
    print(u"最大値："+str(max))    # 結果を表示

if __name__ == '__main__':
    main()
