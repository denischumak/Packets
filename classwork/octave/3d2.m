#plot3(x, y, z) -- отрисовка для 3мерных
t = 0:0.05:9*pi;
x = 2* sin(t);
y = 3*cos(t);

#plot3(x, y, t, 'linewidth', 3)
#view для задания угла
#можно сделать анимированную штуку
#comet3(x, y, t)
#meshgrid(x, y) -подается вектор, формируется массив. Это сеточка на плоскости Oxy
grid on
xlabel('x')
ylabel('y')
zlabel('z')

