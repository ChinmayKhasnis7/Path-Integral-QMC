## Chinmay Khasanis
# Importing necessary libraries and modules
from PIQMC import harmonic_piqmc  # Importing the `harmonic_piqmc` class from the `PIQMC` module
import matplotlib.pyplot as plt
import numpy as np

# Function to define simulation parameters based on `N` (number of time steps)
def parameters(N):
    N = N                   # number of time steps
    warm_steps = 100000     # total thermalization steps
    MC_steps = 1000000      # total MC steps
    dump_freq = 100         # interval between measurements
    delta = 0.5             # change in spatial variable
    w = 1;  m = 1           # Angular velocity, mass      
    return warm_steps, MC_steps, dump_freq, delta, N, w, m

# Starting simulation for different `N` values
corln = []  # List to store correlations
E = []      # List to store energies
N_list = [8, 16, 32, 64]  # List of `N` values for simulations
for N in N_list:
    # Initializing simulation with `harmonic_piqmc` class and parameters function
    simulation = harmonic_piqmc(N, parameters)
    
    # Thermalization step
    simulation.thermalization()
    
    # Generating Monte Carlo steps and obtaining correlation and ground state energy
    corr, E_0 = simulation.generate_MC_steps()
    
    # Appending obtained correlations and energies to respective lists
    corln.append(np.array(corr))
    E.append(np.array(E_0))

# Function to plot correlations against Euclidean time (Tau)
def plot_all(corln):
    fig, axs = plt.subplots(2, 2, figsize=(16, 12))  # Creating a subplot layout
    fig.suptitle('Correlation vs Euclidean time (Tau)', fontsize=18)  # Setting main title
    
    # Iterating through correlations and plotting them in subplots
    for i, corn in enumerate(corln):
        n = len(corn)  # Getting length of current correlation data
        row = i // 2   # Calculating row for current subplot
        col = i % 2    # Calculating column for current subplot
        
        # Plotting correlation data
        axs[row, col].plot(np.linspace(0, n, n), corn, linewidth=2)
        axs[row, col].set_ylabel('$<x(t) x(0)>$', fontsize=15)
        axs[row, col].set_xlabel('$Tau$', fontsize=15)
        axs[row, col].set_title('(N=%2i)' % n, fontsize=15)
        axs[row, col].tick_params(labelsize='large', length=5, width=2, grid_alpha=0.5)
        axs[row, col].grid()

# Calling the function to plot correlations
plot_all(corln)
