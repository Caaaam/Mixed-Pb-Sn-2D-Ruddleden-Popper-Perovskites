import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
import seaborn as sns
from scipy import stats

# Sn Content Fraction
Sn_Content = [0,0.25,0.25,0.25,0.25,0.5,0.5,0.5,0.5,0.5,0.5,0.75,0.75,0.75,0.75,1]

# Results from VASP using 2x2x1 PBE
HGX1 = [0.264, 0.211, 0.209, 0.211, 0.208, 0.186, 0.166, 0.167, 0.184, 0.197, 0.197, 0.158, 0.159, 0.158, 0.158, 0.143]
HGY1 = [0.293, 0.247, 0.248, 0.247, 0.246, 0.194, 0.221, 0.221, 0.195, 0.218, 0.219, 0.179, 0.177, 0.178, 0.178, 0.158]
HGX2 = [0.264, 0.255, 0.255, 0.251, 0.249, 0.223, 0.191, 0.191, 0.222, 0.197, 0.197, 0.172, 0.173, 0.172, 0.172, 0.143]
HGY2 = [0.293, 0.266, 0.264, 0.264, 0.258, 0.197, 0.225, 0.227, 0.197, 0.218, 0.219, 0.187, 0.189, 0.185, 0.185, 0.158]

EGX1 = [0.210, 0.215, 0.216, 0.218, 0.217, 0.238, 0.207, 0.207, 0.242, 0.182, 0.182, 0.194, 0.196, 0.189, 0.189, 0.152]
EGY1 = [0.281, 0.340, 0.340, 0.339, 0.333, 0, 0.260, 0.261, 0, 0.237, 0.238, 0.291, 0.288, 0.282, 0.282, 0.216]
EGX2 = [0.210, 0.184, 0.183, 0.181, 0.180, 0, 0.187, 0.185, 0, 0.182, 0.182, 0.150, 0.151, 0.154, 0.154, 0.152]
EGY2 = [0.281, 0.210, 0.211, 0.209, 0.206, 0, 0.195, 0.196, 0, 0.237, 0.238, 0.184, 0.182, 0.184, 0.184, 0.216]

MRGX1 = np.divide(EGX1,HGX1) 
MRGX2 = np.divide(EGX2,HGX2) 
MRGY1 = np.divide(EGY1,HGY1) 
MRGY2 = np.divide(EGY2,HGY2) 

# Plotting Set Up
plt.figure(figsize=(8,7))
plt.rcParams.update({'font.size': 14})
#plt.title('Effective hole masses as a Function\nof Fraction of Sn Content')
plt.ylabel('Effective mass (m$_e$)')
plt.xlabel('Sn Content ($x$))')
plt.ylim(0.1,0.4)
plt.grid()

#Scatter
plt.scatter(Sn_Content, HGX1, s = 30, label = 'Light hole effective mass $\Gamma$ to $X$')
plt.scatter(Sn_Content, HGX2, s = 30, label = 'Heavy hole effective mass $\Gamma$ to $X$')
plt.scatter(Sn_Content, HGY1, s = 30, label = 'Light hole effective mass $\Gamma$ to $Y$')
plt.scatter(Sn_Content, HGY2, s = 30, label = 'Heavy hole effective mass $\Gamma$ to $Y$')

# Labels 4 dayz
plt.arrow(0.44,1.27,0.06,0.02, width = 0.0000005, head_width = 0.0000000001, fc='k', ec='k')
plt.arrow(0.44,1.27,0.06,0.02, width = 0.0000005, head_width = 0.0000000001, fc='k', ec='k')
plt.arrow(0.44,1.27,0.06,0.015, width = 0.0000005, head_width = 0.0000000001, fc='k', ec='k')
plt.arrow(0.44,1.27,0.06,0.015, width = 0.0000005, head_width = 0.0000000001, fc='k', ec='k')
plt.text(0.304,1.262, "'Columns'")

plt.arrow(0.552,1.363,-0.05,-0.018, width = 0.0000005, head_width = 0.0000000001, fc='k', ec='k')
plt.text(0.557,1.363, "'Battenberg'")



#Labels
plt.xticks([0,0.25,0.5,0.75,1],['0','0.25','0.5','0.75','1'])
plt.legend()

# Save Fig
plt.savefig('PEA_SoC_effective_Hmasses.pdf')

# Plotting Set Up
plt.figure(figsize=(8,9))
#plt.title('Effective electron masses as a Function\nof Fraction of Sn Content')
plt.ylabel('Effective mass (m$_e$)')
plt.xlabel('Sn Content ($x$)')
plt.ylim(0.1,0.4)
plt.grid()

#Scatter
plt.scatter(Sn_Content, EGX2, s = 30, label = 'Light electron effective mass $\Gamma$ to $X$')
plt.scatter(Sn_Content, EGX1, s = 30, label = 'Heavy electron effective mass $\Gamma$ to $X$')
plt.scatter(Sn_Content, EGY2, s = 30, label = 'Light electron effective mass $\Gamma$ to $Y$')
plt.scatter(Sn_Content, EGY1, s = 30, label = 'Heavy electron effective mass $\Gamma$ to $Y$')

# Labels 4 dayz
plt.arrow(0.44,1.27,0.06,0.02, width = 0.0000005, head_width = 0.0000000001, fc='k', ec='k')
plt.arrow(0.44,1.27,0.06,0.02, width = 0.0000005, head_width = 0.0000000001, fc='k', ec='k')
plt.arrow(0.44,1.27,0.06,0.015, width = 0.0000005, head_width = 0.0000000001, fc='k', ec='k')
plt.arrow(0.44,1.27,0.06,0.015, width = 0.0000005, head_width = 0.0000000001, fc='k', ec='k')
plt.text(0.304,1.262, "'Columns'")

plt.arrow(0.552,1.363,-0.05,-0.018, width = 0.0000005, head_width = 0.0000000001, fc='k', ec='k')
plt.text(0.557,1.363, "'Battenberg'")



#Labels
plt.xticks([0,0.25,0.5,0.75,1],['0','0.25','0.5','0.75','1'])
plt.legend()

# Save Fig
plt.savefig('PEA_SoC_effective_Emasses.pdf')

# Plotting Set Up
plt.figure(figsize=(8,7))
plt.title('Ratio of effective masses as a Function\nof Fraction of Sn Content')
plt.ylabel('Ratio of electron mass to hole mass')
plt.xlabel('Sn Content ($x$))')
plt.ylim(0.5, 2)
plt.grid()

#Scatter
plt.scatter(Sn_Content, MRGX1, s = 30, label = 'Ratio of effective masses $\Gamma$ to $X$  ')
plt.scatter(Sn_Content, MRGX2, s = 30, label = 'Ratio of effective masses $\Gamma$ to $X$ #2')
plt.scatter(Sn_Content, MRGY1, s = 30, label = 'Ratio of effective masses $\Gamma$ to $Y$  ')
plt.scatter(Sn_Content, MRGY2, s = 30, label = 'Ratio of effective masses $\Gamma$ to $Y$ #2')

#Labels
plt.xticks([0,0.25,0.5,0.75,1],['0','0.25','0.5','0.75','1'])
plt.legend()

# Save Fig
plt.savefig('PEA_SoC_effective_mass_Ratio.pdf')
