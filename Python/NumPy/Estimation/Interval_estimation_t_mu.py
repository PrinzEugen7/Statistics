# -*- coding: utf-8 -*-
import numpy as np
from scipy import stats

def main():
    (mu, sigma) = (10, 1)           # 正規分布に従う母集団の平均10, 標準偏差1
    alpha = 0.95                    # 信頼係数95[%]
    ok = 0
    x = np.random.normal(mu, sigma, 50)     # 正規分布(mu, sigma)に従う正規分布からサイズ10の標本抽出
    n = len(x)                              # 標本サイズnの取得
    t = stats.t.ppf(1-(1-alpha)/2, n-1)     # t分布を用いて確率変数tを計算
    xa, sigma = np.average(x), np.std(x)    # 標本の平均と分散を計算
    t_min = xa - t * sigma / np.sqrt(n-1)
    t_max = xa + t * sigma / np.sqrt(n-1)
    print u"信頼区間の下限:",t_min
    print u"信頼区間の上限:",t_max

if __name__ == '__main__':
    main()
