import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

sigma = 10
rho = 28
beta = 8/3
x0 = 0
y0 = 1
z0 = 20
t = np.linspace(0, 15, 300)

def func(t, state, sigma, beta, rho):
    x, y, z = state
    dx = sigma * (y-x)
    dy = x*(rho-z)-y
    dz = x*y-beta*z
    return [dx, dy, dz]
p = (sigma, beta, rho)

y0 = [0, 1.0, 20.0]
t_span = (0.0, 40.0)

result_ivp = solve_ivp(func, t_span, y0, args = p)

print(result_ivp)

fig = plt.figure()

ax = fig.add_subplot(1, 1, 1,  projection='3d')#t_span linspaceом пробить 
ax.plot(result_ivp.y[0], result_ivp.y[1], result_ivp.y[2])
ax.set_title("solve_ivp")
plt.show()