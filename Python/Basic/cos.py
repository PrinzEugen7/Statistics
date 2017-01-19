# -*- coding: utf-8 -*-
import math

def main():
    # 度[deg]
    deg = 90

    # 度[deg]をラジアン[rad]に変換
    rad = math.radians(deg)

    y = math.cos(rad)

    # 結果表示
    print(y)

if __name__ == "__main__":
    main()
