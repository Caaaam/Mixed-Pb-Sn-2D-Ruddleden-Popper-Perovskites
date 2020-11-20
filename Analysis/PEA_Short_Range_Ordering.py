import matplotlib.pyplot as plt
import numpy as np

# File Naming
files = ['CONTCAR_Pb']

for i in range(1,15):
    files.append('CONTCAR_PbSn'+str(i))

files.append('CONTCAR_Sn')

# Defining a list to plot for Sn content
x = [0, 0.25, 0.25, 0.25, 0.25, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.75, 0.75, 0.75, 0.75, 1]

# Making an empty pair of lists
pb_pos,sn_pos = [],[]

# Grabs data from file
def positionappender(pbatoms): 
    for linenum, line in enumerate(file): 
        if linenum in range(16, 16 + pbatoms):
            pb_list.append(np.fromstring(line,dtype=float,sep=' '))
        if linenum in range(16 + pbatoms, 20):
            sn_list.append(np.fromstring(line,dtype=float,sep=' '))
    pb_pos.append(pb_list)
    sn_pos.append(sn_list)    

# Cycles through, sorting Pb and Sn based on number in each run 
for filenum,filename in enumerate(files): 
    file = open(filename, "r")
    pb_list, sn_list = [],[]
    # x = 0 
    if filenum == 0: 
        pbatoms = 4 
        positionappender(pbatoms)
    # x = 0.25
    if filenum in range(1,5):
        pbatoms = 3
        positionappender(pbatoms)
    # x = 0.5
    if filenum in range(5,11):
        pbatoms = 2
        positionappender(pbatoms)
        # x = 0.75        
    if filenum in range(11,15):
        pbatoms = 1
        positionappender(pbatoms)
        # x = 1
    if filenum == 15:
        pbatoms = 0
        positionappender(pbatoms)   
        
meandistance, mindistance, maxdistance = [], [], []
for i in range(15):  
    sumdistance = []
    print()
    if len(pb_pos[i]) and len(sn_pos[i]) > 0:
        for num, pb_position in enumerate(pb_pos[i]):
            for num2, sn_position in enumerate(sn_pos[i]):
                print(pb_position, sn_position)
                sumdistance.append(np.linalg.norm(pb_position-sn_position)) 
        meandistance.append(sum(sumdistance)/len(sumdistance))  
        mindistance.append(min(sumdistance))                      
        maxdistance.append(max(sumdistance))                                          
        print('PbSn' + str(i) + ' Mean: ', sum(sumdistance)/len(sumdistance))
        print('PbSn' + str(i) + ' Min: ', min(sumdistance))
        print('PbSn' + str(i) + ' MAx: ', max(sumdistance))
                
# Plotting
fig1, ax1 = plt.subplots()
ax1.grid(linewidth=0.5)
ax1.set_ylabel('Relative Distance')
ax1.set_xlabel('Sn Content (x)')
ax1.set_xticks([0,0.25,0.5,0.75,1])
ax1.scatter(x[1:5],meandistance[0:4], label ='x = 0.25')
ax1.scatter(x[6:10],meandistance[5:9], label ='x = 0.5 Columns')
ax1.scatter(x[5],meandistance[4], c = 'red')
ax1.scatter(x[10],meandistance[9], label ='x = 0.5 Battenberg', c = 'red')
ax1.scatter(x[-5:-1],meandistance[-4:], label ='x = 0.75')
ax1.legend(loc=4)
fig1.savefig('PEA_SRO_Mean.png')    

# Plotting
fig2, ax2 = plt.subplots()
ax2.grid(linewidth=0.5)
ax2.set_ylabel('Relative Distance')
ax2.set_xlabel('Sn Content (x)')
ax2.set_xticks([0,0.25,0.5,0.75,1])
ax2.scatter(x[1:5],mindistance[0:4], label ='x = 0.25')
ax2.scatter(x[6:10],mindistance[5:9], label ='x = 0.5 Columns')
ax2.scatter(x[5],mindistance[4], c = 'red')
ax2.scatter(x[10],mindistance[9], label ='x = 0.5 Battenberg', c = 'red')
ax2.scatter(x[-5:-1],mindistance[-4:], label ='x = 0.75')
ax2.legend(loc=4)
fig2.savefig('PEA_SRO_Min.png')    

# Plotting
fig3, ax3 = plt.subplots()
ax3.grid(linewidth=0.5)
ax3.set_ylabel('Relative Distance')
ax3.set_xlabel('Sn Content (x)')
ax3.set_xticks([0,0.25,0.5,0.75,1])
ax3.scatter(x[1:5],maxdistance[0:4], label ='x = 0.25')
ax3.scatter(x[6:10],maxdistance[5:9], label ='x = 0.5 Columns')
ax3.scatter(x[5],maxdistance[4], c = 'red')
ax3.scatter(x[10],maxdistance[9], label ='x = 0.5 Battenberg', c = 'red')
ax3.scatter(x[-5:-1],maxdistance[-4:], label ='x = 0.75')
ax3.legend(loc=4)
fig3.savefig('PEA_SRO_Max.png')   