#Code by GVV Sharma
#August 1, 2020

#function m_psk=mapping(M,dataSym)
%M=8;
#    I=cos_comp((dataSym-1)/M*2*pi);
#    Q=sin((dataSym-1)/M*2*pi);
#    m_psk=(I+1i*Q);
#end
#Converts bits to 8-PSK symbols using gray code
function PSKSymb = mapping(b0,b1,b2,s_comp)
	if (b0 == 0 ) && (  b1 == 0 ) && (  b2 == 0)
		PSKSymb =  s_comp(1,:);
	elseif (b0 == 0 ) && (  b1 == 0 ) && (  b2 == 1)
		PSKSymb =  s_comp(2,:);
	elseif (b0 == 0 ) && (  b1 == 1 ) && (  b2 == 1)
		PSKSymb =  s_comp(3,:);
	elseif (b0 == 0 ) && (  b1 == 1 ) && (  b2 == 0)
		PSKSymb =  s_comp(4,:);
	elseif( b0 == 1 ) && (  b1 == 1 ) && (  b2 == 0)
		PSKSymb =  s_comp(5,:);
	elseif(b0==1 ) && (  b1 == 1 ) && (  b2 == 1)
		PSKSymb =  s_comp(6,:);
	elseif(b0==1 ) && (  b1 == 0 ) && (  b2 == 1)
		PSKSymb =  s_comp(7,:);
	elseif(b0==1 ) && (  b1 == 0 ) && (  b2 == 0)
		PSKSymb =  s_comp(8,:);

end
