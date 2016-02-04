# -*- coding: utf-8 -*-
import numpy as np

def main():
    # 10人分の得点
    x = np.array([71,72,85,85,78,92,74,82,84,79])
    # 10人分の偏差値を計算
    ans = np.round_(50+10*(x-np.average(x))/np.std(x))
    # 10人分の偏差値を表示
    print(ans)

if __name__ == '__main__':
    main()
