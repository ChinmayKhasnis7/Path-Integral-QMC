## Chinmay Khasanis
import random
import math

class harmonic_piqmc:
    # Constructor method to initialize the class with given parameters
    def __init__(self, N, parameters):
        # Assigning values returned by the parameters function to class attributes
        self.warm_steps, self.MC_steps, self.dump_freq, self.delta, self.N, self.w, self.m = parameters(N)
        
        # Initializing lists to store states and correlations
        self.state = [random.random() - 0.5 for _ in range(self.N)]
        self.state_o = [0.0]*self.N
        self.state_n = [0.0]*self.N
        self.correlation = [0.0]*self.N
        self.correlation_2 = [0.0]*self.N

        # Initializing variables to calculate mean values
        self.x2_mean = 0.0
        self.x_mean = 0.0

    def thermalization(self):
        print("Warming up %2i states...."%self.N)
        for _ in range(0, self.warm_steps):
            for tau in range(self.N):
                self.state_o[tau] = self.state[tau]
                del_X = 2.0 * self.delta * (random.random() - 0.5)
                self.state_n[tau] = self.state[tau] + del_X
                dS = (pow((self.state[(tau + 1) % self.N] - self.state_n[tau]), 2.0)
                      + 0.25 * self.w * self.w *
                      pow((self.state[(tau + 1) % self.N] + self.state_n[tau]), 2.0))
                - (pow((self.state[(tau + 1) % self.N] - self.state_o[tau]), 2.0)
                   + 0.25 * self.w * self.w *
                   pow((self.state[(tau + 1) % self.N] + self.state_o[tau]), 2.0))
                dS = (self.m / 2.0) * dS

                u = random.random()
                if u < math.exp(-dS):
                    self.state[tau] = self.state_n[tau]
                else:
                    self.state[tau] = self.state_o[tau]

    def generate_MC_steps(self):
        print("Generating PIQMC samples for %2i states...."%self.N)
        tot = 0
        Norm = self.dump_freq / (2.0 * self.m * self.w * self.MC_steps)
        for i in range(0, self.MC_steps):
            for tau in range(self.N):
                self.state_o[tau] = self.state[tau]
                del_X = 2.0 * self.delta * (random.random() - 0.5)
                self.state_n[tau] = self.state[tau] + del_X
                dS = (pow((self.state[(tau + 1) % self.N] - self.state_n[tau]), 2.0)
                      + 0.25 * self.w * self.w *
                      pow((self.state[(tau + 1) % self.N] + self.state_n[tau]), 2.0))
                - (pow((self.state[(tau + 1) % self.N] - self.state_o[tau]), 2.0)
                   + 0.25 * self.w * self.w *
                   pow((self.state[(tau + 1) % self.N] + self.state_o[tau]), 2.0))
                dS = (self.m / 2.0) * dS
                u = random.random()
                if u < math.exp(-dS):
                    self.state[tau] = self.state_n[tau]

            if i % self.dump_freq == 0:
                for t in range(self.N):
                    self.correlation[t] += self.state[t] * self.state[0] * Norm
                    self.correlation_2[t] += pow(self.state[t] * self.state[0] * Norm, 2.0)
                    self.x_mean += self.state[t]
                    self.x2_mean += self.state[t] * self.state[t] / (2 * self.m * self.w)
                tot += 1

        norm = self.dump_freq/(self.MC_steps*self.N)
        self.x2_mean = self.x2_mean * norm
        self.x_mean = self.x_mean * norm

        E_0 = self.m*pow(self.w,2.0) * self.x2_mean
        print(f"<x^2> = {self.x2_mean}")
        print(f"<x> = {self.x_mean}")
        print(f"Ground state energy = {E_0}\n") 
        return self.correlation, E_0

