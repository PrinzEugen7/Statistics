# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

def main():

    X = [1,2,3,4,5]
    Y = [1.1, 2.1, 2.8, 4.3, 5.1]

    A = np.array([X,np.ones(len(X))])
    A = A.T
    a,b = np.linalg.lstsq(A,Y)[0]

    plt.plot(X,Y,"ro")
    plt.plot(X,(a*X+b),"g--")
    plt.grid()
    plt.show()


if __name__ == '__main__':
    main()
