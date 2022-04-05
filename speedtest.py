import time 
import numpy as np
import random

x = np.zeros((4*10**6,8,3))
n = []
for i in range(4*10**6):
    if not i%1000:
        print(i)
    for j in range(8):
        for k in range(3):
            n.append(i+j+k)
            # x[i,j,k] = i+j+k
    # n.append( n.array([[random.randint(0,8) for i in range(3)] for k in range(8)], np.byte))

