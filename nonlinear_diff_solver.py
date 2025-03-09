import matplotlib
import matplotlib.pyplot as plt
import numpy as np


def forward_solver(t_initial, t_final, dt, x_0, system_coef_x, system_coef_u, u):
    x_var = np.arange(t_initial,t_final,dt)
    x_var[0] = x_0

    for i in range(0,int((t_final-t_initial)/dt)-1):
        x_var[i+1] =  x_var[i] + dt*(system_coef_x * x_var[i] +system_coef_u*u[i])

    return x_var


#parameters

dt = 0.00001
t_initial = 0
t_final = 3
x_0 = 0
system_coef_x = -1
system_coef_u = 1
u_bias = 100

x = np.arange(t_initial,t_final,dt)
t = np.arange(t_initial,t_final,dt)
u = np.arange(t_initial,t_final,dt)


for i in range(0,int((t_final-t_initial)/dt)-1):
    u[i] = u_bias

x = forward_solver(t_initial,t_final,dt,x_0,system_coef_x,system_coef_u,u)

plt.figure()
plt.plot(t,x,'r')
plt.xlabel('time(sec)')
plt.ylabel('meter(m)')
plt.title('forward solver')
plt.grid(True)
plt.show()