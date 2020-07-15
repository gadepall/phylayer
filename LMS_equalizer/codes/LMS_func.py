#Code by Krishnaja Kodali
#July  14, 2020

#Revised by GVV Sharma
#July  15, 2020

#released under GNU GPL
#The LMS algrorithm

import numpy as np

def LMS(Rk_noisy, Ak):
#def LMS(Rk_noisy, Ak, Rk):
	#Begin LMS algorithm
	Ek=[]
	hTap=11 #Channel Taps
	beta = 0.001 # step-size of the algorithm
	c_LMS = np.zeros([hTap,1]) #equalizer coefficients, initializations

	for i in range(0,len(Rk_noisy)-int((hTap-1)/2)-1):
		Ek.append(0)
	for i in range(int((hTap-1)/2),len(Rk_noisy)-int((hTap-1)/2)-1):
		rkt =Rk_noisy[i-int((hTap-1)/2):i+int((hTap-1)/2)+1] 
		rk=np.flipud(rkt.reshape(-1,1)) # recieved signal vector
		Ek[i] = Ak[i] - np.matmul(np.transpose(c_LMS),rk) #Error signal, we assume a known symbol sequence
		c_LMS = np.add(c_LMS,beta*Ek[i]*(np.conj(rk))) # LMS update !

#	y_LMS=signal.lfilter(np.ndarray.flatten(c_LMS),1,np.ndarray.flatten(Rk))
	#End LMS algorithm
#	return y_LMS
	return c_LMS
