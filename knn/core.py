import torch
import torch.nn as nn
from torch.autograd import Variable
import matplotlib.pyplot as plt
import time

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
    n, d = ref.size()
    m, d = qry.size()
    mref = ref.expand(m, n, d)
    mqry = qry.expand(n, m, d).transpose(0,1)
    print(mqry - mref)
    dist = torch.sum((mqry - mref)**2, 2).squeeze()**0.5
    dist, inds = torch.topk(dist, k, dim = 1, largest = False, sorted = False)
    return inds, dist

if __name__ == "__main__":
    torch.random.manual_seed(0)

    ref = Variable(torch.FloatTensor(50000, 3).random_()).cuda()
    qry = Variable(torch.FloatTensor(5000, 3).random_()).cuda()

    t0 = time.time()
    inds, dist = knn(ref, qry, 8)
    print(time.time() - t0)

    # t = 21
    # ref_regional = ref[inds,:]
    # test_point = qry[t,:].cpu().data.numpy()
    # neighborhood = ref_regional[t,:,:].cpu().data.numpy()
    # plt.scatter(ref[:,0], ref[:,1])
    # plt.scatter(test_point[0], test_point[1], s = 100, c = 'green')
    # plt.scatter(neighborhood[:,0], neighborhood[:,1], s = 100, c = 'red')
    # plt.show()
