#%%
import numpy as np
import matplotlib.pyplot as plt
from math import comb

def catalan_number(n):
    return comb(2*n-2, n-1) // n # does fun catalan number calculation

def compute_P(n_max):
    P = [catalan_number(n) for n in range(2, n_max+1)] # calculates P(n) for n = 2 to n_max
    plt.figure() 
    plt.plot(range(2, n_max+1), P, marker='o') # plots P(n) vs n
    plt.xlabel('n')
    plt.ylabel('P(n)')
    plt.title('Number of Ways to Parenthesize (2 <= n <= 20)')
    plt.show()
    
if __name__ == "__main__":
    compute_P(20)
# %%
