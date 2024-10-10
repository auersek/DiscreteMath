import matplotlib.pyplot as plt
import numpy as np
import time

def converter(u, v):
    res = []
    for i in range(max(u) + 1):
        res.append([])
    for i in range(len(u)):
        res[u[i]].append(v[i])
    print(res)


if __name__ == '__main__':
    u = [0, 1, 2, 3, 0, 1, 2, 3, 2, 1, 4, 4, 3]
    v = [1, 3, 0, 1, 2, 1, 2, 2, 1, 2, 2, 3, 3]

    converter(u, v)



