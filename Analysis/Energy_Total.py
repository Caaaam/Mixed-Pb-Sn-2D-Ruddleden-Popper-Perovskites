import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

# Sn Content Fraction
Sn_Content = [0,0.25,0.25,0.25,0.25,0.5,0.5,0.5,0.5,0.5,0.5,0.75,0.75,0.75,0.75,1]

# Results from VASP using 2x2x1 PBE
Total_Energy = [-0.10564035*10**4, -0.10561827*10**4, -0.10561868*10**4, -0.10561888*10**4, -0.10561896*10**4, -0.10559427*10**4, -0.10559216*10**4, -0.10559322*10**4, -0.10559358*10**4, -0.10559369*10**4, -0.10559521*10**4, -0.10556752*10**4, -0.10556840*10**4, -0.10556840*10**4, -0.10556783*10**4, -0.10554433*10**4]

# Plotting Set Up
plt.figure(figsize=(10,7))
plt.rcParams.update({'font.size': 14})
plt.title('Total Energy as a Function of Fraction of Sn Content')
plt.ylabel('Total Energy (eV)')
plt.xlabel('Sn Content Fraction')
plt.ylim(0.999*min(Total_Energy),1.001*max(Total_Energy))
plt.grid()

#Scatter
plt.scatter(Sn_Content, Total_Energy, s = 30)

#Labels
plt.xticks([0,0.25,0.5,0.75,1],['0','0.25','0.5','0.75','1'])
plt.legend()

# Save Fig
plt.savefig('PEA_SoC_Total_Energy.pdf')
