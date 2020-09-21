function h_hat = Channel_estimation(x_p,y_p,L)
    z_p = flip(y_p);
    y_p(1:L-1) = y_p(1:L-1)+flip(z_p(1:L-1));
    y = y_p(1:end-L+1);
    X = fft(x_p);
    Y = fft(y);
    %disp(size(X));
    %disp(size(Y));
    H = Y./X;
    h_hat = ifft(H);
%     xc = x;
%     xr = [x(1) zeros(1,L-1)];
%     X = toeplitz(xc,xr);
%     h_hat = (X'*X)\X'*y;
end
