import matplotlib.pyplot as plt
from A_single_sol import a_single_sol
from S_sol import s_test_sol


n = 4
a_data = a_single_sol(n)
s_data = s_test_sol(n)

c0 = 346.3
deltax = 0.55
t = a_data[2]
t_star = t*c0/deltax

middle = s_data[0][:len(s_data[0])//2][-1]
s_data[1] = s_data[1][:len(s_data[1])//2]
s_data[1] = s_data[1] + s_data[1][::-1]
s_data[0] = [i-middle for i in s_data[0]]
a_data[0] = [i-0.5*t_star for i in a_data[0]]

plt.plot(a_data[0], a_data[1], linestyle='-', linewidth=2, label='Analytical')
plt.plot(s_data[0], s_data[1], linestyle='-', linewidth=2, label='Simulation')

plt.xlabel(r'$x/\Delta x$', fontsize=22)
plt.ylabel(r'$p^\'{} \rho_{0} c_{0}^{2}$ [$Pa$]', fontsize=22)
plt.title('Pressure fluctuations comparison. t='+s_data[2], fontsize=16)
plt.legend(loc=0, fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=15)
plt.grid(b=True, which='major')
plt.show()
