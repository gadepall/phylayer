function y=channel(x,offset,phi0,snr)
sigma=sqrt(1/2*10^(-snr/10));
i=(1:length(x));
phaseoffset=exp(1i*(i*offset+phi0));
temp = exp(1i*x*pi*2/8);
y=temp.*phaseoffset+sigma*(randn(1,length(x))+1i*randn(1,length(x)));
