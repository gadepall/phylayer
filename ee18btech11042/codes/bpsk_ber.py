#if using termux
import subprocess
import shlex
#end if
import numpy as np
import math
import matplotlib.pyplot as plt
def qfunc(x):
	return 0.5*math.erfc(x/math.sqrt(2))

# SNR values in db
SNR_db = np.linspace(0,9,10)
# SNR values
SNR = 10**(0.1*SNR_db)
#simualtion ber declaration
err_sim = []
#No.of samples
simlen = int(1e5)
#analytical ber declaratiom
err_ana = []

for i in range(0,len(SNR)):
	#AWGN with mean 0 and variance 1
	n1 = np.random.normal(0,1,simlen)
	
	# received  signal
	rx = math.sqrt(SNR[i]) + n1
	#Storing indices of rx<0
	err_ind = np.nonzero(rx < 0)
	#calculating simulation error
	err_sim.append((np.size(err_ind))/simlen)
	#calculating analytical error
	err_ana.append(qfunc(math.sqrt(SNR[i])))
	
plt.semilogy(SNR_db.T,err_ana,label='Analysis')
plt.semilogy(SNR_db.T,err_sim,'o',label='Sim')
plt.xlabel('SNR$\\left(\\frac{E_b}{N_o}\\right)$')
plt.ylabel('$P_e$')
plt.legend()
plt.grid()
#if using termux
plt.savefig('./figs/ee18btech11042/ee18btech11042.pdf')
plt.savefig('./figs/ee18btech11042/ee18btech11042_1.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11042/ee18btech11042.pdf"))
#else
#plt.show()
plt.show()
