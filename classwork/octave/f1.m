t = -5:0.01:5;
a = 1/4;
b = 1/16;
m = 8;
n=8;
s = 1000;
x = cos(t) - a*cos(m*t)+b*sin(n*t);
y = sin(t) + a* sin(m*t) +b*cos(n * t);
hold on
for i = 1:s
  plot(x/i, y/i)
end
hold off
grid on
