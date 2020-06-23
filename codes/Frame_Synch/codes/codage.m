function Y=codage(b,Scramb)
G=def_G();
Y=mod(b(1:5)*G,2);
Y=kron(Y,[1 1]);
b6=kron(ones(1,16),[0  b(6)]);
Y=mod(Y+b6,2);
%Scrambling 
Y=xor(Y,Scramb);

Y=2*Y-1;
