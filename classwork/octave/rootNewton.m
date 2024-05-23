
fun = @(x) 1+(1+sin(x)-cos(x)).^2-(sin(2*x)-cos(2*x)-0.2).^2;
x=-10:0.1:10;
y = fun(x);
plot(x, y)

f = zeros(1, 10/0.5);
j = 1;
for i = -5:0.5:5
  f(j) = fzero(fun, i);
  j = j+1;
endfor
hold on
plot(f, 0, 'ro')
hold off

grid on


f = @(x) 1+(1+sin(x)-cos(x)).^2-(sin(2*x)-cos(2*x)-0.2).^2;

x0 = 0;
N = 10;
for n = 1:N
    fx = f(x0);
    dx = (f(x0 + eps) - f(x0 - eps)) / (2 * eps);
    x1 = x0 - fx / dx;
    x0 = x1;
end

x = linspace(-5, 5);
y = f(x);
plot(x, y);
xlabel('x');
ylabel('f(x)');

hold on
plot(x0, f(x0), 'ro');
hold off


#half devision

f = @(x) 1+(1+sin(x)-cos(x)).^2-(sin(2*x)-cos(2*x)-0.2).^2;


a = -5; ## [a, b]
b = 5;
epsilon = 1e-6;

while abs(b-a) > epsilon
    c = (a+b)/2;
    if f(c) * f(a) < 0
        b = c;
    elseif f(c) * f(b) < 0
        a = c;
    else
        break;
    end
end
x = linspace(-5,5);
y = f(x);
plot(x, y);
hold on
grid on
xlabel('x');
ylabel('y');
plot(c, f(c), 'ro');


h = 1e-6;
f = @(x) 1+(1+sin(x)-cos(x)).^2-(sin(2*x)-cos(2*x)-0.2).^2;

df = @(x) (f(x + h) - f(x)) / h;


x0 = -5;
max_iter = 500;
cnt = 1;

roots = []
for i = -5:0.25:5
    x0 = i;
    x1 = x0 - (f(x0) / df(x0));
    if abs(x1 - x0) < h
        roots(cnt) = x1;
        cnt = cnt+1;
    end
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
    x0 = x1;

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

function roots = rootNewton(f, z0)
    max_iter = 100;
    eps = 1e-6;

    z = z0;
    iter = 0;

    while iter < max_iter && abs(f(z)) > eps
        z = z - f(z) / (3*z^2);
        iter = iter + 1;
    end

    roots = [z, exp(2i*pi/3)*z, exp(4i*pi/3)*z];
end


