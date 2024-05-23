

u = 0:0.05:2*pi + 1;
v = -1:0.05:1;


##[X, Y] = meshgrid(x, y);
[U, V] = meshgrid(u, v);
x = (1+ V./2.*cos(U./2)).*cos(U);
y = (1+ V./2.*cos(U./2)).*sin(U);
z = V./2.*sin(U./2);
surf(x, y, z)
grid on

colormap('spring')

