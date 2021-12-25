%% This is a linear algebraic technique to find
%% weights of each feature of the data.

function theta = normalization (X, y)
  %% Step1: 
  %%  4096x595 * 595x4096 = 4096x4096
  %% Step2:
  %%  4096x4096 * 4096x595 = 4096x595
  %% Step3:
  %%  4096x595 * 595x1 = 4096x1
  
  theta = pinv(X' * X) * X' *y;

endfunction
