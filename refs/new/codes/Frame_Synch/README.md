         Frame Synchronization : Global Summation of SOF/PLSC Detectors
1. Frame_detection.pdf document gives the theoritical analysys of the global SOF + PLS.
2. def_G.m defines the construction of Hadamard matrix for PLS.
3. codage.m describes the scrambled pls sequence.
4. channel.m describes the calculation of the received symbols at the receiver as per (1.1) in Frame_detection.pdf .
5. dec_sof_plus_pls_globlal.m gives the calculation of the global SOF/PLS summation as per (1.5) - (1.9).
6. frame.m describes the entire end to end process from generating symbols to calculatinf P_fa and P_md as per 
(1.11) and (1.12) to plotting the ROC curve for the receiver.
