# -*- coding: utf-8 -*-
import numpy as np

def main():
    # データ
    data = np.array([31,30,27,25,29,34,32,31,30,29]) 
    mean = np.mean(data)              # 算術平均を計算
    print(u"算術平均："+str(mean))    # 結果を表示

if __name__ == '__main__':
    main()
