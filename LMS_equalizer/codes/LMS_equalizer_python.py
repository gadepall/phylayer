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
import math
from channel import chan

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
#L = 10000 #payload

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

##readsfrom tex file command File_object.readline(n)
##pg=dlmread('path_gains.dat',',',[0,0,0,4])

##Channel taps
pd=np.array([0, 2.0000e-06 ,4.0000e-06, 6.0000e-06, 8.0000e-06])/ts
#Channel coefficients
g = chan(pg,pd,N)

#Channel response for pilot
Rk=np.convolve(Ak,g,'same')

#AWGN for pilot
noise = (1/np.sqrt(2))*(np.random.randn(len(Rk)) + 1j*np.random.randn(len(Rk))) #Initial noise vector
P_s =np.var(Rk)  #Signal power
P_n = np.var(noise)  #Noise power

# Defining noise scaling factor based on the desired SNR:
noise_scaling_factor = np.sqrt((P_s/P_n)/10**(SNR/10)) 

#Adding AWGN for pilot
Rk_noisy=Rk+noise*noise_scaling_factor # Received signal
print(len(Rk_noisy))

#Received Pilot channel output I and Q
rkr=np.real(Rk)
rki=np.imag(Rk)

#Received Pilot symbols I and Q
noisy_rkr=np.real(Rk_noisy)
noisy_rki=np.imag(Rk_noisy)


#Channel response for payload
pay_Rk=np.convolve(payload,g,'same')

#AWGN for payload
noise = (1/np.sqrt(2))*(np.random.randn(len(pay_Rk)) + 1j*np.random.randn(len(pay_Rk))) #Initial noise vector

#Adding AWGN for payload
pay_Rk_noisy=pay_Rk+noise*noise_scaling_factor # Received signal


#Received payload channel output I and Q
pay_rkr=np.real(pay_Rk)
pay_rki=np.imag(pay_Rk)


#Received payload symbols I and Q
pay_rkr_noisy=np.real(pay_Rk_noisy)
pay_rki_noisy=np.imag(pay_Rk_noisy)



#LMS estimation
c_LMS = LMS(Rk_noisy, Ak)
#LMS equalization

#Equalizing pilot
y_LMS_pilot=signal.lfilter(np.ndarray.flatten(c_LMS),1,np.ndarray.flatten(Rk_noisy))

Lr=np.real(y_LMS_pilot)
Li=np.imag(y_LMS_pilot)

#Equalizing payload
y_LMS_payload=signal.lfilter(np.ndarray.flatten(c_LMS),1,np.ndarray.flatten(pay_Rk_noisy))

pay_Lr=np.real(y_LMS_payload)
pay_Li=np.imag(y_LMS_payload)


#Following plots related to  payload


#Plotting channel output
#plt.scatter(pay_rkr,pay_rki)

##Plotting payload received symbols (Channel output + AWGN)
plt.scatter(pay_rkr_noisy,pay_rki_noisy)
#
## Plotting payload LMS_estimate
plt.scatter(pay_Lr,pay_Li)
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
