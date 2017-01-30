# -*- coding: utf-8 -*-
import numpy as np

def main():
    x = np.array([1,2,3])
    y = np.array([4,5,6,7])
    xx, yy = np.meshgrid(x, y)
    print(xx)
    print(yy)

if __name__ == '__main__':
    main()
