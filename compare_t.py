from S_sol import s_t_sol
import matplotlib.pyplot as plt

t = 0.048
data = s_t_sol(t)

c0 = 346.3
deltax = 0.55
t_star = t*c0/deltax

data[0] = [i-t_star for i in data[0]]

plt.plot(data[0], data[1], linestyle='-', linewidth=2, label='Simulation. t='+str(t))
plt.xlabel(r'$x/\Delta x$', fontsize=22)
plt.ylabel(r'$p^\'{} \rho_{0} c_{0}^{2}$ [$Pa$]', fontsize=22)
plt.title('Simulated pressure fluctuations', fontsize=16)
plt.legend(loc=0, fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=15)
plt.grid(b=True, which='major')
plt.show()
