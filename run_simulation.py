from PIQMC import harmonic_piqmc
import matplotlib.pyplot as plt
import numpy as np 

# simulation parameters
def parameters(N):
    N = N                   # number of time steps
    warm_steps = 100000     # total thermalization steps
    MC_steps = 1000000      # total mc steps
    dump_freq = 100         # interval between measurements
    delta = 0.5             # change in  spacial variable
    w = 1;  m = 1           # Angular velocity, mass      
    return warm_steps,MC_steps,dump_freq,delta,N,w,m

# start
corln = [];  E = []
N_list =[4, 8]
for N in N_list:
    simulation = harmonic_piqmc(N,parameters)
    simulation.thermalization()
    corr, E_0 = simulation.generate_MC_steps()
    corln.append(np.array(corr))
    E.append(np.array(E_0))

# plot
def plot_all(corln):
    fig, axs = plt.subplots(2, 2, figsize=(16, 12))
    fig.suptitle('Correlation vs Euclidean time (Tau)', fontsize=18)
    for i, corn in enumerate(corln):
        n = len(corn)
        row = i // 2
        col = i % 2
        axs[row, col].plot(np.linspace(0, n, n), corn, linewidth=2)
        axs[row, col].set_ylabel('$<x(t) x(0)>$',fontsize=15)
        axs[row, col].set_xlabel('$Tau$',fontsize=15)
        axs[row, col].set_title('(N=%2i)' % n,fontsize=15)
        axs[row, col].tick_params(labelsize= 'large',length=5,width=2,grid_alpha=0.5)
        axs[row, col].grid()
plot_all(corln)