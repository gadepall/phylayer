#Code by Krishnaja Kodali
#July  14, 2020

#Revised by GVV Sharma
#July  15, 2020

#released under GNU GPL
#Testing the LMS algrorithm

import numpy as np
import matplotlib.pyplot as plt
import random
from scipy import signal
from LMS_func import LMS

#if using termux
import subprocess
import shlex
#end if


TimeSlot=2e-3 #Transmit time duration
SNR = 18 #Signal to noise ratio
Rs = 185e3 # symbol rate
N = 10 #channel filter length
P = 10000 #pilot symbols
#P = 156//3 #pilot symbols
L = 255//3 #payload

a=np.array([1+0j,1/np.sqrt(2)+1j*1/np.sqrt(2) ,1j ,-1/np.sqrt(2)+1j*1/np.sqrt(2), -1 ,-1/np.sqrt(2)-1j*1/np.sqrt(2), -1j ,1/np.sqrt(2)-1j*1/np.sqrt(2)])


Ak=np.zeros(P)+1j*np.zeros(P)
payload=np.zeros(L)+1j*np.zeros(L)

#Pilot Symbols
for ii in range(P):
	Ak[ii] = a[random.randint(0,7)]

Akr = np.real(Ak)
Aki = np.imag(Ak)

#Payload Symbols
for ii in range(L):
	payload[ii] = a[random.randint(0,7)]


# Channel creation and channel modelling
Rsym = Rs; M = 8;                  # Input symbol rate
Rbit = Rsym * math.log2(M);      #Input bit rate
Nos = 1;                    # Oversampling factor
ts = (1/Rsym) / Nos;
pg=np.array([0.9417 - 0.2214j ,-0.1596 - 0.0874j ,-0.0644 - 0.0163j, -0.0645 - 0.0387j, -0.0751 + 0.0467j])

#readsfrom tex file command File_object.readline(n)
#pg=dlmread('path_gains.dat',',',[0,0,0,4])
#Channel taps
pd=np.array([0, 2.0000e-06 ,4.0000e-06, 6.0000e-06, 8.0000e-06])/ts
g=[]
for n in range(0,N):
     g.append(0)
     for k in range(5):
         g[n]=g[n]+pg[k]*np.sinc(pd[k]-n+N/2)

#Channel response
Rk=np.convolve(Ak,g,'same')
noise = (1/np.sqrt(2))*(np.random.randn(len(Rk)) + 1j*np.random.randn(len(Rk))) #Initial noise vector
P_s =np.var(Rk)  #Signal power
P_n = np.var(noise)  #Noise power

# Defining noise scaling factor based on the desired SNR:
noise_scaling_factor = np.sqrt((P_s/P_n)/10**(SNR/10)) 

#Adding AWGN
Rk_noisy=Rk+noise*noise_scaling_factor # Received signal
print(len(Rk_noisy))

rkr=np.real(Rk)
rki=np.imag(Rk)

noisy_rkr=np.real(Rk_noisy)
noisy_rki=np.imag(Rk_noisy)


pay_Rk=np.convolve(payload,g,'same')
noise = (1/np.sqrt(2))*(np.random.randn(len(pay_Rk)) + 1j*np.random.randn(len(pay_Rk))) #Initial noise vector
pay_Rk_noisy=pay_Rk+noise*noise_scaling_factor # Received signal
pay_rkr=[x.real for x in pay_Rk]
pay_rki=[x.imag for x in pay_Rk]



#LMS estimation
c_LMS = LMS(Rk_noisy, Ak)
#LMS equalization

#Equalizing pilot
y_LMS=signal.lfilter(np.ndarray.flatten(c_LMS),1,np.ndarray.flatten(Rk_noisy))

#Equalizing payload
#y_LMS=signal.lfilter(np.ndarray.flatten(c_LMS),1,np.ndarray.flatten(pay_Rk_noisy))

#Lr=[x.real for x in y_LMS]
#Li=[x.imag for x in y_LMS]
Lr=np.real(y_LMS)
Li=np.imag(y_LMS)


#Following plots related to pilot

#Plotting transmitted symbols
plt.scatter(Akr,Aki)

#Plotting channel output
#plt.scatter(rkr,rki)

#Plotting received symbols (Channel output + AWGN)
plt.scatter(noisy_rkr,noisy_rki)
#plt.title('Recieved constellation')
#plt.grid()

# Plotting LMS_estimate
plt.scatter(Lr,Li)
#End plots related to pilot

#Plot parameters
plt.title('LMS equalized constellation')
plt.grid()
plt.show()
#
##if using termux
plt.savefig('./figs/lms_test.pdf')
plt.savefig('./figs/lms_test.eps')
subprocess.run(shlex.split("termux-open ./figs/lms_test.pdf"))
#else
#plt.show()
