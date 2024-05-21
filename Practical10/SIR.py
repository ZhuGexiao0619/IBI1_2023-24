import numpy as np
import matplotlib.pyplot as plt
S = 9999
I = 1
R = 0
beta = 0.3
gamma = 0.05
N = 10000
S_time = []
I_time = []
R_time = []
for t in range(1000):
    contact_rate = beta * I / N
    infections = np.random.choice([1,0], S, p=[contact_rate, 1- contact_rate])
    new_I = infections.sum()
    recoveries = np.random.choice([1,0], I, p=[gamma, 1-gamma])
    new_R = recoveries.sum()
    S -= new_I
    I = I + new_I - new_R
    R += new_R
    S_time.append(S)
    I_time.append(I)
    R_time.append(R)
plt.figure(figsize=(6,4), dpi=150)
plt.plot(S_time, label="susceptible")
plt.plot(I_time, label="infected")
plt.plot(R_time, label="recovered")
plt.xlabel("time")
plt.ylabel("Number")
plt.legend()
plt.title("SIR model")
plt.show()