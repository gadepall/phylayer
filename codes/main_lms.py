#Code by Krishnaja Kodali
#July  14, 2020

#Revised by GVV Sharma
#July  15, 2020
#July 20, 2020
#released under GNU GPL
#Testing the LMS algrorithm by comparing the transmitted
#and received constellation

#Global
import numpy as np
import matplotlib.pyplot as plt
import random
import math
from scipy import signal

#Local
from chest.LMSFuncs import LMS
from chest.ChannelGain import chan
from chest.ChannelParams import *

#if using termux
import subprocess
import shlex
#end if

SNRdB = 18 #Signal to noise ratio in dB
P = 10000
L = 255//3 #payload
SNR = 10**(SNRdB/10)
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

#Channel coefficients
g = chan(PathGains,PathDelays,ChannelFilterLen)

#Channel response for pilot
Rk=np.convolve(Ak,g,'same')
print(len(Rk),len(Ak),len(g))
#AWGN for pilot
noise = (1/np.sqrt(2))*(np.random.randn(len(Rk)) + 1j*np.random.randn(len(Rk))) #Initial noise vector

#Adding AWGN for pilot
Rk_noisy=Rk+1/np.sqrt(SNR)*noise # Received signal
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
pay_Rk_noisy=pay_Rk+1/np.sqrt(SNR)*noise # Received signal

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
#plt.show()
#
##if using termux
plt.savefig('./figs/lms_constellation.pdf')
plt.savefig('./figs/lms_constellation.eps')
subprocess.run(shlex.split("termux-open ./figs/lms_constellation.pdf"))
#else
#plt.show()
