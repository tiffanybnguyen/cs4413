#%%
import numpy as np
import matplotlib.pyplot as plt

def generate_pairs(N):
    # generates a new seed every time
    ui = np.random.default_rng().uniform(0, 1, N) 
    vi = np.random.default_rng().uniform(0, 1, N)
    
    return ui, vi

def plot_unit_square(N):
    ui, vi = generate_pairs(N)
    plt.figure(figsize=(5,5))
    plt.scatter(ui, vi, s=1, color='blue')
    plt.xlabel('u')
    plt.ylabel('v')
    plt.title(f'N={N} pairs on Unit Square')
    plt.show()
    
def estimate_pi(N):
    ui, vi = generate_pairs(N)
    count = 0
    for i in range(N): # for i = 1 to N
        if ui[i]**2 + vi[i]**2 <= 1: # if u^2 + v^2<= 1 then count = count + 1
            count += 1
    return count / N # returns ratio of count / N (this will estimate pi/4, thanks Monte Carlo)

def plot_pi_estimates():
    N_values = [10**3, 10**4, 10**5, 10**6] # N = 10^3, 10^4, 10^5, 10^6
    pi_estimates = [estimate_pi(N) for N in N_values] # estimate π/4 for each N
    
    plt.figure()
    plt.plot(N_values, pi_estimates, marker='o', linestyle='-', label='Estimated π/4') # plot the estimated π/4
    plt.axhline(y=22/(7*4), color='r', linestyle='--', label='True π/4') # plot the true value of π/4
    plt.xscale('log') # log scale on x-axis
    plt.xlabel('N') # x-axis label
    plt.ylabel('π/4 estimate') # y-axis label
    plt.legend() 
    plt.title('Monte Carlo Estimate of π/4 vs N')
    plt.show()

if __name__ == "__main__":
    N = 10**3
    plot_unit_square(N)
    plot_pi_estimates()
    
# %%
