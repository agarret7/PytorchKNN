import torch
import torch.nn as nn
import matplotlib.pyplot as plt

import numpy as np
from scipy.spatial.distance import cdist

try:
    pass
except SystemError:
    pass

def knn(ref, qry, k):
    """
    TODO
    :type ref: TODO
    :type qrt: TODO
    :type k: TODO
    :rtype: TODO
    :param ref: TODO
    :param qry: TODO
    :param k: TODO
    :return: TODO
    """
    return None

if __name__ == "__main__":
    ref = torch.FloatTensor(100, 3).random_()
    qry = torch.FloatTensor(10 , 3).random_()
    dist = knn(ref, qry, 3)
    print(dist)

    m = 2500
    p = 10
    mp1 = torch.rand(m,p)
    mp2 = torch.rand(m,p)
    mmp1 = torch.stack([mp1]*m)
    mmp2 = torch.stack([mp2]*m).transpose(0,1)
    mm = torch.sum((mmp1-mmp2)**2,2).squeeze()
    print(mm)

    print("start")
    print(np.sort(np.random.rand(50000000)))
    print("stop")
