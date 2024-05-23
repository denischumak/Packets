##clear
##[x, y]=meshgrid(-5:0.5:5, -5:0.5:5);
##plot(x, y);
##xlable('X')
##ylable('Y')

x = -10:0.9:10;
y = -10:0.9:10;

[X, Y] = meshgrid(x, y);
z = sin(sqrt(X.^2+Y.^2))./sqrt(X.^2+Y.^2);
grid on
##subplot(1, 3, 1)
##surf(X, Y, z)

##shading flat
##
##subplot(1, 3, 2)
##surf(X, Y, z)
##shading faceted
##
##subplot(1, 3, 3)
##surf(X, Y, z)
##shading interp

##surfc(X, Y, z)
contour(X, Y, z)
##colorbar
##colormap('spring')
##colormap('winter')
##colormap('summer')


colormap('spring')
##surf(X, Y, z)

##surf(X, Y, z)
##hidden on

