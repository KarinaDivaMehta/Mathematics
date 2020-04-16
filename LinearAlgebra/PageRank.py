import numpy as np
import numpy.linalg as la

# M = dL + (1-d)J/n
# d is the possiblity of following the page
# J is a n x n matrix full of 1
# n is the number of websites
# initial r is evenly distributed
def pageRank(linkMatrix, d) :
    n = linkMatrix.shape[0]
    M = d * linkMatrix + (1-d)/n * np.ones([n, n])
    r = 100 * np.ones(n) / n
    lastR = r
    r = M @ r
    i = 0
    while la.norm(lastR - r) > 0.01 :
        lastR = r
        r = M @ r
        i += 1
    return r