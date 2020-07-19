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

#SNR Loop for computing the overall SER and BER
for k in range(0,snrlen):
#Computing the SER and BER per frame
	for i in range(0,nFrame):
		noise_comp = np.random.normal(0,1,FrameLen)+1j*np.random.normal(0,1,FrameLen) #AWGN for the frame
		FrameRxSymb = AllFramesSymbols[i,:] +1/np.sqrt(snr[k])*noise_comp #Received frame with noise
		FrameMACRxSymb = FrameRxSymb[FrameMACBegin:FramePayloadBegin] #MAC part of the received frame
		FramePayloadRxSymb = FrameRxSymb[FramePayloadBegin:FrameSymbLen] #Payload part of the received frame
		#MAC Detection
	received = []
	t=0
	#Complex noise
	#Generating complex received symbols
	
	brx = []
	for i in range(FrameLen):
		srx_comp = decode(y_comp[i]) #Received Symbol
		brx.append(detect(srx_comp))  #Received Bits
		if symbols_comp[i]==srx_comp:
			t+=1; #Counting symbol errors
	#Evaluating SER
	ser.append(1-(t/33334.0))
	ser_anal.append(2*qfunc((np.sqrt(snr[k]))*np.sin(np.pi/8)))
	#Received bitstream
	brx=np.array(brx).flatten()
	#Evaluating BER
	bit_diff = bits-brx
	ber.append(1-len(np.where(bit_diff == 0)[0])/bitsimlen)

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
##Plots
#plt.semilogy(snr_db,ser_anal,label='SER Analysis')
#plt.semilogy(snr_db,ser,'o',label='SER Sim')
#plt.semilogy(snr_db,ber,label='BER Sim')
#plt.xlabel('SNR$\\left(\\frac{E_b}{N_0}\\right)$')
#plt.ylabel('$P_e$')
#plt.legend()
#plt.grid()
#
##if using termux
#plt.savefig('./figs/ser_ber.pdf')
#plt.savefig('./figs/ser_ber.eps')
#subprocess.run(shlex.split('termux-open ./figs/ser_ber.pdf'))
