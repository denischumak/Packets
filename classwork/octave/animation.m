#
##plot(randn(10,3));
##get(gcf); #get current figure
##get(gca); #get current axes
##
##get(gca,'ytick'); #get ytick
##get(gca,'ytick', [-2 0 1.5 pi]); # change var ytick
##set(gca,'linewidth', 20); #change linewith

##h = plot(randn(10,1))
##get(h)
##set(h,'linestyle','--') #стиль линии
##set(h,'linewidth',1337) #ширина линии

##Пример№1

##x = -10:0.01:10;
##k = -2;
##y = k*x.^2 - 2;
##ph = plot(x, y)
##
##axis([-10 10 -100 100])
##
##while k <= 2
##  k = k + 0.01;
##  y = k*x.^2 - 2;
##  set(ph, 'XData', x, 'YData', y)
##  set(ph, 'linewidth', 1337)
##  set(ph, 'linestyle', '--')
####  pause(0.0000000001)
##  drawnow
##endwhile

##Пример№2

clear, clc
x=0:pi/50:4*pi;
y=x;
[X,Y]=meshgrid(x,y);
z=3*sin(X)+cos(Y);
h = surf(z);

axis tight

shading interp
colormap(spring)

for k = 0:pi/100:2*pi
  z = (sin(X)+cos(Y)).*sin(k);
  set(h,'Zdata',z)
  drawnow
endfor
