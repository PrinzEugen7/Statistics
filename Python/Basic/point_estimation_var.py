# -*- coding: utf-8 -*-
import numpy as np

def main():
    # 母集団の生成
    data = np.random.rand(50)
    # 母分散の点推定
    var = np.ndarray([])                        # 不偏分散を格納する配列
    # 点推定(100回繰り返し)
    for i in range(100):
        x = np.random.choice(data,5)            # 母集団からサイズ5の標本を抽出
        var = np.append(var, np.var(x, ddof=1)) # 不偏分散を計算して配列に格納

    sigma = np.average(var)                     # 100個の不偏分散の平均値:母集団の推定分散値
    # 結果を表示
    print u"点推定で求めた母分散:",sigma
    print u"実際の母分散:",np.var(data, ddof=1)

if __name__ == '__main__':
    main()
