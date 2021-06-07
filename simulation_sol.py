import os
import matplotlib.pyplot as plt
import csv

directory = os.fsencode('C:/Users/lucaj/PycharmProjects/Simulator/test times')
filelist = []
namelist = []

for folder in os.listdir(directory):
    filepath = os.fsdecode(directory)+'/'+os.fsdecode(folder)+'/'+'line_p_pa.xy'
    namelist.append(os.fsdecode(folder))
    filelist.append(filepath)

c0 = 346.3
deltax = 0.55

i = 0
for files in filelist:
    x = []
    y = []

    with open(files, 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=' ')
        for row in plots:
            x.append(float(row[0]))
            y.append(float(row[2]))

    plt.plot(x, y, linestyle='-', linewidth=4, label='$t^{*}$='+str(round(float(namelist[i])*c0/deltax, 1)))
    i += 1

plt.xlabel(r'$x/\Delta x$', fontsize=22)
plt.ylabel(r'$p^\'{} \rho_{0} c_{0}^{2}$ [$Pa$]', fontsize=22)
plt.title('Temporal progression of pressure fluctuations along the $y=0$ axis from the simulation, $t'
          '^{*}=t\cdot c_{0}/\Delta x$',fontsize=16)
plt.legend(loc=0, fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=15)
plt.grid(b=True, which='major')
plt.show()
