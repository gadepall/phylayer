clc;
clear;
close all;

function w = bitstream(n)
	w = randi([0 1],n,1);
end

TimeSlot=2e-3; %Transmit time duration
SNR = 1; %Signal to noise ratio
Rs = 123e3; % symbol rate %53.34
%scaling_factor = 10e6;
M=8;
%Nf = 5; % MMSE filter length
L = 5 ; % Channel filter length
%N = 1e4;   % Number of symbols
%BitsnrdB=0:1:15;  % SNR in dB
BitsnrdB=14:1:15;  % SNR in dB
kk=log2(M);   
SymbolSNRdB = BitsnrdB+10*log10(kk);   % Adding 3 dB to SNR as we are calculating Symbol Error Rate
BYTELEN = 8;
nFrame = 2000;
#Payload
#PayloadByte = 36; # Size of payload in bytes
PayloadByte = 90; # Size of payload in bytes
PayloadBitsLen = PayloadByte*BYTELEN; # Size of payload in bytes
#PayloadBitsLen = 240*3;
#PayloadSymbsLen = PayloadBitsLen//3
PayloadSymbsLen = (PayloadBitsLen/3);
UsedPilotSymbsLen = 10
UsedPilotBitsLen = 3*UsedPilotSymbsLen;
#UsedPilotSymbsLen=(UsedPilotBitsLen/3);
#UsedPayloadSymbsLen1=3*4;
UsedPayloadSymbsLen = 4;#Number of payload symbols used at the receiver for channel estimation/equalization
#UsedPayloadSymbsLen = (UsedPayloadSymbsLen1/3);#Number of symbols used at the receiver for channel estimation/equalization
#Number of payload symbols from all frames
N = (PayloadSymbsLen)*nFrame/2;
%  
#Generating used pilots for a frame
DataSym = bitstream(UsedPilotBitsLen);
#DataSym = randi([0 1],UsedPilotBitsLen,1)
DataSym1=reshape(DataSym,3,[]);
UsedPilotSymbs=transpose(DataSym1);
DataSym3=zeros(1,UsedPilotSymbsLen);

for ii=1:(UsedPilotSymbsLen)
    DataSym3(ii)=bi2de(UsedPilotSymbs(ii,:),'left-msb')+1;
end
DataSym3
pilot_sym = mapping(M,DataSym3');   % 8-PSK modulation

% 
% % %nErr_seq = zeros(1,length(SymbolSNRdB));
SER_MMSE=zeros(1,length(SymbolSNRdB));

#for i=1:length(SymbolSNRdB)
#     nErr_mmse = 0;
#     EsN01in=10.^(SymbolSNRdB(i)/10);
#     for j = 1:nFrame
#         h1 = randn(L-1,1);
#         h2 = randn(L-1,1);
#         h  = h1 + 1i*h2;
#         h = h/sqrt(2);
#         h = [1; h] ;                 % Rician fading channel
#         h = h/sqrt(L);
#           
#         % Channel estimation
#         Rk_p = conv(h,pilot_sym);
#         noiseSigma=1/sqrt(2)*sqrt(1/(2*EsN01in));
#         noise=noiseSigma*(randn(length(Rk_p),1)+1i*randn(length(Rk_p),1));
#         y_p = Rk_p + noise;
#         h_hat = channel_Estimation_fft(pilot_sym,y_p,L);
#         h_est = h_hat(1:L);
#         w = MMSE_matrix(h_est,length(h)+UsedPayloadSymbsLen-1,EsN01in);
#%          %for k=1:PayloadSymbsLen  
#             DataSym = randi([0 1],(PayloadBitsLen/2),1);
#             DataSym1=reshape(DataSym,3,[]);
#             UsedPilotSymbs=transpose(DataSym1);
#             DataSym3=zeros((PayloadSymbsLen/2),1);
#
#             for ii=1:(PayloadSymbsLen/2)
#                 DataSym3(ii)=bi2de(UsedPilotSymbs(ii,:),'left-msb')+1;
#             end
#             m_psk = mapping(M,DataSym3');
#             m_psk1 = zero_padding(m_psk);
#             Rk = conv(h,m_psk1);
#             Rk1 = reshape(Rk,[244,1]);
#             %Rk=m_psk;
#             noiseSigma=1/sqrt(2)*sqrt(1/(2*EsN01in));
#             noise=noiseSigma*(randn(length(Rk),1)+1i*randn(length(Rk),1));
#             %noise=0+0j;
#             y = Rk1 + noise;   % Received symbols with AWGN noise
#             
#             % MMSE Equalizer
#             X_hat = [];
#             nErr_frame = 0;
#             for jj = 1:(PayloadSymbsLen/8)
#                 y1 = y((jj-1)*8+1:(jj-1)*8+8);
#                 x_hat = w*y1;
#                 x_hat1=demapping(M,x_hat);
#                 x_hat2=(x_hat1-1);
#                 x_hat3=de2bi(x_hat2,3,'left-msb');
#                 x_hat4=transpose(x_hat3);
#                 x_hat5=reshape(x_hat4,[],1);
#                 X_hat = [X_hat;x_hat5];
#               %  disp(size(X_hat))
#                 %nErr_frame = nErr_frame + sum(DataSym((jj-1)*4*3+1:(jj-1)*4*3+12)~=x_hat5);
#              end              
#              nErr_mmse = nErr_mmse + sum(DataSym~=X_hat);
#              %nErr_mmse = nErr_mmse + nErr_frame; 
#% %          % end
#       end
#%       
#%     % SER_MMSE(i) = nErr_mmse/(N)
#      SER_MMSE(i) = nErr_mmse/(3*N)
#   end
#% % 
#EbN0=10.^(BitsnrdB/10);
# theoreticalSER=(1/kk)*(erfc(sqrt(EbN0*log2(M))*sin(pi/M)));
# theory_bpsk = 1.0/2* erfc(sqrt(EbN0));
#
#%% Plots
##semilogy(BitsnrdB,(SER_MMSE),'m-*');
##hold on;
##
##% semilogy(BitsnrdB,theoreticalSER,'r-*');
##% hold on;
##% 
##% semilogy(BitsnrdB,theory_bpsk,'b-*');
##% hold on;
##
##legend('MMSE','TheoryBER','TheoryBPSK','location','best');
##xlabel('$\frac{E_s}{N_0}$(dB)','Interpreter','latex');
##ylabel('$P_e$','Interpreter','latex');
##%saveas(gcf,'Equalizers','eps');
##grid on;
#save ("-ascii", "mmse_ser.dat","BitsnrdB","SER_MMSE","theoreticalSER","theory_bpsk");
