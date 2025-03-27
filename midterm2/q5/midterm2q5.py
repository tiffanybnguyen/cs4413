#%%
import math
import matplotlib.pyplot as plt

def stirling_approx(n):
    return math.sqrt(2 * math.pi * n) * (n / math.e) ** n

# a
def compute_stirling_error(n_max):
    errors = [abs(stirling_approx(n) - math.factorial(n)) for n in range(2, n_max+1)]
    return errors

def plot_stirling_error(n_max):
    errors = compute_stirling_error(n_max)
    plt.figure()
    plt.plot(range(2, n_max+1), errors, marker='o') # plots error vs n
    plt.xlabel('n')
    plt.ylabel('Error')
    plt.title('Stirling Approximation Error')
    plt.yscale('log')
    plt.show()

# b
def compute_relative_error(n_max):
    errors = [abs(stirling_approx(n) - math.factorial(n)) / math.factorial(n) for n in range(2, n_max+1)]
    return errors

def plot_relative_error(n_max):
    errors = compute_relative_error(n_max)
    plt.figure()
    plt.plot(range(2, n_max+1), errors, marker='o') # plots relative error vs n
    plt.xlabel('n')
    plt.ylabel('Relative Error')
    plt.title('Stirling Approximation Relative Error')
    plt.yscale('log')
    plt.show()
    
    
if __name__ == "__main__":
    plot_stirling_error(20)
    print(compute_stirling_error(20))
    plot_relative_error(20) 
    print(compute_relative_error(20))
    

# %%
