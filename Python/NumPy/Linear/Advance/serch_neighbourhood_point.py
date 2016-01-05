# -*- coding: utf-8 -*-
import numpy as np

# 点p0に一番近い点を点群psから抽出
def serch_neighbourhood(p0, ps):
    L = np.array([])
    for i in xrange(ps.shape[0]):
        L = np.append(L,np.linalg.norm(ps[i]-p0))
    return ps[np.argmin(L)]

def main():
    p0 = np.array([0, 0])
    ps = np.array([[1,1],[2,2],[3,3]])
    print serch_neighbourhood(p0, ps)

if __name__ == '__main__':
    main()
