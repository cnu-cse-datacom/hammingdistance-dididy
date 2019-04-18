import random
import numpy as np
import pandas as pd
from hamming_practice import hamming

df = pd.read_csv('sample.csv', names=['word','bin'])

count = 0
minimum = 0
for i in range(0, 99):
    for j in range(i+1, 100):
        hd = hamming(df.iloc[i,1], df.iloc[j,1]) # hamming_practice
        print(count,"(", df.iloc[i,0], df.iloc[j,0], ")", hd)
        if i == 0:
            minimum = hd
        if hd < minimum:
            minimum = hd
        count = count + 1
   

print("min hamming distnace", minimum)
