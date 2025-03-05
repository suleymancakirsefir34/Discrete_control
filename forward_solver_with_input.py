import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# Bu fonksiyon ileri çözüm yöntemini kullanarak bir sistemin zamanla nasıl geliştiğini çözer.
# Parametreler:
# t_initial: Başlangıç zamanı
# t_final: Bitiş zamanı
# dt: Zaman adımı
# initial_cond: Sistemin başlangıç koşulu
# system_coef_x: Sistem değişkeni katsayısı (x için katsayı)
# system_coef_u: Giriş katsayısı (u için katsayı)
# u: Sisteme uygulanan giriş dizisi
def forward_solver(t_initial, t_final, dt, initial_cond, system_coef_x, system_coef_u, u):
    
    # x_var: Sistemin çözümünün depolandığı dizi
    x_var = np.arange(t_initial, t_final, dt)
    # Başlangıç koşulunu x_var'ın ilk elemanına atar
    x_var[0] = initial_cond
    
    # Sistemin zaman içinde nasıl evrildiğini hesaplamak için döngü
    for k in range(0, int((t_final - t_initial)/dt) - 1):
        # Euler yöntemi kullanarak bir sonraki adımı hesaplar
        x_var[k+1] = x_var[k] + dt * (system_coef_x * x_var[k] + system_coef_u * u[k])
    
    return x_var

# PARAMETRELER
dt = 0.001  # Zaman adımı
t_initial = 0  # Başlangıç zamanı
t_final = 4  # Bitiş zamanı
x_0 = 0  # Başlangıçtaki sistem durumu
system_coef_x = 1  # x için sistem katsayısı
system_coef_u = 1  # u için sistem katsayısı

# Zaman dizisi oluşturulur
t = np.arange(t_initial, t_final, dt)
# Sistemin durumunu tutmak için dizi
x = np.arange(t_initial, t_final, dt)
# Giriş sinyali için dizi
u = np.arange(t_initial, t_final, dt)

# Giriş sinyali olan u'yu sabit 100 değeri ile dolduruyoruz
for i in range(0, int((t_final - t_initial) / dt) - 1):
    u[i] = 100

# Sistemin çözümünü forward_solver fonksiyonu ile buluyoruz
x = forward_solver(t_initial, t_final, dt, x_0, system_coef_x, system_coef_u, u)

# Çözümü grafiğe dökelim
plt.figure()
# Zaman (t) ve sistemin durumu (x) arasındaki ilişkiyi çiz
plt.plot(t, x, 'r')
# Grafik etiketleri ve başlıklar
plt.xlabel('time (t)')
plt.ylabel('meter (m)')
plt.grid(True)
plt.title('forward_solver')

# Grafiği ekranda göster
plt.show()
