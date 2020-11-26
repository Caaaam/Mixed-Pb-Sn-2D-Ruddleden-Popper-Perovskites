from ase.build import molecule
from ase.geometry.analysis import Analysis
from ase import Atoms
from ase.io import read, write
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

AllPbIBonds = []
AllSnIBonds = []
AllPbIAngles = []
AllSnIAngles = [] 
AllPbIPbAngles = []
AllSnISnAngles = [] 

for i in range(0,16):

	# VASP POSCAR
	PEA2PbSnI4 = read('CONTCAR_PbSn'+str(i))

	#print(PEA2PbSnI4)

	ana = Analysis(PEA2PbSnI4)

	# Bonds 

	PbIBonds = ana.get_bonds('Pb', 'I', unique=True)
	SnIBonds = ana.get_bonds('Sn', 'I', unique=True)

	#print("\nThere are {} Pb-I bonds in PEA2PbSnI4.".format(len(PbIBonds[0])))
	#print("There are {} Pb-I bonds in PEA2PbSnI4.".format(len(SnIBonds[0])))

	if len(PbIBonds[0]) > 0: 
		PbIBondValues = ana.get_values(PbIBonds)
	
	if len(SnIBonds[0]) > 0: 
		SnIBondValues = ana.get_values(SnIBonds)

	#print("The average Pb-I bond length is {}.".format(np.average(PbIBondValues)))
	#print("The average Sn-I bond length is {}.".format(np.average(SnIBondValues)))

	if len(PbIBonds[0]) > 0: 
		AllPbIBonds.append(np.average(PbIBondValues))

	if len(SnIBonds[0]) > 0: 	
		AllSnIBonds.append(np.average(SnIBondValues))

	# 

	# Angles 

	IPbIAngles = ana.get_angles('I', 'Pb', 'I', unique=True)
	ISnIAngles = ana.get_angles('I', 'Sn', 'I', unique=True)

	PbIPbAngles = ana.get_angles('Pb', 'I', 'Pb', unique=True)
	SnISnAngles = ana.get_angles('Sn', 'I', 'Sn', unique=True)

	#print("\nThere are {} I-Pb-I angles in PEA2PbSnI4.".format(len(IPbIAngles[0])))
	#print("There are {} I-Sn-I angles in PEA2PbSnI4.".format(len(ISnIAngles[0])))

	if len(IPbIAngles[0]) > 0: 
		IPbIAngleValues = ana.get_values(IPbIAngles)
		IPbIAngleValuesOver120 = np.array(IPbIAngleValues) [(np.array(IPbIAngleValues)  >= 120)]
		AllPbIAngles.append(np.average(IPbIAngleValuesOver120))
	if len(PbIPbAngles[0]) > 0: 
		PbIPbAngleValues = ana.get_values(PbIPbAngles)
		print('Pb', i)
		PbIPbAngleValuesOver120 = np.array(PbIPbAngleValues) [(np.array(PbIPbAngleValues)  >= 120)]
		AllPbIPbAngles.append(np.average(PbIPbAngleValuesOver120))

	if len(ISnIAngles[0]) > 0: 
		ISnIAngleValues = ana.get_values(ISnIAngles)
		ISnIAngleValuesOver120 = np.array(ISnIAngleValues) [(np.array(ISnIAngleValues)  >= 120)]
		AllSnIAngles.append(np.average(ISnIAngleValuesOver120))
	if len(SnISnAngles[0]) > 0: 
		SnISnAngleValues = ana.get_values(SnISnAngles)
		print(i, SnISnAngleValues)
		SnISnAngleValuesOver120 = np.array(SnISnAngleValues) [(np.array(SnISnAngleValues)  >= 120)]
		AllSnISnAngles.append(np.average(SnISnAngleValuesOver120))

	#print("The average I-Pb-I angle above 120 is {}.".format(np.average(IPbIAngleValuesOver120)))
	#print("The average I-Sn-I angle above 120 is {}.".format(np.average(ISnIAngleValuesOver120)))

	#

print('\nThe Average Pb-I Bond Length is: \n', AllPbIBonds)
print('\nThe Average Sn-I Bond Length is: \n', AllSnIBonds)
print('\nThe Average I-Pb-I Bond Angle Above 120 is: \n', AllPbIAngles)
print('\nThe Average I-Sn-I Bond Angle Above 120 is: \n', AllSnIAngles)
print('\nThe Average Pb-I-Pb Bond Angle Above 120 is: \n', AllPbIPbAngles)
print('\nThe Average Sn-I-Sn Bond Angle Above 120 is: \n', AllSnISnAngles)

# Plotting 
Pb_Content = [0,0.25,0.25,0.25,0.25,0.5,0.5,0.5,0.5,0.5,0.5,0.75,0.75,0.75,0.75]
Sn_Content = [0.25,0.25,0.25,0.25,0.5,0.5,0.5,0.5,0.5,0.5,0.75,0.75,0.75,0.75,1]

