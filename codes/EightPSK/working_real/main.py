#Code by GVV Sharma
#July 10, 2020
#Released under GNU/GPL
#SER and BER simulation for 8-PSK 

import numpy as np
import matplotlib.pyplot as plt


#if using termux
import subprocess
import shlex
#end if

#Importing custom functions
from mod import *
from demod import *
from mats import *


#SNR range
snrlen=10

#SNR in dB and actual per bit 
#(Check Proakis for factor of 6)
snr_db = np.linspace(0,snrlen,snrlen)
snr = 6*10**(0.1*snr_db)

#Bitstream size
bitsimlen = 99999

#Symbol stream size
simlen = bitsimlen //3

#Generating bitstream
bits = bitstream(bitsimlen)

#Converting bits to Gray coded 8-PSK symbols
#Intermediate steps  required for converting list to
#numpy matrix
symbols_lst = symb(bits)
symbols = np.array(symbols_lst).T

ser =[]
ser_anal=[]
ber = []

#SNRloop
for k in range(0,snrlen):
	received = []
	t=0
	noise = np.random.normal(0,1,(2,simlen))
	y = np.sqrt(snr[k])*symbols+noise
	brx = []
	for i in range(simlen):
		srx = decode(y[:,i]) #Received Symbol
		brx.append(detect(srx))  #Received Bits
		if symbols[0,i]==srx[0] and symbols[1,i]==srx[1]:
			t+=1; #Counting symbol errors
	#Evaluating SER
	ser.append(1-(t/33334.0))
	ser_anal.append(2*qfunc((np.sqrt(snr[k]))*np.sin(np.pi/8)))
	#Received bitstream
	brx=np.array(brx).flatten()
	#Evaluating BER
	bit_diff = bits-brx
	ber.append(1-len(np.where(bit_diff == 0)[0])/bitsimlen)



#Plots
plt.semilogy(snr_db,ser_anal,label='SER Analysis')
plt.semilogy(snr_db,ser,'o',label='SER Sim')
plt.semilogy(snr_db,ber,label='BER Sim')
plt.xlabel('SNR$\\left(\\frac{E_b}{N_0}\\right)$')
plt.ylabel('$P_e$')
plt.legend()
plt.grid()

#if using termux
plt.savefig('./figs/ee18btech11012.pdf')
plt.savefig('./figs/ee18btech11012.eps')
subprocess.run(shlex.split('termux-open ./figs/ee18btech11012.pdf'))
