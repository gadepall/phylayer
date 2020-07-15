#Code by Krishnaja Kodali
#July  14, 2020

#Revised by GVV Sharma
#July  15, 2020

#released under GNU GPL
#Testing the LMS algrorithm

import numpy as np
import matplotlib.pyplot as plt
import math
import cmath
import random
from LMS_func import LMS
#if using termux
import subprocess
import shlex
#end if


TimeSlot=2e-3 #Transmit time duration
SNR = 18 #Signal to noise ratio
Rs = 185e3 # symbol rate
a=np.array([1+0j,1/math.sqrt(2)+1j*1/math.sqrt(2) ,1j ,-1/math.sqrt(2)+1j*1/math.sqrt(2), -1 ,-1/math.sqrt(2)-1j*1/math.sqrt(2), -1j ,1/math.sqrt(2)-1j*1/math.sqrt(2)])

Ak=[]
for i in range(10000):
	Ak.append(0)

for ii in range(10000):
	Ak[ii] = a[random.randint(0,7)]
ar=[x.real for x in a]
ai=[x.imag for x in a]
plt.scatter(ar,ai)
#plt.title('8-PSK')
#plt.grid()
##if using termux
#plt.savefig('./figs/lms_test_symb.pdf')
#plt.savefig('./figs/lms_test_symb.eps')
#plt.show()


# Channel creation and channel modelling
Rsym = Rs; M = 8;                  # Input symbol rate
Rbit = Rsym * math.log2(M);      #Input bit rate
Nos = 1;                    # Oversampling factor
ts = (1/Rsym) / Nos;
pg=np.array([0.9417 - 0.2214j ,-0.1596 - 0.0874j ,-0.0644 - 0.0163j, -0.0645 - 0.0387j, -0.0751 + 0.0467j])

#readsfrom tex file command File_object.readline(n)
#pg=dlmread('path_gains.dat',',',[0,0,0,4])
pd=np.array([0, 2.0000e-06 ,4.0000e-06, 6.0000e-06, 8.0000e-06])/ts
g=[]
for n in range(0,1600):
     g.append(0)
     for k in range(5):
         g[n]=g[n]+pg[k]*np.sinc(pd[k]-n+800)
Rk=np.convolve(Ak,g,'same')
noise = (1/math.sqrt(2))*(np.random.randn(len(Rk)) + 1j*np.random.randn(len(Rk))) #Initial noise vector
P_s =np.var(Rk)  #Signal power
P_n = np.var(noise)  #Noise power
# Defining noise scaling factor based on the desired SNR:
noise_scaling_factor = math.sqrt((P_s/P_n)/10**(SNR/10)) 
Rk_noisy=Rk+noise*noise_scaling_factor # Received signal
print(len(Rk_noisy))
rkr=[x.real for x in Rk]
rki=[x.imag for x in Rk]
#plt.scatter(rkr,rki)
#plt.title('Recieved constellation')
#plt.grid()
#plt.savefig('./figs/lms_test_rx.pdf')
#plt.savefig('./figs/lms_test_rx.eps')
#plt.show()

#LMS algorithm
y_LMS = LMS(Rk_noisy, Ak, Rk)

Lr=[x.real for x in y_LMS]
Li=[x.imag for x in y_LMS]


# Plotting
plt.scatter(Lr,Li)
plt.title('LMS equalized constellation')
plt.grid()
plt.show()
#

##if using termux
plt.savefig('./figs/lms_test.pdf')
plt.savefig('./figs/lms_test.eps')
#subprocess.run(shlex.split("termux-open ./figs/lms_test_rx.pdf"))
subprocess.run(shlex.split("termux-open ./figs/lms_test.pdf"))
#else
#plt.show()
