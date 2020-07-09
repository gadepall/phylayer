#Code by GVV Sharma
#July 9, 2020
#Released under GNU/GPL
#Converts bits to 8-PSK symbols using gray code
import numpy as np
def mapping(b0,b1,b2):
	s = np.zeros((2,1))
	if (b0 == 0 and b1 == 0 and b2 == 0):
		s[0] = 1
		s[1] = 0
		return s;
	elif (b0 == 0 and b1 == 0 and b2 == 1):
		s[0] = 1/np.sqrt(2)
		s[1] = 1/np.sqrt(2)
		return s;
	elif (b0 == 0 and b1 == 1 and b2 == 1):
		s[0] = 0
		s[1] = 1
		return s;
	elif (b0 == 0 and b1 == 1 and b2 == 0):
		s[0] = -1/np.sqrt(2)
		s[1] = 1/np.sqrt(2)
		return s;
	elif( b0 == 1 and b1 == 1 and b2 == 0):
		s[0]=-1
		s[1]=0
		return s;
	elif(b0==1 and b1 == 1 and b2 == 1):
		s[0]=-1/np.sqrt(2)
		s[1]=-1/np.sqrt(2)
		return s;
	elif(b0==1 and b1 == 0 and b2 == 1):
		s[0]=0
		s[1]=-1
		return s;
	elif(b0==1 and b1 == 0 and b2 == 0):
		s[0]=1/np.sqrt(2)
		s[1]=-1/np.sqrt(2)
		return s;
