import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

# Generates x values and makes a order 2 polynomial from Fit
x = np.linspace(0,1, num = 100)

# x^2 coeff is from our results, x coeff is -Sn BG, constant is Pb BG

# NDefine modified coeffs. x2coeff comes from our plot. coeff is Pb BG. 
x2coeff = 0.379
coeff = 2.56
xcoeff = 1.97 - coeff - x2coeff

socx2coeff = 0.351
soccoeff = 2.56
socxcoeff = 1.97 - soccoeff - socx2coeff

No_SoC_Func = x2coeff*x**2 + xcoeff*x + coeff
SoC_Func = socx2coeff*x**2 + socxcoeff*x + soccoeff

# Print statements
Fit_No_SoC_Text = "%.3f$x^2$ %.3fx + %.3f" % (x2coeff,xcoeff,coeff)
Fit_SoC_Text = "%.3f$x^2$ %.3fx + %.3f" % (socx2coeff,socxcoeff,soccoeff)

# Plotting Set Up
plt.figure(figsize=(7,6))
plt.title('Bandgap (eV) as a Function of Fraction of Sn Content\nin PEA$_2$Pb$_{1-x}$Sn$_x$I$_4$ with Fixed Boundary Conditions')
plt.ylabel('Bandgap Energy (eV)')
plt.xlabel('Sn Content ($x$)')
plt.xlim(0,1)
plt.ylim(1.9,2.6)
plt.grid()

#SciPy curve fit
plt.plot(x, No_SoC_Func, linestyle = '--')
plt.plot(x, SoC_Func, linestyle = '--')
plt.text(0.255,2.05,'No SoC: ' + Fit_No_SoC_Text)
plt.text(0.55,2.16,'SoC: ' + Fit_SoC_Text)


#Labels
plt.xticks([0,0.25,0.5,0.75,1],['0','0.25','0.5','0.75','1'])
plt.legend(('Non-Linear Least Square Fit Without SoC','Non-Linear Least Square Fit With SoC', 'Without SoC', 'With SoC'))

# Save Fig
plt.savefig('PEA_PbSn_Modified_BG_Function_Graph_SoC_No_SoC_Comp.pdf')
