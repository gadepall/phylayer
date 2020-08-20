#Code by Krishnaja Kodali
#July  14, 2020

#Revised by GVV Sharma
#July  15, 2020

#released under GNU GPL
#The LMS algrorithm

import numpy as np

def LMS(Rk_noisy, Ak):
	framelen= len(Rk_noisy)
	#Begin LMS algorithm
	Ek=[]
	hTap=11 #Channel Taps
	beta = 0.001 # step-size of the algorithm
	c_LMS = np.zeros([hTap,1]) #equalizer coefficients, initializations

	Ek = np.zeros((framelen-int((hTap-1)/2)-1))+1j*np.zeros((framelen-int((hTap-1)/2)-1))
	print(Ek.shape)
	for i in range(int((hTap-1)/2),framelen-int((hTap-1)/2)-1):
		rkt =Rk_noisy[i-int((hTap-1)/2):i+int((hTap-1)/2)+1] 
		rk=np.flipud(rkt.reshape(-1,1)) # recieved signal vector
		Ek[i] = Ak[i] - np.transpose(c_LMS)@rk #Error signal, we assume a known symbol sequence
		c_LMS = c_LMS+beta*Ek[i]*(np.conj(rk)) # LMS update !

	return c_LMS #returning estimated channel coefficients



def LMSPilot(PilotFramesRx,PilotFramesTx):
	#Begin LMS algorithm
	PilotFramesLen = len(PilotFramesRx)
#	print(PilotFramesRx.shape)
	Ek=[]
	hTap=11 #Channel Taps
	beta = 0.001 # step-size of the algorithm
	c_LMS = np.zeros([hTap,1]) #equalizer coefficients, initializations

	Ek = np.zeros((PilotFramesLen-int((hTap-1)/2)-1))+1j*np.zeros((PilotFramesLen-int((hTap-1)/2)-1))
#	print(Ek.shape)
	for i in range(int((hTap-1)/2),PilotFramesLen-int((hTap-1)/2)-1):
		rkt =PilotFramesRx[i-int((hTap-1)/2):i+int((hTap-1)/2)+1] 
		rk=np.flipud(rkt.reshape(-1,1)) # recieved signal vector
#		Ek[i] = Ak[i] - np.transpose(c_LMS)@rk #Error signal, we assume a known symbol sequence
		Ek[i] = PilotFramesTx[i] - np.transpose(c_LMS)@rk #Error signal, we assume a known symbol sequence
		c_LMS = c_LMS+beta*Ek[i]*(np.conj(rk)) # LMS update !

	return c_LMS #returning estimated channel coefficients


