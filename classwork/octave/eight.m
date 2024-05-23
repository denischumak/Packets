function task08(z, x0, y0)
  x = -pi:0.1:pi;
  y = -pi:0.1:pi;
  [X, Y] = meshgrid(x, y);
  ##z = 20 - X.^2 - Y.^2;
  Z = z(X, Y);
  surf(X, Y, Z)

  colormap("spring")
  shading interp
  axis equal

  x0 = 0;
  y0 = -1;


  ##z0 = 20 - x0^2 - y0^2;
  z0 = z(x0, y0)

  h = 10^(-10);

  dx = (z(x0 + h, y0) - z(x0, y0))/h;
  dy = (z(x0, y0 + h) - z(x0, y0))/h;
##  dz = ((z0 + h) - z0)/h;
  dz = 1;
  t = -1:0.03:1;
  ax = dx*t + x0;
  ay = dy*t + y0;
  az = dz*t + z0;

  hold on
  plot3(ax, ay, az)
  hold off

endfunction
