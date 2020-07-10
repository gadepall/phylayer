import mpmath as mp
import numpy as np
from scipy import special

def qfunc(x):
	return 0.5*special.erfc(x/np.sqrt(2))
#	return 0.5*mp.erfc(x/np.sqrt(2))
