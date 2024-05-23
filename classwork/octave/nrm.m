function paramnorm(mx, my, mz, u, v)
  x = mx(u, v);
  y = my(u, v);
  z = mz(u, v);

##  [X, Y] = meshgrid(x, y);

##[X, Y] = meshgrid(x, y);
  [U, V] = meshgrid(u, v);
  grid on

  colormap('spring')
  surf(X, Y, z);
endfunction
