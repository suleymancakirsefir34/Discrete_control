#######################################################
################### FORWARD SOLVER  ###################

# Gerekli kütüphaneler matplotlib ve numpy import ediliyor
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Zaman adımı dt tanımlanıyor
dt = 0.001

# Başlangıç ve bitiş zamanları belirleniyor
t_initial = 0.0
t_final = 1.0

# Zaman vektörü t oluşturuluyor, t_initial'dan t_final'a kadar dt aralıklarıyla
t = np.arange(t_initial, t_final, dt)

# Değişkenin (x'in) zaman içindeki değerleri için bir vektör oluşturuluyor
x = np.arange(t_initial, t_final, dt)

# Başlangıç koşulu: x'in başlangıçtaki değeri 10 olarak atanıyor
x[0] = 10

# Bir döngü oluşturuluyor, her adımda x'in bir sonraki değeri hesaplanıyor
for k in range(0, int((t_final-t_initial)/dt) - 1):
    # Birinci dereceden dinamik model: x'in bir sonraki değeri, şu anki değeri eksi 5 ile çarpılarak hesaplanıyor
    x[k + 1] = x[k] + dt * (-5 * x[k])

# Sonuçlar grafiğe dökülüyor
plt.figure()  # Yeni bir figür oluşturuluyor
plt.plot(t, x, 'r')  # Zaman vektörüne karşılık x vektörü kırmızı ('r') ile çiziliyor
plt.ylabel('Meter(m)')  # Y eksenine birim ekleniyor
plt.xlabel('Time(sec)')  # X eksenine birim ekleniyor
plt.title('First order dynamics')  # Grafik başlığı ekleniyor
plt.grid(True)  # Grafik üzerinde bir ızgara gösteriliyor
plt.show()  # Grafik ekranda gösteriliyor
