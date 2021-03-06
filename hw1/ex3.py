import itertools
import random
import scipy.stats as sct
import numpy as np
import matplotlib.pyplot as plt

def aprox():
    
    nmax = 10000
    # number of samples
    x_axis = np.arange(100, nmax + 100, 100)
    mu_estim = []
    mu_true = 1/12
    full = 0
    x=[]
    finalo = []
    o = []

    for combination in itertools.permutations([1,2,3,4], 4):
        #take all the possible permutations of (F,U,L,L=1,2,3,4)
        x.append(combination)
        print(x[0])
    for n in x_axis:
        for i in range(n):
            o.append(random.choice(x)) 
        #icrease the counter for every FULL occurence
        for i in o:
            if i == x[0] or i == x[1]:
                full = full + 1
        #calculate the estimated probability
        f = full/len(o)
        mu_estim.append(f)
        o.clear() 
        finalo.clear()
        full = 0
    #convergence plot
    plt.plot(x_axis, mu_estim, '-g', alpha = 0.5)
    plt.hlines(y = mu_true, xmin = x_axis[0], 
              xmax = x_axis[-1], colors = 'blue', lw = 6.5)
    plt.title(f'Convergence to $Np = ${mu_true}')
    plt.xlabel('Sample size')
    plt.ylabel('$E[X]$')
    plt.xticks(rotation = 90)
    plt.grid()
    plt.show()

if __name__ == '__main__': 
    aprox()

import math

