import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

# Sn Content Fraction
Sn_Content = [0,0.25,0.25,0.25,0.25,0.5,0.5,0.5,0.5,0.5,0.5,0.75,0.75,0.75,0.75,1]

# Results from VASP using 4x4x1 PBE
No_SoC_BG = [2.243,1.923,1.926,1.926,1.924,1.726,1.670,1.782,1.785,1.671,1.733,1.559,1.557,1.555,1.558,1.415]
SoC_BG = [1.578,1.395,1.395,1.394,1.391,1.287,1.283,1.285,1.290,1.345,1.346,1.251,1.257,1.247,1.247,1.225]

# Uses non-linear least squares to fit, fixing both edges
def fit_func(x, a, b,c):
    return a*x**2 + b*x + c 

# Calls function to fit, Sigma weights different points, FIXING the x = 0 and 1 case 
# https://stackoverflow.com/questions/33539287/how-to-force-specific-points-in-curve-fitting
sigma = np.ones(len(Sn_Content))
sigma[[0, -1]] = 0.01
Fit_No_SoC, Covariance_No_Soc = curve_fit(fit_func, Sn_Content, No_SoC_BG, p0=(0.1 ,1e-3, 0.1), sigma=sigma)
Fit_SoC, Covariance_Soc = curve_fit(fit_func, Sn_Content, SoC_BG, p0=(0.1 ,1e-3, 0.1), sigma=sigma)

# Generates x values and makes a order 2 polynomial from Fit
x = np.linspace(0,1, num = 100)
No_SoC_Func = Fit_No_SoC[0]*x**2 + Fit_No_SoC[1]*x + Fit_No_SoC[2]
SoC_Func = Fit_SoC[0]*x**2 + Fit_SoC[1]*x + Fit_SoC[2]

# Print statements
Fit_No_SoC_Text = "%.3f$x^2$ %.3fx + %.3f" % (Fit_No_SoC[0],Fit_No_SoC[1],Fit_No_SoC[2])
Fit_SoC_Text = "%.3f$x^2$ %.3fx + %.3f" % (Fit_SoC[0],Fit_SoC[1],Fit_SoC[2])


print("\nNo SoC funcion coefficients:") 
print(Fit_No_SoC_Text) 

print("\nSoC funcion coefficients:") 
print(Fit_SoC_Text) 


# Plotting Set Up
plt.figure(figsize=(7,6))
plt.title('Bandgap (eV) as a Function of Fraction of\nSn Content For MA$_2$Pb$_{1-x}$Sn$_x$I$_4$')
plt.ylabel('Bandgap Energy (eV)')
plt.xlabel('Sn Content ($x$)')
plt.xlim(0,1)
plt.ylim(1.2,2.25)
plt.grid()

#SciPy curve fit
plt.plot(x, No_SoC_Func, linestyle = '--', label = 'Non-Linear Least Square Fit Without SoC')
plt.plot(x, SoC_Func, linestyle = '--',label = 'Non-Linear Least Square Fit With SoC')
plt.text(0.65,1.62,Fit_No_SoC_Text)
plt.text(0.65,1.28,Fit_SoC_Text)

#Scatter
plt.scatter(Sn_Content, No_SoC_BG, s = 30,label = 'Without SoC')
plt.scatter(Sn_Content, SoC_BG, s = 30,label = 'With SoC')

# Labels 4 dayz
plt.arrow(0.438,1.7,0.06,0.026, width = 0.0000005, head_width = 0.0000000001, fc='k', ec='k')
plt.arrow(0.438,1.7,0.06,0.033, width = 0.0000005, head_width = 0.0000000001, fc='k', ec='k')
plt.arrow(0.438,1.7,0.06,-0.03, width = 0.0000005, head_width = 0.0000000001, fc='k', ec='k')
plt.arrow(0.438,1.7,0.06,-0.03, width = 0.0000005, head_width = 0.0000000001, fc='k', ec='k')
plt.text(0.30,1.692, "'Columns'")

plt.arrow(0.552,1.763,-0.05,0.02, width = 0.0000005, head_width = 0.0000000001, fc='k', ec='k')
plt.text(0.557,1.75, "'Battenberg'")

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
plt.savefig('MA_BG_Function_Graph_SoC_No_SoC_Comp.pdf')
