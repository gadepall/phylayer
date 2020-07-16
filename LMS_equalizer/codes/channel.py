#Code by Krishnaja Kodali
#July  14, 2020

#Revised by GVV Sharma
#July  15, 2020

#released under GNU GPL
#free to use for anything

#Returns Channel  coefficients
#Takes channel taps and path delay as input

import numpy as np
#from params import *

#Channel gain
def chan(pg,pd,N):
	g=np.zeros(N)+1j*np.zeros(N)
	K = len(pd)
	for n in range(0,N):
	     for k in range(K):
	         g[n]=g[n]+pg[k]*np.sinc(pd[k]-n)

	return g

#Noise scaling factor 
#def noise_power(Rk,noise,SNR):
#	P_s =np.var(Rk)  #Signal power
#	P_n = np.var(noise)  #Noise power
#
#	# Defining noise scaling factor based on the desired SNR:
#	noise_scaling_factor = np.sqrt((P_s/P_n)/10**(SNR/10)) 
#	return  noise_scaling_factor
##
