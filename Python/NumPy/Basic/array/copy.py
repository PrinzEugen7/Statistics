# -*- coding: utf-8 -*-
import numpy as np

def main():
    x = np.array([1, 2, 3])
    y = x.copy()
    y = y * 2
    print("x=", x)
    print("y=", y)

if __name__ == '__main__':
    main()
