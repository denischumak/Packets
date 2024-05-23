
x = -pi:0.1:pi;
y = -pi:0.1:pi;
[X, Y] = meshgrid(x, y);
z = 20 - X.^2 - Y.^2;

surf(X, Y, z)

colormap("spring")
shading interp
axis equal

x0 = 0;
y0 = -1;


z0 = 20 - x0^2 - y0^2;

h = 10^(-10);

dx = ((x0 + h)^2 - x0^2)/h;
dy = ((y0 + h)^2 - y0^2)/h;
dz = ((z0 + h) - z0)/h;

t = -1:0.03:1;
ax = dx*t + x0;
ay = dy*t + y0;
az = dz*t + z0;

hold on
plot3(ax, ay, az)
hold off

