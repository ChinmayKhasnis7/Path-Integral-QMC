#  Path Integral Quantum Monte Carlo (PI-QMC)
This repository contains Python implementation PI-QMC to find the ground state energy of the harmonic oscillator. The action for Wick rotated Harmonic oscillator in Euclidean time, $t \rightarrow  -i\tau$.
$$S[x(\tau)]=\int_{\tau_a}^{\tau_b} d \tau\left(\frac{1}{2} m \dot{x}^2+\frac{1}{2} m \omega^2 x^2\right)$$

Applying periodic boundary condition $x\left(\tau_{i+N}\right)=x\left(\tau_i\right)$,
$$S_L=\frac{m \Delta}{2} \sum_{i=0}^{N-1}\left[\left(\frac{x_{i+1}-x_i}{\Delta}\right)^2+\omega^2\left(\frac{x_{i+1}+x_i}{2}\right)^2\right]$$
Converting into reduced units $\hat{m}=m \Delta, \hat{\omega}=\omega \Delta, \hat{x}\left(\tau_i\right)=\hat{x}_i=\frac{x_i}{\Delta}$,

```math
\Delta S_L=\frac{\hat{m}}{2} \sum_{i=0}^{N-1} \left[\left(\hat{x}_{i+1}-\hat{x}_i^{\prime}\right)^2 -\left(\hat{x}_{i+1}-\hat{x}_i\right)^2+\frac{\hat{\omega}^2}{4}\left(\left(\hat{x}_{i+1}+\hat{x}_i^{\prime}\right)^2- \left(\hat{x}_{i+1}+\hat{x}_i\right)^2\right)\right]
```
Choose $\xi \sim Unif[-\Delta, \Delta]$ and update the configuration $\hat{x}_i^{\prime}=\hat{x}_i+\xi$. 
Now compute the  change in action $\Delta S_L=S_L\left(\hat{x}_i^{\prime}\right)-S_L\left(\hat{x}_i\right)$,

$$\Delta S_L=\frac{\hat{m}}{2} \sum_{i=0}^{N-1} \left[\left(\hat{x}_{i+1}-\hat{x}_i^{\prime}\right)^2 -\left(\hat{x}_{i+1}-\hat{x}_i\right)^2+\frac{\hat{\omega}^2}{4}\left(\left(\hat{x}_{i+1}+\hat{x}_i^{\prime}\right)^2- \left(\hat{x}_{i+1}+\hat{x}_i\right)^2\right)\right]$$


