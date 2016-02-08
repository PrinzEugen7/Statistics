# -*- coding: utf-8 -*-
import numpy as np

def main():
    # 母集団の生成
    data = np.random.rand(50)
    # 母平均の点推定
    ave = np.ndarray([])                    # 標本平均を格納する配列
    # 点推定(100回繰り返し)
    for i in range(100):
        x = np.random.choice(data,5)        # 母集団からサイズ5の標本を抽出
        ave = np.append(ave, np.average(x)) # 標本平均を計算して配列に格納

    mu = np.average(ave)                    # 100個の標本平均の平均値:母集団の推定平均値
    # 結果を表示
    print u"点推定で求めた母平均:",mu
    print u"実際の母平均:",np.average(data)

if __name__ == '__main__':
    main()
