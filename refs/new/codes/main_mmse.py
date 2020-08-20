#Code by GVV Sharma
#July  30, 2020

#released under GNU GPL
#Main file for MMSE equalization

#Global Packages
import numpy as np

#Importing custom functions
from EightPSK.mod import *
from EightPSK.demod import *
from EightPSK.mats import *
from frame.frametx import *
from frame.FrameParams import *
from MMSE.ChannelParams import *

#TimeSlot=2e-3 #Transmit time duration
#SNR = 1 #Signal to noise ratio
#TxSymbolRate = 123e3 # symbol rate #53.34

scaling_factor = 10e6
#M=8
#MMSEFilterLen = 5 # MMSE filter length
#ChannelFilterLen = 5  # Channel filter length
#N = 1e4   # Number of symbols
BERsnrdB=np.linspace(0,15,16)  # SNR in dB
print(snrdB)
#kk=log2(M)   
snrdB = BERsnrdB+10*log10(3)   # Adding 3 dB to SNR as we are calculating Symbol Error Rate
#
#nFrame = 2000 #Number of transmitted frames
#PayloadBitsLen = 240*3 #Payload size in bits
#PayloadSymbsLen = (PayloadBitsLen/3) #Payload size in symbols
#len_pilot1 = 3*10 $Number of pilot its used for equalization
#len_pilot=(len_pilot1/3) #Number of pilot symbols
#len_seq1=3*4 #For creating 4x4 matrices at the receiverfor channel estimation/equalization
#len_seq = (len_seq1/3) #Number of symbols used at the receiver for channel estimation/equalization
#N = (PayloadSymbsLen)*nFrame/2 #Number of symbols actually used at the receiver, 4 out of 8 symbols are discarded because they are 0s
##  
#DataSym = randi([0 1],len_pilot1,1)
#DataSym1=reshape(DataSym,3,[])
#DataSym2=transpose(DataSym1)
#DataSym3=zeros(1,len_pilot)
#
#for ii=1:(len_pilot)
#    DataSym3(ii)=bi2de(DataSym2(ii,:),'left-msb')+1
#end
#pilot_sym = mapping(M,DataSym3')   # 8-PSK modulation
#
## 
## # #nErr_seq = zeros(1,length(EsN0dB))
#SER_MMSE=zeros(1,length(EsN0dB))
#
#for i=1:length(EsN0dB)
#     nErr_mmse = 0
#     EsN01in=10.^(EsN0dB(i)/10)
#     for j = 1:nFrame
#         h1 = randn(L-1,1)
#         h2 = randn(L-1,1)
#         h  = h1 + 1i*h2
#         h = h/sqrt(2)
#         h = [1 h]                  # Rician fading channel
#         h = h/sqrt(L)
#           
#         # Channel estimation
#         Rk_p = conv(h,pilot_sym)
#         noiseSigma=1/sqrt(2)*sqrt(1/(2*EsN01in))
#         noise=noiseSigma*(randn(length(Rk_p),1)+1i*randn(length(Rk_p),1))
#         y_p = Rk_p + noise
#         h_hat = channel_Estimation_fft(pilot_sym,y_p,L)
#         h_est = h_hat(1:L)
#         w = MMSE_matrix(h_est,length(h)+len_seq-1,EsN01in)
##          #for k=1:PayloadSymbsLen  
#             DataSym = randi([0 1],(PayloadBitsLen/2),1)
#             DataSym1=reshape(DataSym,3,[])
#             DataSym2=transpose(DataSym1)
#             DataSym3=zeros((PayloadSymbsLen/2),1)
#
#             for ii=1:(PayloadSymbsLen/2)
#                 DataSym3(ii)=bi2de(DataSym2(ii,:),'left-msb')+1
#             end
#             m_psk = mapping(M,DataSym3')
#             m_psk1 = zero_padding(m_psk)
#             Rk = conv(h,m_psk1)
#             Rk1 = reshape(Rk,[244,1])
#             #Rk=m_psk
#             noiseSigma=1/sqrt(2)*sqrt(1/(2*EsN01in))
#             noise=noiseSigma*(randn(length(Rk),1)+1i*randn(length(Rk),1))
#             #noise=0+0j
#             y = Rk1 + noise   # Received symbols with AWGN noise
#             
#             # MMSE Equalizer
#             X_hat = []
#             nErr_frame = 0
#             for jj = 1:(PayloadSymbsLen/8)
#                 y1 = y((jj-1)*8+1:(jj-1)*8+8)
#                 x_hat = w*y1
#                 x_hat1=demapping(M,x_hat)
#                 x_hat2=(x_hat1-1)
#                 x_hat3=de2bi(x_hat2,3,'left-msb')
#                 x_hat4=transpose(x_hat3)
#                 x_hat5=reshape(x_hat4,[],1)
#                 X_hat = [X_hatx_hat5]
#               #  disp(size(X_hat))
#                 #nErr_frame = nErr_frame + sum(DataSym((jj-1)*4*3+1:(jj-1)*4*3+12)~=x_hat5)
#              end              
#              nErr_mmse = nErr_mmse + sum(DataSym~=X_hat)
#              #nErr_mmse = nErr_mmse + nErr_frame 
## #          # end
#       end
##       
##     # SER_MMSE(i) = nErr_mmse/(N)
#      SER_MMSE(i) = nErr_mmse/(3*N)
#   end
## # 
#EbN0=10.^(snrdB/10)
# theoreticalSER=(1/kk)*(erfc(sqrt(EbN0*log2(M))*sin(pi/M)))
# theory_bpsk = 1.0/2* erfc(sqrt(EbN0))
#
### Plots
#semilogy(snrdB,(SER_MMSE),'m-*')
#hold on
#
## semilogy(snrdB,theoreticalSER,'r-*')
## hold on
## 
## semilogy(snrdB,theory_bpsk,'b-*')
## hold on
#
#legend('MMSE','TheoryBER','TheoryBPSK','location','best')
#xlabel('$\frac{E_s}{N_0}$(dB)','Interpreter','latex')
#ylabel('$P_e$','Interpreter','latex')
##saveas(gcf,'Equalizers','eps')
#grid on
