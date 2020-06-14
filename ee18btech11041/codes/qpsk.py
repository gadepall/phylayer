from __future__ import division
import numpy as np
import mpmath as mp
import matplotlib.pyplot as plt

#if using termux
import subprocess
import shlex
#end if



def qfunc(x):
	return 0.5*mp.erfc(x/np.sqrt(2))

#Number of SNR samples 
snr_len = 10
#SNR values in dB
snr_db = np.linspace(0,9,10)
#Number of samples
sim_len = int(1e5)
#Simulated BER declaration		
err = []
#Analytical BER declaration
ber = []
temp=0
noise1 = np.random.normal(0,1,sim_len)
noise2=np.random.normal(0,1,sim_len)

#for SNR 0 to 10 dB

for i in range(0,snr_len):
	snr = 10**(0.1*snr_db[i])	#Received symbol in baseband
	rx = mp.sqrt(2*snr) + noise1
	ry = noise2
	temp=0
	for j in range (0,len(rx)):
	    if ((rx[j]>ry[j]) and (rx[j]>-ry[j])):
	    	temp=temp+1                
                				
	#calculating the total number of errors
	#err_n = np.size(err_ind)
	#calcuating the simulated BER
	err.append(1-temp/sim_len)
	#calculating the analytical BER
	ber.append(1-(1-qfunc(mp.sqrt(snr)))**2)
	
plt.semilogy(snr_db.T,ber,label='Analysis')
plt.semilogy(snr_db.T,err,'o',label='Sim')
plt.xlabel('SNR$\\left(\\frac{E_b}{N_0}\\right)$')
plt.ylabel('$P_e$')
plt.legend()
plt.grid()
#if using termux
plt.savefig('./figs/qpsk.pdf')
plt.savefig('./figs/qpsk.eps')
subprocess.run(shlex.split("termux-open ./figs/qpsk.pdf"))
#else
#plt.show()
