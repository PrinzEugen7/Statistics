# -*- coding: utf-8 -*-
import math

def main():

    x = 1
    y = 1
    rad = math.atan2(y, x)

    # ラジアンを度に変換
    deg = math.degrees(rad)
    # 結果表示
    print(rad)
    print(deg)

if __name__ == "__main__":
    main()
