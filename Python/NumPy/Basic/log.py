# -*- coding: utf-8 -*-
import numpy as np

def main():
    # xの値を生成(-3.14～3.14　0.25刻み)
    x = np.arange(-3.14, 3.14, 0.25)
    # 関数計算
    y = np.log(x)
    # 結果表示
    print(y)

if __name__ == '__main__':
    main()
