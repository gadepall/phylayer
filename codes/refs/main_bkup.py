#Code by GVV Sharma
#July 10, 2020
#Released under GNU/GPL
#SER and BER simulation for 8-PSK 

from __future__ import division
import random
import numpy as np
import mpmath as mp
import matplotlib.pyplot as plt
import cmath


#if using termux
import subprocess
import shlex
#end if

from qfunc import qfunc
from mod import *
from demod import *


#SNR range
snrlen=10

#SNR in dB
snr_db = range(snrlen)


#Bitstream size
bitsimlen = 9
#Symbol stream size
simlen = bitsimlen //3

#Generating bitstream
bits = bitstream(bitsimlen)

#Converting bits to Gray coded 8-PSK symbols
#Intermediate steps  required for converting list to
#numpy matrix
symbols_lst = symb(bits)

symbols = np.array(symbols_lst).T

ber= []
ser = []
#SNR Loop begins
for k in range(0,snrlen):
	snr = 10**(0.1*snr_db[k])
#Adding AWGN noise with 0 mean and unit variance
	noise = np.random.normal(0,1,(2,simlen))
	rx_vec = snr*symbols+noise

#Demodulating symbols
	rx_symb_stream = np.array(rx_symb(rx_vec)).T

#Detecting bits
	rx_bit_stream = (np.array(rx_bit(rx_symb_stream)).T).flatten()
	
#	#Computing SER
#	symb_diff = symbols-rx_symb_stream
#	ser.append(len(np.where(symb_diff == 0)[0])/simlen)
	#Computing BER
	bit_diff = bits-rx_bit_stream
	ber.append(1-len(np.where(bit_diff == 0)[0])/bitsimlen)
#	ere = bit_err.append(decode(mat[:,i]))
# = 
#print(ber)
print(symbols, symbols[0,1])
#print(bits,rx_bit_stream)
#print(bit_diff, zero_loc)
#print(bit_diff, zero_loc)
#print(bit_diff)
#symbols = symbols_array[:,:,0].T
#print(symbols)
#symbols_array = np.array(symbols_lst).T
#print(np.array(rx_symb(rx_vec)))
#print(rx_bit(rx_symb(rx_vec)))
#a = decode(rx_vec[:,0])
#print(rx_vec[:,0])
#rx_symb = decode(rx_vec[:,0])
#rx_bits = detect(rx_symb)
#print(decode(rx_vec[:,0]))
#print(rx_vec.shape)
#print(decode(rx_vec[:,0]), rx_bits)
#print(symbols[:,0],decode(rx_vec[:,0]))
#symbol=[]
#	symbol=symb()
#	snr_db = np.linspace(0,9,10)
#
#print(s[0,:,:], rx_vec[:,0], s@rx_vec[:,0])
#Detecting symbols

#print( bitstream(10))
#print(mapping(0,0,0))
#print(symbols, noise, symbols+noise)
#print(simlen)
#err=[]
#ber=[]
#snr_db=[]
#err,ber,snr_db=rec()
#
#
#plt.semilogy(snr_db.T,ber,label='Analysis')
#plt.semilogy(snr_db.T,err,'o',label='Sim')
#plt.xlabel('SNR$\\left(\\frac{E_b}{N_0}\\right)$')
#plt.ylabel('$P_e$')
#plt.legend()
#plt.grid()
##if using termux
#plt.savefig('./figs/ee18btech11012.pdf')
#plt.savefig('./figs/ee18btech11012_1.eps')
#subprocess.run(shlex.split('termux-open ./figs/ee18btech11012.pdf'))
