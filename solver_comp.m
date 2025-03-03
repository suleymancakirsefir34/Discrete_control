%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%      FORWARD - BACKWARD -  CENTRED DIFFERENCE COMPARISON
%           İLERİ - GERİ - MERKEZİ FARK KARŞILAŞTIRMASI
%       Çözümü karşılaştırılacak fonksiyon : x_dot(t) = -5.x(t)

clear all;      % tüm değişkenler silinir.
close all;      % tüm figure pencereleri kapatılır.
clc;            % komut satırı temizlenir.
%%                          MATLAB

x_0 = 5; %initial value 
syms s;             %sembolik değişken takımı oluşturma
X_s = x_0/(5 +s);   %laplace formu
X_t_continuous= ilaplace(X_s); %ters laplace alma

fplot([X_t_continuous]);
xlim([0 5])
grid on
xlabel('Time (sec)');
ylabel('position (meter)');

%%                     NUMERICAL SOLUTION
%                         SAYISAL ÇÖZÜM

dt = 0.001;     % adım sayısı

%initial and final time
tf = 5;
ti = 0;
t = [ti:dt:tf-dt]'; % ' ile transpozesi alınıp sütüna yazdırıldı

% iterasyon sayısı hesaplama
lenght_of_loop = (tf-ti)/dt;

%%                     BACKWARD DIFFERENCE
%               [x(k) - x(k -1)]/dt = -5.x(k-1)
X_t_b = zeros(lenght_of_loop,1); %ilk değerler sıfır


% initial condition update
X_t_b(1,1) = x_0;

for k = 2 : 1 : lenght_of_loop
    X_t_b(k,1) = X_t_b(k - 1,1)*(1 - 5*dt);
end

hold on 
plot (t,X_t_b);

%%                     FORWARD DIFFERENCE
%               [x(k+1) - x(k)]/dt = -5.x(k)
X_t_f = zeros(lenght_of_loop,1); %ilk değerler sıfır


% initial condition update
X_t_f(1,1) = x_0;

for k = 1 : 1 : lenght_of_loop - 1
    X_t_f(k + 1,1) = X_t_f(k,1)*(1 - 5*dt);
end

hold on 
plot (t,X_t_f);

%%                     CENTERED DIFFERENCE
%               [x(k+1) - x(k -1)]/(2.dt) = -5.x(k - 1)
X_t_c = zeros(lenght_of_loop,1); %ilk değerler sıfır


% initial condition update
X_t_c(1,1) = x_0;
X_t_c(2,1) = x_0 + (-5)*dt/10;
for k = 2 : 1 : lenght_of_loop - 1
    X_t_c(k + 1,1) = X_t_c(k-1,1)*(1 - 5*2*dt);
end

hold on 
plot (t,X_t_c);
legend('real','backward','forward','centered');