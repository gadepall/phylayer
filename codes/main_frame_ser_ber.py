#Code by GVV Sharma
#July 19, 2020
#Released under GNU/GPL
#SER and BER simulation for 8-PSK MAC Bits

import numpy as np
import matplotlib.pyplot as plt


#if using termux
import subprocess
import shlex
#end if

#Importing custom functions
from EightPSK.mod import *
from EightPSK.demod import *
from EightPSK.mats import *
from frame.frametx import *
from frame.FrameParams import *


#SNR range
snrlen=10

#SNR in dB and actual per bit 
#(Check Proakis for factor of 6)
snr_db = np.linspace(0,snrlen,snrlen)
snr = 6*10**(0.1*snr_db)

#Initializing all Frames in Bits and 8PSK Symbols
AllFramesBits = np.zeros((nFrame,FrameLen))
AllFramesSymbols = np.zeros((nFrame,FrameSymbLen))+1j*np.zeros((nFrame,FrameSymbLen))

#Generating all the Frames in Bits and 8PSK Symbols
for i in range(0,nFrame):
	
	AllFramesBits[i,:]=FrameGen(i)
	AllFramesSymbols[i,:] = CompSymb(AllFramesBits[i,:])

#print(AllFramesSymbols.shape)

MACSERSim =[]
MACSERTheory=[]
MACBER = []

#SNR Loop for computing the overall SER and BER
for k in range(0,snrlen):
#Computing the SER and BER per frame
	FrameMACSymbErr = 0
	MACFrameCorrect = 0
	for i in range(0,nFrame):
		noise_comp = np.random.normal(0,1,FrameSymbLen)+1j*np.random.normal(0,1,FrameSymbLen) #AWGN for the frame
		FrameTxSymb = AllFramesSymbols[i,:]  #Transmitted frame 
		FrameRxSymb = FrameTxSymb +1/np.sqrt(snr[k])*noise_comp #Received frame with noise

		FrameMACTxSymb = FrameTxSymb[FrameMACBegin:FramePayloadBegin] #MAC part of the transmittedframe
		FrameMACRxSymb = FrameRxSymb[FrameMACBegin:FramePayloadBegin] #MAC part of the received frame
		FramePayloadRxSymb = FrameRxSymb[FramePayloadBegin:FrameSymbLen] #Payload part of the received frame
		#MAC Detection
		MACBitsRx = []
		for m in range(MACSymbsLen):
			MACSymbRx = decode(FrameMACRxSymb[m]) #Demodulated MAC Symbol
			MACBitsRx.append(detect(MACSymbRx))  #Demodulated MAC bits per symbol
			if MACSymbRx!=FrameMACTxSymb[m]:
				FrameMACSymbErr +=1; #Counting symbol errors

		MACTxBits = AllFramesBits[i,3*FrameMACBegin:3*FramePayloadBegin]  #Transmitted MAC frame bits
		MACBitsRxTemp=np.array(MACBitsRx).flatten() #Received MAC Frame Bits
		MACFrameErrBits = MACTxBits-MACBitsRxTemp 
		MACFrameCorrect += len(np.where(MACFrameErrBits == 0)[0]) #Checking for number of correct bits
	#Evaluating SER and BER
	MACSERSim.append(FrameMACSymbErr/(MACSymbsLen*nFrame)) #Simulated SER
	MACSERTheory.append(2*qfunc((np.sqrt(snr[k]))*np.sin(np.pi/8))) #Analytical SER
	MACBER.append(1-MACFrameCorrect/(nFrame*MACBitsLen)) #Simulatd BER

#Plots
plt.semilogy(snr_db,MACSERTheory,label='MAC SER Analysis')
plt.semilogy(snr_db,MACSERSim,'o',label='MAC SER Sim')
plt.semilogy(snr_db,MACBER,label='MAC BER Sim')
plt.xlabel('SNR')
plt.ylabel('$P_e$')
plt.legend()
plt.grid()

#if using termux
plt.savefig('./figs/mac_ser_ber.pdf')
plt.savefig('./figs/mac_ser_ber.eps')
subprocess.run(shlex.split('termux-open ./figs/mac_ser_ber.pdf'))