# Plotting Set Up
plt.figure(figsize=(5.5,3.8))
plt.title('Bond Lengths as a Function of Fraction of\nSn Content For PEA$_2$Pb$_{1-x}$Sn$_x$I$_4$')
plt.ylabel('Bond Length ($\AA$)')
plt.xlabel('Sn Content Fraction')
#plt.xlim(0,1)
#plt.ylim(1.2,2.25)
plt.grid()

#m, b = np.polyfit(Pb_Content, AllPbIBonds, 1)
#plt.plot(Pb_Content, m*Pb_Content + b)
slope, intercept, r_value, p_value, std_err = stats.linregress(Pb_Content,AllPbIBonds)
sns.regplot(Pb_Content,AllPbIBonds, line_kws={'label':"y={0:.4f}x+{1:.2f}".format(slope,intercept)})
plt.scatter(Pb_Content, AllPbIBonds, label = 'Pb-I Bond Length')

slope, intercept, r_value, p_value, std_err = stats.linregress(Sn_Content,AllSnIBonds)
sns.regplot(Sn_Content,AllSnIBonds, line_kws={'label':"y={0:.4f}x+{1:.2f}".format(slope,intercept)})
plt.scatter(Sn_Content, AllSnIBonds, label = 'Sn-I Bond Length')

#Labels
plt.xticks([0,0.25,0.5,0.75,1],['0','0.25','0.5','0.75','1'])
plt.legend()

# Save Fig
plt.savefig('PEA_Bond_Lengths.pdf')

# Plotting Set Up
plt.figure(figsize=(5.5,3.8))
plt.title('Opposite X-B-X Bond Angle as a Function of Fraction of\nSn Content For PEA$_2$Pb$_{1-x}$Sn$_x$I$_4$')
plt.ylabel('Bond Angle ($^{\circ}$)')
plt.xlabel('Sn Content Fraction')
#plt.xlim(0,1)
#plt.ylim(0.99*min(AllPbIAngles),1.01*max(AllSnIAngles))
plt.grid()

slope, intercept, r_value, p_value, std_err = stats.linregress(Pb_Content,AllPbIAngles)
sns.regplot(Pb_Content,AllPbIAngles, line_kws={'label':"y={0:.2f}x+{1:.2f}".format(slope,intercept)})
plt.scatter(Pb_Content, AllPbIAngles, label = 'I-Pb-I Bond Angle')


slope, intercept, r_value, p_value, std_err = stats.linregress(Sn_Content,AllSnIAngles)
sns.regplot(Sn_Content,AllSnIAngles, line_kws={'label':"y={0:.2f}x+{1:.2f}".format(slope,intercept)})
plt.scatter(Sn_Content, AllSnIAngles, label = 'I-Sn-I Bond Angle')

#Labels
plt.xticks([0,0.25,0.5,0.75,1],['0','0.25','0.5','0.75','1'])
plt.legend()

# Save Fig
plt.savefig('PEA_XBX_Bond_Angles.pdf')

# Plotting Set Up
plt.figure(figsize=(5.5,3.8))
plt.title('B-X-B Bond Angle as a Function of Fraction of\nSn Content For PEA$_2$Pb$_{1-x}$Sn$_x$I$_4$')
plt.ylabel('Bond Angle ($^{\circ}$)')
plt.xlabel('Sn Content Fraction')
#plt.xlim(0,1)
#plt.ylim(0.99*min(AllPbIAngles),1.01*max(AllSnIAngles))
plt.grid()

# The CONTCARs with 2 opposing B-X-B bonds Sn content
Pbwithbonds = [0,0.25,0.25,0.25,0.25,0.5,0.5,0.5,0.5]
Snwithbonds = [0.5,0.5,0.5,0.5,0.75,0.75,0.75,0.75,1]

slope, intercept, r_value, p_value, std_err = stats.linregress(Pbwithbonds,AllPbIPbAngles)
sns.regplot(Pbwithbonds, AllPbIPbAngles, line_kws={'label':"y={0:.2f}x+{1:.1f}".format(slope,intercept)})
plt.scatter(Pbwithbonds, AllPbIPbAngles, label = 'I-Pb-I Bond Angle')


slope, intercept, r_value, p_value, std_err = stats.linregress(Snwithbonds,AllSnISnAngles)
sns.regplot(Snwithbonds,AllSnISnAngles, line_kws={'label':"y={0:.2f}x+{1:.1f}".format(slope,intercept)})
plt.scatter(Snwithbonds, AllSnISnAngles, label = 'I-Sn-I Bond Angle')

#Labels
plt.xticks([0,0.25,0.5,0.75,1],['0','0.25','0.5','0.75','1'])
plt.legend()

# Save Fig
plt.savefig('PEA_BXB_Bond_Angles.pdf')
