function X = feature_normalize (data, m)
  X = zeros(size(data));
  
  for i = 1: m,
    data_range = range(data(i, :));
    data_range = range(data(i, :));
    X(i, :) = data(i, :) ./ data_range;
    
  endfor
  
  X = X ./ 255.0;

endfunction
