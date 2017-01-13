# -*- coding: utf-8 -*-
import numpy as np
 
 
def main():
    A = np.array([[2.,1.,1.]   # 行列Aの生成
                 ,[1.,2.,1.]
                 ,[1.,1.,1.]])
 
    B = np.array([[2.,3.,3.]   # 行列Bの生成
                 ,[1.,2.,3.]
                 ,[3.,3.,3.]])
 
    C = np.cross(A,B)          # 行列AとBの外積を計算
    print(C)
 
 
if __name__ == '__main__':
    main()
