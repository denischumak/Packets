### реализуем диффруыз
##syms y(t)
##DE = diff(y, t) - y == 0
###          d
###  -y(t) + --(y(t)) = 0
###          dt
##sol = dsolve(DE)
###      t
###  C1*e

##syms x(t) y(t)
##ode_sys = [diff(x(t),t) == y(t); diff(y(t),t) == x(t)]
##soln = dsolve(ode_sys)
##
##sx = soln.x
##sy = soln.y

#################ЧИСЛЕННОЕ РЕШЕНИЕ ДИФФУРОВ

# ode45 - четырехшаговый метод рунге кута
# ode23 - двухшаговый метод рунге кута

%Функция решения задачи Коши методом Рунге-Кутта.
function [x,t]=runge_kut(a,b,n,x0)
  h=(b-a)/n;
  x(1)=x0;
  for i=1:n+1
  (i)=a+(i-1)*h;
  end
  for i=2:n+1
  K1=g(t(i-1),x(i-1));
  K2=g(t(i-1)+h/2,x(i-1)+h/2*K1);
  K3=g(t(i-1)+h/2,x(i-1)+h/2*K2);
  K4=g(t(i-1)+h,x(i-1)+h*K3);
  delt=h/6*(K1+2*K2+2*K3+K4);
  x(i)=x(i-1)+delt;
  end
end
