clc;
clear all;
close all;
%====================================================================
% Inputs : Eb_N0_dB,
%          freq_offset,
%          phase_offset,
%
% Output : ROC curve
%====================================================================

Eb_N0_dB=-2;     % SNR = -2 dB
freq_offset=250e3*pi*2; % Frequency offset of 250KHz
phase_offset=0.2*pi;    % Phase offset
sof= [-1 1 1 -1 -1 -1 1 1 -1 1 -1 -1 1 -1 1 1 1 -1 1 -1 -1 -1 -1 -1 1 -1 -1 1 1 -1 1 -1]; % SOF 

S_sequence= [0,1,1,1,0,0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,0,0,1,1,1,1,0,0,1,0,0,1]   % Scrambler 
        
modcod=[0 1 0 0 1 0];  
pls=codage(modcod,S_sequence); % Generating PLHEADER

sof_modified = -sof*2+2;
pls_modified = -pls*2+2;
%% Filters calculation
L_sof=32;
L_pls=32;
inverse_index_sof=L_sof:-1:1;
sofI=[sof(inverse_index_sof) zeros(1,L_sof)];
for s=1:L_sof-1
    sof_r(1,:)=sofI(1:L_sof).*sofI(1+s:L_sof+s);
    sof_m_r(s,:)=circshift(sof_r(1,:),[0 s]);
    clear sof_r;
end;
sof_m_b_r=[sof_m_r;zeros(1,32)];
m_buf_filtre_sof=[zeros(32,32) sof_m_b_r];
% 
inverse_index_pls=L_pls:-1:1;
plsI=[pls(inverse_index_pls) zeros(1,L_pls)];
for s=1:5
     filtre(s,:)=kron(ones(1,2^(5-s)),[ones(1,2^(s-1)) zeros(1,2^(s-1))]);
end
filtre_r=[filtre(1,:);filtre(2,:);zeros(1,32);filtre(3,:);zeros(3,32);...
      filtre(4,:);zeros(7,32);filtre(5,:)];
%filtre_r = [zeros(16,32) filtre_r]
%for i = 1:16
 %   filtre_r = [filtre_r;filtre_r(i,:)]
%end
for s1=[1,2,4,8,16]
     pls_r(s1,:)=plsI(1:L_pls).*plsI(1+s1:L_pls+s1);
end
for s2=[1,2,4,8,16]
      filtre_pls(s2,:)=pls_r(s2,:).*filtre_r(s2,:);
end
m_buf_filtre_pls=[filtre_pls zeros(16,32)];
% % %%
withoutplheader=[];

%=================================================================================
% Sending without PLHEADER, Only XFECFRAME. Calculation of False Alarm Probability.
for i=1:100
    x=randi([0 7], 1,360*(L_sof+L_pls));
    y=channel(x,freq_offset,phase_offset,Eb_N0_dB);
    y=y./abs(y);
    % Global summation of SOF/PLSC detectors
    d4=detec_sof_plus_pls_global(y,m_buf_filtre_sof,m_buf_filtre_pls);
    withoutplheader=[withoutplheader d4];
end;
%====================================================================================


%====================================================================================
% Sending XFECFRAME along with PLHEADER. Calculation of Missed Detection Probability.

x=kron(ones(1,10000),[sof_modified pls_modified randi([0 7], 1,64)]);
y=channel(x,freq_offset,phase_offset,Eb_N0_dB);
y=y./abs(y);
d4=detec_sof_plus_pls_global(y,m_buf_filtre_sof,m_buf_filtre_pls);
withplheader=d4(1:L_sof + L_pls +64:length(d4));
%=====================================================================================



%======================================================================================
%% Calculation of False Alarm and Missed detection Probabilities

maxi=max(max(withplheader),max(withoutplheader));

for i=1:100
    threshold= (maxi)/99*(i-1);
    
    pfa(i)=sum((sign(abs(withoutplheader)-threshold)+1)/2)/length(withoutplheader);
    pmd(i)=sum((sign(threshold-abs(withplheader))+1)/2)/length(withplheader);
%% 
end;


%========================================================================================
%% Plotting
semilogx(pfa,pmd);
xlabel('$P_{fa}$','Interpreter','latex');
ylabel('$P_{md}$','Interpreter','latex');
%hl = legend( '$\frac{E_b}{N_0}$=-2 dB, $\phi_0=0.2\pi$ rad, $f_0= 5\times 10^6$ MHz');
%set(hl ,'Interpreter','latex')
xlim([10^(-6) 10^(-2)]);
grid on;
