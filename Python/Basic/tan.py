# -*- coding: utf-8 -*-
import math

def main():
    # 度[deg]
    deg = 45

    # 度[deg]をラジアン[rad]に変換
    rad = math.radians(deg)

    y = math.tan(rad)

    # 結果表示
    print(y)

if __name__ == "__main__":
    main()
