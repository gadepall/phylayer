function G=def_G()
G=[kron(ones(1,8),[0 1]);kron(ones(1,4),[0 0 1 1]);kron(ones(1,2),[0 0 0 0 1 1 1 1])];
G=[G;kron([0 1], ones(1,8));ones(1,16)];
