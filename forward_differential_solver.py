import matplotlib
import matplotlib.pyplot as plt
import numpy as np

dt = 0.001

t_initial = 0.0
t_final = 1.0

t = np.arange(t_initial,t_final,dt)
x = np.arange(t_initial,t_final,dt)

x[0] = 10

for k in range(0, int(t_final/dt) - 1):
    x[k +1] = x[k] + dt*(-5*x[k])

plt.figure()
plt.plot(t,x,'r')
plt.ylabel('Meter(m)')
plt.xlabel('Time(sec)')
plt.title('First order dynamics')
plt.grid(True)
plt.show()