# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

def main():
    data = pd.read_csv("data.csv", sep=",")
    print(data.head)
    
if __name__ == "__main__":
    main()
