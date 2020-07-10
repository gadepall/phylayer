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
from mapping import mapping
#from symbol import symb
from mod import symb
from demod import decode
#from received import rec
from mats import *

err=[]
ber=[]
snr_db=[]
#err,ber,snr_db=rec()

#SNR range
snrlen=10

#SNR in dB
snr_db = range(snrlen)

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

err =[]
#s_in,s_q =0,0
ber=[]
for k in range(0,snrlen):
	snr = 10**(0.1*snr_db[k])
	received = []
	t=0
	noise = np.random.normal(0,1,(2,simlen))
	y = mp.sqrt(6*snr)*symbols+noise
	for i in range(simlen):
		srx = decode(y[:,i])
		if symbols[0,i]==srx[0] and symbols[1,i]==srx[1]:
			t+=1;
	err.append(1-(t/33334.0))
	ber.append(2*qfunc((mp.sqrt(6*snr))*np.sin(np.pi/8)))

plt.semilogy(snr_db,ber,label='Analysis')
plt.semilogy(snr_db,err,'o',label='Sim')
plt.xlabel('SNR$\\left(\\frac{E_b}{N_0}\\right)$')
plt.ylabel('$P_e$')
plt.legend()
plt.grid()
#if using termux
plt.savefig('./figs/ee18btech11012.pdf')
plt.savefig('./figs/ee18btech11012.eps')
subprocess.run(shlex.split('termux-open ./figs/ee18btech11012.pdf'))
