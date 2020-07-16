#Code by Krishnaja Kodali
#July  14, 2020

#Revised by GVV Sharma
#July  16, 2020

#released under GNU GPL
#Communication parameters

import numpy as np
import math


SNR_dB = 18 #Signal to noise ratio in dB
TimeSlot=2e-3 #Transmit time duration
Rs = 185e3 # symbol rate
N = 10 #channel filter length
P = 10000 #pilot symbols
#P = 156//3 #pilot symbols
L = 255//3 #payload
#L = 10000 #payload
SNR = 10**(SNR_dB/10)

a=np.array([1+0j,1/np.sqrt(2)+1j*1/np.sqrt(2) ,1j ,-1/np.sqrt(2)+1j*1/np.sqrt(2), -1 ,-1/np.sqrt(2)-1j*1/np.sqrt(2), -1j ,1/np.sqrt(2)-1j*1/np.sqrt(2)])

# Channel creation and channel modeling
Rsym = Rs; M = 8;                  # Input symbol rate
Rbit = Rsym * math.log2(M);      #Input bit rate
Nos = 1;                    # Oversampling factor

#Sampling period
ts = (1/Rsym) / Nos;

#Channel path gains
pg=np.array([0.9417 - 0.2214j ,-0.1596 - 0.0874j ,-0.0644 - 0.0163j, -0.0645 - 0.0387j, -0.0751 + 0.0467j])
##Channel path delays
pd=np.array([0, 2.0000e-06 ,4.0000e-06, 6.0000e-06, 8.0000e-06])/ts
