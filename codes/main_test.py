#Code by GVV Sharma
#July 19, 2020
#Released under GNU/GPL
#SER and BER simulation for 8-PSK 
#using complex symbols

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
from chest.LMSFuncs import LMS
from chest.ChannelGain import chan
from chest.ChannelParams import *


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
#For Collecting Pilot Frames
#	PilotFramesTx = []
	PilotFramesRx = []
#	PilotFrames = []
	#LMS Loop
	for i in range(0,pFrame):
		noise_comp = (np.random.normal(0,1,FrameSymbLen)+1j*np.random.normal(0,1,FrameSymbLen)) #AWGN for the frame
		FrameTxSymb = AllFramesSymbols[i,:]  #Transmitted frame 
		#Channel response for pilot
		FrameChanResp=np.convolve(FrameTxSymb,ChanGain,'same')

		FrameRxSymb = FrameChanResp +1/np.sqrt(snr[k])*noise_comp #Received frame with fading and noise
#		PilotFramesTx.append(FrameTxSymb)  #Transmitted Pilot Frames
		PilotFramesRx.append(FrameRxSymb)  #Received Pilot Frames

	PilotFramesRx = np.array(PilotFramesRx)
	#LMS estimation
#	c_LMS = LMS(PilotFrames, Ak)

	print(PilotFramesRx.size,FrameSymbLen*pFrame)
		
#	for i in range(pframe,nFrame):
	for i in range(0,nFrame):
		noise_comp = (np.random.normal(0,1,FrameSymbLen)+1j*np.random.normal(0,1,FrameSymbLen)) #AWGN for the frame
		FrameTxSymb = AllFramesSymbols[i,:]  #Transmitted frame 
		#Channel response for pilot
		FrameChanResp=np.convolve(FrameTxSymb,ChanGain,'same')

		FrameRxSymb = FrameChanResp +1/np.sqrt(snr[k])*noise_comp #Received frame with fading and noise
#		FrameRxSymb = FrameTxSymb +1/np.sqrt(snr[k])*noise_comp #Received frame with noise

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

		MACTxBits = AllFramesBits[i,3*FrameMACBegin:3*FramePayloadBegin]  #Transmitted frame bits
		MACBitsRxTemp=np.array(MACBitsRx).flatten()
#		if i==0:
#			print(i,MACBitsRxTemp)
#		print(MACBitsRxTemp.size)
#		print(MACTxBits.size,MACBitsRxTemp.size)
		MACFrameErrBits = MACTxBits-MACBitsRxTemp
#		print(i,MACFrameErr.size)
#
#		MACFrameBER = 1-len(np.where(MACFrameErr == 0)[0])/MACBitsLen
		MACFrameCorrect += len(np.where(MACFrameErrBits == 0)[0])
	#Evaluating SER
	MACSERSim.append(FrameMACSymbErr/(MACSymbsLen*nFrame))
	MACSERTheory.append(2*qfunc((np.sqrt(snr[k]))*np.sin(np.pi/8)))
	MACBER.append(1-MACFrameCorrect/(nFrame*MACBitsLen))
	#Received bitstream
#	brx=np.array(brx).flatten()
	#Evaluating BER
#	bit_diff = bits-brx
#	MACBER.append(1-len(np.where(bit_diff == 0)[0])/bitsimlen)

#print(AllFramesSymbols[0,:])
#print(AllFrames[0,:])
#print(symbols_comp[1])
##Bitstream size
#bitsimlen = 99999
#
##Symbol stream size
#simlen = bitsimlen //3
#
##Generating bitstream
#bits = bitstream(bitsimlen)
#
##Converting bits to Gray coded 8-PSK symbols
##Intermediate steps  required for converting list to
##numpy matrix
#symbols_lst = symb(bits)
#symbols = np.array(symbols_lst).T #Symbol vectors
#symbols_comp = symbols[0,:]+1j*symbols[1,:] #Equivalent complex symbols
#
#ser =[]
#ser_anal=[]
#ber = []
#
##SNRloop
#for k in range(0,snrlen):
#	received = []
#	t=0
#	#Complex noise
#	noise_comp = np.random.normal(0,1,simlen)+1j*np.random.normal(0,1,simlen)
#	#Generating complex received symbols
#	y_comp = np.sqrt(snr[k])*symbols_comp+noise_comp
#	brx = []
#	for i in range(simlen):
#		srx_comp = decode(y_comp[i]) #Received Symbol
#		brx.append(detect(srx_comp))  #Received Bits
#		if symbols_comp[i]==srx_comp:
#			t+=1; #Counting symbol errors
#	#Evaluating SER
#	ser.append(1-(t/33334.0))
#	ser_anal.append(2*qfunc((np.sqrt(snr[k]))*np.sin(np.pi/8)))
#	#Received bitstream
#	brx=np.array(brx).flatten()
#	#Evaluating BER
#	bit_diff = bits-brx
#	ber.append(1-len(np.where(bit_diff == 0)[0])/bitsimlen)
#
#
#
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
