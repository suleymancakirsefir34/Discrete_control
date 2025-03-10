import matplotlib
import matplotlib.pyplot as plt
import numpy as np


#paramaters
dt = 0.001

t_initial = 0
t_final = 10

x_0 = 0
v_0 = 0

t = np.arange(t_initial,t_final,dt)
X_t_f = np.arange(t_initial,t_final,dt)
V_t_f = np.arange(t_initial,t_final,dt)

F = np.arange(t_initial,t_final,dt)

for i in range(0,int((t_final - t_initial)/dt)):
    F[i] = 10


#system paramaters
m = 1
c = 2
k = 1

for i in range(0,int((t_final - t_initial)/dt) - 1):
    X_t_f[i + 1] = X_t_f[i] + dt*V_t_f[i]
    V_t_f[i + 1] = -(k*dt/m)*X_t_f[i] +(1 - (c*dt/k))*V_t_f[i] + dt/m*F[i]

plt.figure()
plt.subplot(311)  # Yeni bir figür oluşturuluyor
plt.plot(t, X_t_f, 'r')  # Zaman vektörüne karşılık x vektörü kırmızı ('r') ile çiziliyor
plt.ylabel('Meter(m)')  # Y eksenine birim ekleniyor
plt.xlabel('Time(sec)')  # X eksenine birim ekleniyor
plt.title('MCK System')  # Grafik başlığı ekleniyor
plt.grid(True)  # Grafik üzerinde bir ızgara gösteriliyor


plt.subplot(312)  
plt.plot(t, V_t_f, 'g')  
plt.ylabel('Velocity(m/s)')  
plt.xlabel('Time(sec)')  
plt.grid(True)  

plt.subplot(313)  
plt.plot(t, F, 'b')  
plt.ylabel('Force(N)')  
plt.xlabel('Time(sec)')  
plt.grid(True)  

plt.show()  # Grafik ekranda gösteriliyor
