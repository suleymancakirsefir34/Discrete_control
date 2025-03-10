import matplotlib
import matplotlib.pyplot as plt
import numpy as np 

# Zaman adımı
dt = 0.001

# Başlangıç ve bitiş zamanı
t_initial = 0.0
t_final = 20.0
# Döngü uzunluğu (toplam adım sayısı)
length_of_loop = int((t_final - t_initial)/dt)

# Zaman dizisi oluşturma
t = np.arange(t_initial,t_final,dt,dtype=float)

# Başlangıç pozisyonu ve hızı
x_0 = 0
v_0 = 0

# Uygulanan kuvvet dizisi
F = np.arange(t_initial,t_final,dt,dtype=float)

# Her zaman adımında kuvveti 10 yapıyoruz
for i in range(0,length_of_loop):
    F[i] = 10

# Sistem parametreleri
m = 1  # kütle
c = 2  # sönüm katsayısı
k = 1  # yay sabiti

# A matrisi (sistem matrisi)
row_a = 2
column_a = 2
A = np.arange(row_a*column_a,dtype=float).reshape(row_a,column_a)
A[0,0] = 1
A[0,1] = dt
A[1,0] = -k*dt/m
A[1,1] = (1 - c*dt/m)

# B matrisi (girdi matrisi)
row_b = 2
column_b = 1
B = np.arange(row_b*column_b,dtype=float).reshape(row_b,column_b)
B[0,0] = 0
B[1,0] = dt/m
print(B)

# Sistem değişkenleri
state_number = 2  # iki durum var: pozisyon ve hız
tru = np.arange(state_number*length_of_loop,dtype=float).reshape(length_of_loop,state_number)
tru[0,0] = x_0  # başlangıç pozisyonu
tru[0,1] = v_0  # başlangıç hızı

# İleri fark yöntemi ile sistemin simülasyonu
for i in range (0,length_of_loop - 1):
    # Sistem denklemleri: A * durum + B * kuvvet
    tru[i+1,:] = np.transpose(A.dot(tru[i,:])).flatten() + B.dot(F[i]).flatten()



# Grafik çizimi
plt.figure()
plt.plot(t,tru[:,0],'r')  # Pozisyon (kırmızı)
plt.plot(t,tru[:,1],'b')  # Hız (mavi)

# Grafik ayarları
plt.grid(True)
plt.title('MCK Sistemi (Kuvvet Dizisi ile)')
plt.show()
