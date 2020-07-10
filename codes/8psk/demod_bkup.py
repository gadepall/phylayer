#Code by GVV Sharma
#July 9, 2020
#Released under GNU/GPL
#Detection for 8-PSK 
import numpy as np
#import mpmath as mp
#from symbol import symb
#from qfunc import qfunc
from mats import *

#Demodulating symbol from noisy received vector
def decode(vec):
	for i in range(8):
		y = A[i,:,:]@vec
#		print(y)
		if (y [0] >= 0) and (y[1] >= 0):
			return s[i,:]

#Extracting bits from demodulated symbols
def detect(vec):
	for i in range(8):
		if s[i,0]==vec[0] and s[i,1] == vec[1]:
			return gray[i,:]

#Demodulating symbol stream from received noisy  symbols
def rx_symb(mat):
	len = mat.shape[1]
	rx_symb_stream = []
	for i in range(len):
		rx_symb_stream.append(decode(mat[:,i]))
	return rx_symb_stream

#Getting received bit stream from demodulated symbols
def rx_bit(mat):
	len = mat.shape[1]
	rx_bit_stream = []
	for i in range(len):
		rx_bit_stream.append(detect(mat[:,i]))
	return rx_bit_stream
#			
#def rec():
#
#def rec():
#	symbol=[]
#	symbol=symb()
#	snr_db = np.linspace(0,9,10)
#	snrlen=10
#	err =[]
#	s_in,s_q =0,0
#	ber=[]
#	for k in range(0,snrlen):
#		snr = 10**(0.1*snr_db[k])
#		received = []
#		t=0
#		for i in range(len(symbol)):
#			if symbol[i] == "s0":
#				s_in = 1
#				s_q = 0
#			elif symbol[i] =="s1":
#				s_in = 1/np.sqrt(2)
#				s_q = 1/np.sqrt(2)
#			elif symbol[i] == "s2":
#				s_in = 0
#				s_q = 1
#			elif symbol[i] == "s3":
#				s_in = -1/np.sqrt(2)
#				s_q = 1/np.sqrt(2)
#			elif symbol[i]=="s4":
#				s_in=-1
#				s_q=0
#			elif symbol[i]=="s5":
#				s_in=-1/np.sqrt(2)
#				s_q=-1/np.sqrt(2)
#			elif symbol[i]=="s6":
#				s_in=0
#				s_q=-1
#			elif symbol[i]=="s7":
#				s_in=1/np.sqrt(2)
#				s_q=-1/np.sqrt(2)
#			noise1 = np.random.normal(0,1,1)
#			noise2 = np.random.normal(0,1,1)
#			y1 = mp.sqrt(6*snr)*s_in + noise1
#			y2 = mp.sqrt(6*snr)*s_q + noise2
#			if(y2+(np.sqrt(2)-1)*y1>0 and y2-(np.sqrt(2)-1)*y1<0):
#				received.append("s0")
#			elif(y2-(np.sqrt(2)-1)*y1>0 and y2-(np.sqrt(2)+1)*y1<0):
#				received.append("s1")
#			elif(y2-(np.sqrt(2)+1)*y1>0 and y2+(np.sqrt(2)+1)*y1>0):
#				received.append("s2")
#			elif(y2+(np.sqrt(2)-1)*y1>0 and y2+(np.sqrt(2)+1)*y1<0):
#				received.append("s3")
#
#			elif(y2+(np.sqrt(2)-1)*y1<0 and y2-(np.sqrt(2)-1)*y1>0):
#				received.append("s4")
#			elif(y2-(np.sqrt(2)+1)*y1>0 and y2-(np.sqrt(2)-1)*y1<0):
#				received.append("s5")
#			elif(y2-(np.sqrt(2)+1)*y1<0 and y2+(np.sqrt(2)+1)*y1<0):
#				received.append("s6")
#			elif(y2+(np.sqrt(2)-1)*y1<0 and y2+(np.sqrt(2)+1)*y1>0):
#				received.append("s7")
#			if symbol[i]==received[i]:
#				t+=1;
#		err.append(1-(t/33334.0))
#		ber.append(2*qfunc((mp.sqrt(6*snr))*np.sin(np.pi/8)))
#	return err,ber,snr_db
