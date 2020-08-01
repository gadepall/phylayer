#Code by GVV Sharma
#August 1, 2020

#8PSK constellation 
#Demodulation matrx


#Generating constellation points
s = zeros(8,2);
s_comp = zeros(8,1);
for i =1:8
	s(i,:) = [cos(i*2*pi/8) sin(i*2*pi/8)]; #vector
	s_comp(i) = s(i,1)+1j*s(i,2); #equivalent complex number
end
#
#Generating demodulation matrix
A = zeros(2,2,8);
A(:,:,1) = [sqrt(2)-1 1; sqrt(2)-1 -1];
A(:,:,2) = [sqrt(2)+1 -1; -(sqrt(2)-1) 1];
A(:,:,3) = [-(sqrt(2)+1) 1; sqrt(2)+1 1];
A(:,:,4) = [sqrt(2)-1 1; -(sqrt(2)+1) -1];
A(:,:,5) = [-(sqrt(2)-1) -1; -(sqrt(2)-1) 1];
A(:,:,6) = [-(sqrt(2)+1) 1; sqrt(2)-1 -1];
A(:,:,7) = [sqrt(2)+1 -1; -(sqrt(2)+1) -1];
A(:,:,8) = [-(sqrt(2)-1) -1; sqrt(2)+1 1];

#Gray code
gray = zeros(8,3);
gray(1,:) = [0 0 0];
gray(2,:) = [0 0 1];
gray(3,:) = [0 1 1];
gray(4,:) = [0 1 0];
gray(5,:) = [1 1 0];
gray(6,:) = [1 1 1];
gray(7,:) = [1 0 1];
gray(8,:) = [1 0 0];
#
#gray
#
##Q-function
#def qfunc(x):
#	return 0.5*special.erfc(x/sqrt(2
