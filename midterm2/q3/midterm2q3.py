#%%
import matplotlib.pyplot as plt
from math import comb

def p_nj(n, j):
    return comb(n, j) * (1/n)**j * (1 - 1/n)**(n-j) # probability function p(n, j)

def compute_LV(n_max):
    L = {1: 1}  # base case: L(1) = 1
    
    for n in range(2, n_max + 1):
        sum_Lp = sum(L[j] * p_nj(n, j) for j in range(2, n))
        denominator = 1 - p_nj(n, 0) - p_nj(n, n)
        L[n] = (1 + sum_Lp) / denominator if denominator != 0 else 0  # avoid dividing by 0
    
    return L

def plot_LV(n_max):
    L_values = compute_LV(n_max)
    n_values = list(L_values.keys())
    
    plt.figure(figsize=(8, 5))
    plt.plot(n_values, [L_values[n] for n in n_values], marker='o', color='b', label='Las Vegas L(n)')
    plt.xlabel('n')
    plt.ylabel('L(n)')
    plt.title('Las Vegas Analysis: Electing a Leader')
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    plot_LV(30)

# %%
