#######################################################
## forward solver function definition
def forward_solver(t_initial,t_final,dt, initial_cond):

    x_var = np.arange(t_initial, t_final, dt)
    x_var[0] = initial_cond

    for k in range(0,int((t_final - t_initial)/dt) - 1):
        x_var[k + 1] = x_var[k] + dt * (-5 * x_var[k])
    return x_var
#######################################################
## backward solver function definition
def backward_solver(t_initial,t_final,dt, initial_cond):

    x_var = np.arange(t_initial, t_final, dt)
    x_var[0] = initial_cond

    for k in range(1,int((t_final - t_initial)/dt)):
        x_var[k] = x_var[k - 1] + dt * (-5 * x_var[k- 1])
    return x_var
#######################################################
## centred solver function definition
def centred_solver(t_initial,t_final,dt, initial_cond, initial_cond_2):

    x_var = np.arange(t_initial, t_final, dt)
    x_var[0] = initial_cond
    x_var[1] = initial_cond_2
    for k in range(1,int((t_final - t_initial)/dt)):
        x_var[k+1] = x_var[k - 1] + 2 *dt * (-5 * x_var[k- 1])
    return x_var
#######################################################
#######################################################
## main code

# Gerekli kütüphaneler matplotlib ve numpy import ediliyor
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Zaman adımı dt tanımlanıyor
dt = 0.001

# Başlangıç ve bitiş zamanları belirleniyor
t_initial = 0.0
t_final = 1.0
x_0 = 10
x_1 = x_0 + (-5)*dt*x_0/5
# Zaman vektörü t oluşturuluyor, t_initial'dan t_final'a kadar dt aralıklarıyla
t = np.arange(t_initial, t_final, dt)

# Değişkenin (x'in) zaman içindeki değerleri için bir vektör oluşturuluyor
x = np.arange(t_initial, t_final, dt)

x = forward_solver(t_initial,t_final,dt,x_0)

# Sonuçlar grafiğe dökülüyor
plt.figure()  # Yeni bir figür oluşturuluyor
plt.plot(t, x, 'r')  # Zaman vektörüne karşılık x vektörü kırmızı ('r') ile çiziliyor
plt.ylabel('Meter(m)')  # Y eksenine birim ekleniyor
plt.xlabel('Time(sec)')  # X eksenine birim ekleniyor
plt.title('First order dynamics')  # Grafik başlığı ekleniyor
plt.grid(True)  # Grafik üzerinde bir ızgara gösteriliyor
plt.show()  # Grafik ekranda gösteriliyor


## main code
#######################################################