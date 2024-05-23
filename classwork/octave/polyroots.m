h = 1e-6;
f = @(x) 1+(1+sin(x)-cos(x)).^2-(sin(2*x)-cos(2*x)-0.2).^2;

df = @(x) (f(x + h) - f(x)) / h;


##x0 = -5;
max_iter = 500;
cnt = 1;

roots = []
for i = -5:0.25:5
    x0 = i;
    x1 = x0 - (f(x0) / df(x0));
    while abs(x1 - x0) >= h
      if cnt < max_iter
        x0 = x1;
        x1 = x0 - f(x0) / df(x0);
      else
        break;
      endif
    endwhile
    if abs(x1) < 5
      roots(cnt) = x1;
      cnt = cnt+1;
    endif

endfor
roots = unique(roots);
x = linspace(-10, 10, 1000);
y = f(x);
plot(x, y)
roots
hold on
for i = 1:length(roots)
    plot(roots(i), 0, 'ro');
end
hold off
xlabel('x');
ylabel('f(x)');


