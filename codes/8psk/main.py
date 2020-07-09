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
from bs import bitstream
#from mapping import mapping
from mapping_new import mapping
from bit2symb import symb
from mats import *
#from symbol import symb
#from received import rec


#Bitstream size
bitsimlen = 11
#Symbol stream size
simlen = bitsimlen //3

#Generating bitstream
bits = bitstream(11)

#Converting bits to Gray coded 8-PSK symbols
#Intermediate steps  required for converting list to
#numpy matrix
symbols_lst = symb(bits)
symbols_array = np.array(symbols_lst)
symbols = symbols_array[:,:,0].T

#Adding AWGN noise with 0 mean and unit variance
noise = np.random.normal(0,1,(2,simlen))
rx_vec = symbols+noise

print(s7)
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
