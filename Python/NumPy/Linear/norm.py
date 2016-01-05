# -*- coding: utf-8 -*-
import numpy as np

def main():
    a = np.array([1, 1])
    b = np.array([4, 4])
    l = np.linalg.norm(b-a)
    print l

if __name__ == '__main__':
    main()
