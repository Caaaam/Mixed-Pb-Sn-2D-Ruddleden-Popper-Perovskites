import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

files = ['CONTCAR_Pb', 'CONTCAR_Sn']

for i in range(1,15):
    files.append('CONTCAR_PbSn'+str(i))

x = [0, 0.25, 0.25, 0.25, 0.25, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.75, 0.75, 0.75, 0.75, 1]

a, b = [],[]
    
for filename in files: 

    file = open(filename, "r")
    
    for linenum, line in enumerate(file): 
        if linenum == 2: 
            a.append(float(line.split('   ', 1)[1].split('   ', 1)[0]))
        if linenum == 3: 
            b.append(float(line.split('   ', 1)[1].split('   ', 1)[1].split('   ', 1)[0]))

xunique = [0, 0.25, 0.5, 0.5, 0.75, 1]           
meana = [] 
meana.append(a[0])
meana.append(sum(a[1:5])/4)
meana.append(sum(a[6:10])/4)
meana.append((a[5]+a[10])/2)
meana.append(sum(a[11:15])/4)
meana.append(a[-1])
print(meana)

meanb = [] 
meanb.append(b[0])
meanb.append(sum(b[1:5])/4)
meanb.append(sum(b[6:10])/4)
meanb.append((b[5]+b[10])/2)
meanb.append(sum(b[11:15])/4)
meanb.append(b[-1])
print(meanb)

fig1, ax1 = plt.subplots(figsize=(5.5,3.8))
ax1.grid(linewidth=0.5)
ax1.set_ylim(11.97,12.04)
ax1.set_xlim()
ax1.set_ylabel('Lattice Parameter ($\AA$)')
ax1.set_xlabel('Sn Content (x)')
ax1.set_xticks([0,0.25,0.5,0.75,1])
slope, intercept, r_value, p_value, std_err = stats.linregress(x,a)
sns.regplot(x,a, line_kws={'label':"y={0:.4f}x+{1:.2f}".format(slope,intercept)})
ax1.scatter(x,a, label ='a')
slope, intercept, r_value, p_value, std_err = stats.linregress(x,b)
sns.regplot(x,b, line_kws={'label':"y={0:.4f}x+{1:.2f}".format(slope,intercept)})
ax1.scatter(x,b, label ='b')
ax1.legend()
#ax1.set_title('Lattice Parameters as a Function of Fraction of\nSn Content For PEA$_2$Pb$_{1-x}$Sn$_x$I$_4$')
fig1.savefig('PEA_lattice_Params.png')


fig2, ax2 = plt.subplots(figsize=(5.5,3.8))
ax2.grid(linewidth=0.5)
ax2.set_ylim(11.97,12.04)
ax2.set_ylabel('Lattice Parameter ($\AA$)')
ax2.set_xlabel('Sn Content ($x$)')
ax2.set_xticks([0,0.25,0.5,0.75,1])
#slope, intercept, r_value, p_value, std_err = stats.linregress(x,a)
#sns.regplot(x,a, line_kws={'label':"y={0:.4f}x+{1:.4f}".format(slope,intercept)})
ax2.scatter(xunique,meana, label ='meana')
#slope, intercept, r_value, p_value, std_err = stats.linregress(x,b)
#sns.regplot(x,b, line_kws={'label':"y={0:.4f}x+{1:.4f}".format(slope,intercept)})
ax2.scatter(xunique,meanb, label ='meanb')
ax2.legend()
fig2.savefig('PEA_Mean_lattice_Params.png')