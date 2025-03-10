import matplotlib
import matplotlib.pyplot as plt
import numpy as np


dt = 0.40

t_initial = 0.0
t_final = 20.0

lenght_of_loop = int((t_final - t_initial)/dt)

t = np.arange(t_initial,t_final,dt,dtype=float)

y1_0 = 2
y2_0 = -2
mu = 1

row_a = 2
column_a = 2

A = np.arange(row_a*column_a,dtype=float).reshape(row_a,column_a)


state_number = column_a

tru = np.arange(lenght_of_loop*state_number,dtype=float).reshape(lenght_of_loop,state_number)
 
tru[0,0] = y1_0
tru[0,1] = y2_0


for i in range(0,lenght_of_loop-1):
    A[0,0] = 1
    A[0,1] = dt
    A[1,0] = -dt
    A[1,1] = (1 + mu*dt*(1 - tru[i,0]*tru[i,0]))
    tru[i+1,:] = A.dot(np.transpose(tru[i,:])).flatten()


# Grafik çizimi
plt.figure()
plt.plot(t,tru[:,0],'r')  
plt.plot(t,tru[:,1],'b')  

# Grafik ayarları
plt.grid(True)
plt.title('vanderpoldif')
plt.show()


