import pandas as pd
import matplotlib.pyplot as plt

# df variables, this holds a pandas.df for each Permutation of PbSn
Pb_dict = {}
Sn_dict = {}
I_dict = {}

# This holds a VBM and CBM for each Permutation of PbSn
Pb_s_VBM_dict = {}
Pb_p_VBM_dict = {}
Pb_s_CBM_dict = {}
Pb_p_CBM_dict = {}
Sn_s_VBM_dict = {}
Sn_p_VBM_dict = {}
Sn_s_CBM_dict = {}
Sn_p_CBM_dict = {}

##################################### Pb #####################################
Folder = 'Pb'

Total = pd.read_csv(Folder + '/' + Folder + '_total_dos.dat', delimiter = ' ')
Pb = pd.read_csv(Folder + '/' + Folder + '_Pb_dos.dat', delimiter = ' ')
I = pd.read_csv(Folder + '/' + Folder + '_I_dos.dat', delimiter = ' ')

# Columns
Total.columns = ['Energy','DOS','#']
Total = Total.drop(['#'], axis = 1)
                    
Pb.columns = ['Energy','s','p','d','#']
Pb = Pb.drop(['#'], axis = 1)
              
# Removes non-sensical-ve values              
Pb['s'][Pb['s'] < 0.0000001] = -100
Pb['p'][Pb['p'] < 0.0000001] = -100

I.columns = ['Energy','s','p','d','#']
I = I.drop(['#'], axis = 1)
              
# Removes non-sensical-ve values              
I['s'][I['s'] < 0.0000001] = -100
I['p'][I['p'] < 0.0000001] = -100

# VBM and CBM Finder

for index, row in Pb.iterrows():
    if Pb.iloc[index]['Energy'] > -1 and Pb.iloc[index]['Energy'] < 0.5 and Pb.iloc[index]['s'] < -90 and Pb.iloc[index-1]['s'] > 0: 
        Pb_s_VBM = Pb.iloc[index-1]['Energy']
    if Pb.iloc[index]['Energy'] > -1 and Pb.iloc[index]['Energy'] < 0.5 and Pb.iloc[index]['p'] < -90 and Pb.iloc[index-1]['p'] > 0: 
        Pb_p_VBM = Pb.iloc[index-1]['Energy']
    if Pb.iloc[index]['Energy'] > 0.5 and Pb.iloc[index]['Energy'] < 1.5 and Pb.iloc[index]['s'] > 0 and Pb.iloc[index-1]['s'] < -90: 
        Pb_s_CBM = Pb.iloc[index-1]['Energy']
    if Pb.iloc[index]['Energy'] > 0.5 and Pb.iloc[index]['Energy'] < 1.5 and Pb.iloc[index]['p'] > 0 and Pb.iloc[index-1]['p'] < -90: 
        Pb_p_CBM = Pb.iloc[index-1]['Energy']
        
###############################################################################         

##################################### PbSn #####################################

Folder = 'PbSn'

for i in range(1,15):
    Total_read = pd.read_csv(Folder + str(i)+ '/' + Folder + str(i) + '_total_dos.dat', delimiter = ' ')
    Pb_read = pd.read_csv(Folder + str(i)+ '/' + Folder + str(i) + '_Pb_dos.dat', delimiter = ' ')
    Sn_read = pd.read_csv(Folder + str(i)+ '/' + Folder + str(i) + '_Sn_dos.dat', delimiter = ' ')    
    I_read = pd.read_csv(Folder + str(i)+ '/' + Folder + str(i) + '_I_dos.dat', delimiter = ' ')    

    # Columns
    Total_read.columns = ['Energy','DOS','#']
    Total_read = Total_read.drop(['#'], axis = 1)
                        
    Pb_read.columns = ['Energy','s','p','d','#']
    Pb_read = Pb_read.drop(['#'], axis = 1)    
    
    Sn_read.columns = ['Energy','s','p','d','#']
    Sn_read = Sn_read.drop(['#'], axis = 1)      
                            
    I_read.columns = ['Energy','s','p','d','#']
    I_read = I_read.drop(['#'], axis = 1)                             
                            
    # Removes non-sensical-ve values              
    Pb_read['s'][Pb_read['s'] < 0.0000001] = -100
    Pb_read['p'][Pb_read['p'] < 0.0000001] = -100       
    Sn_read['s'][Sn_read['s'] < 0.0000001] = -100
    Sn_read['p'][Sn_read['p'] < 0.0000001] = -100      
    I_read['s'][I_read['s'] < 0.0000001] = -100
    I_read['p'][I_read['p'] < 0.0000001] = -100                 
                            
    Pb_dict["string{0}".format(i)] = Pb_read                    
    Sn_dict["string{0}".format(i)] = Sn_read
    I_dict["string{0}".format(i)] = I_read  
    
    # CBM and VBM Finder
    for index, row in Pb_read.iterrows():
        if Pb_read.iloc[index]['Energy'] > -1 and Pb_read.iloc[index]['Energy'] < 0.5 and Pb_read.iloc[index]['s'] < -90 and Pb_read.iloc[index-1]['s'] > 0: 
            Pb_s_VBM_dict["string{0}".format(i)] = Pb_read.iloc[index-1]['Energy']
        if Pb_read.iloc[index]['Energy'] > -1 and Pb_read.iloc[index]['Energy'] < 0.5 and Pb_read.iloc[index]['p'] < -90 and Pb_read.iloc[index-1]['p'] > 0: 
            Pb_p_VBM_dict["string{0}".format(i)] = Pb_read.iloc[index-1]['Energy']
        if Pb_read.iloc[index]['Energy'] > 0.5 and Pb_read.iloc[index]['Energy'] < 1.5 and Pb_read.iloc[index]['s'] > 0 and Pb_read.iloc[index-1]['s'] < -90: 
            Pb_s_CBM_dict["string{0}".format(i)] = Pb_read.iloc[index-1]['Energy']
        if Pb_read.iloc[index]['Energy'] > 0.5 and Pb_read.iloc[index]['Energy'] < 1.5 and Pb_read.iloc[index]['p'] > 0 and Pb_read.iloc[index-1]['p'] < -90: 
            Pb_p_CBM_dict["string{0}".format(i)] = Pb_read.iloc[index-1]['Energy']
    
    for index, row in Sn_read.iterrows():
        if Sn_read.iloc[index]['Energy'] > -1 and Sn_read.iloc[index]['Energy'] < 0.5 and Sn_read.iloc[index]['s'] < -90 and Sn_read.iloc[index-1]['s'] > 0: 
            Sn_s_VBM_dict["string{0}".format(i)] = Sn_read.iloc[index-1]['Energy']
        if Sn_read.iloc[index]['Energy'] > -1 and Sn_read.iloc[index]['Energy'] < 0.5 and Sn_read.iloc[index]['p'] < -90 and Sn_read.iloc[index-1]['p'] > 0: 
            Sn_p_VBM_dict["string{0}".format(i)] = Sn_read.iloc[index-1]['Energy']
        if Sn_read.iloc[index]['Energy'] > 0.5 and Sn_read.iloc[index]['Energy'] < 1.5 and Sn_read.iloc[index]['s'] > 0 and Sn_read.iloc[index-1]['s'] < -90: 
            Sn_s_CBM_dict["string{0}".format(i)] = Sn_read.iloc[index-1]['Energy']
        if Sn_read.iloc[index]['Energy'] > 0.5 and Sn_read.iloc[index]['Energy'] < 1.5 and Sn_read.iloc[index]['p'] > 0 and Sn_read.iloc[index-1]['p'] < -90: 
            Sn_p_CBM_dict["string{0}".format(i)] = Sn_read.iloc[index-1]['Energy']
###############################################################################             
              
##################################### Sn #####################################
Folder = 'Sn'

Total = pd.read_csv(Folder + '/' + Folder + '_total_dos.dat', delimiter = ' ')
Sn = pd.read_csv(Folder + '/' + Folder + '_Sn_dos.dat', delimiter = ' ')
I2 = pd.read_csv(Folder + '/' + Folder + '_I_dos.dat', delimiter = ' ')

# Columns
Total.columns = ['Energy','DOS','#']
Total = Total.drop(['#'], axis = 1)
                    
Sn.columns = ['Energy','s','p','d','#']
Sn = Sn.drop(['#'], axis = 1)
              
# Removes non-sensical-ve values              
Sn['s'][Sn['s'] <= 0] = -100
Sn['p'][Sn['p'] <= 0] = -100 

I2.columns = ['Energy','s','p','d','#']
I2 = I2.drop(['#'], axis = 1)
              
# Removes non-sensical-ve values              
I2['s'][I2['s'] < 0.0000001] = -100
I2['p'][I2['p'] < 0.0000001] = -100

# VBM and CBM Finder

for index, row in Sn.iterrows():
    if Sn.iloc[index]['Energy'] > -1 and Sn.iloc[index]['Energy'] < 0.5 and Sn.iloc[index]['s'] < -90 and Sn.iloc[index-1]['s'] > 0: 
        Sn_s_VBM = Sn.iloc[index-1]['Energy']
    if Sn.iloc[index]['Energy'] > -1 and Sn.iloc[index]['Energy'] < 0.5 and Sn.iloc[index]['p'] < -90 and Sn.iloc[index-1]['p'] > 0: 
        Sn_p_VBM = Sn.iloc[index-1]['Energy']
    if Sn.iloc[index]['Energy'] > 0.5 and Sn.iloc[index]['Energy'] < 1.5 and Sn.iloc[index]['s'] > 0 and Sn.iloc[index-1]['s'] < -90: 
        Sn_s_CBM = Sn.iloc[index-1]['Energy']
    if Sn.iloc[index]['Energy'] > 0.5 and Sn.iloc[index]['Energy'] < 1.5 and Sn.iloc[index]['p'] > 0 and Sn.iloc[index-1]['p'] < -90: 
        Sn_p_CBM = Sn.iloc[index-1]['Energy']

###############################################################################               
              
############################# Plotting ########################################
# Plotting Set Up
plt.figure(figsize=(30,40))
plt.rcParams.update({'font.size': 16})
nrows = 10
ncols = 3
ymin = 0
ymax = 4
xmin = -2
xmax = 3
Pb_s_VBM_Label = 1.5 
Pb_p_VBM_Label = 1.7 
Sn_s_VBM_Label = 1.1 
Sn_p_VBM_Label = 1.3 
VBM_text_spacing = 0.08
VBM_arrow_spacing = 0.07
CBM_text_spacing = 0.53
CBM_arrow_spacing = 0.145


# Pb
plt.subplot2grid((nrows,ncols), (1,1))
plt.title('PEA$_2$PbI$_4$ DOS')
plt.xlim(xmin,xmax)
plt.ylim(ymin,ymax)
plt.grid()
plt.yticks([])

# Plot 
plt.plot(Pb['Energy'],Pb['s'], color = '#1f77b4')
plt.fill_between(Pb['Energy'],Pb['s'], alpha=0.3)
plt.plot(Pb['Energy'],Pb['p'], color = '#ff7f0e')
plt.fill_between(Pb['Energy'],Pb['p'], alpha=0.3)
plt.plot(I['Energy'],I['s'], color = '#9467bd')
plt.fill_between(I['Energy'],I['s'], alpha=0.3, color = '#9467bd')
plt.plot(I['Energy'],I['p'], color = '#8c564b')
plt.fill_between(I['Energy'],I['p'], alpha=0.3, color = '#8c564b')
plt.legend(('Pb s', 'Pb p','I s', 'I p'), loc = 2, ncol = 2)

'''
# Find Highest VBM and Lowest CBM
Highest_VBM_List = [Pb_s_VBM,Pb_p_VBM]
Highest_VBM = max(Highest_VBM_List)
#Lowest_CBM_List = [Pb_s_CBM,Pb_p_CBM]
#Lowest_CBM = min(Lowest_CBM_List)     

# VBM and CBM Lines
plt.axvline(x=Pb_s_VBM, color = '#1f77b4', linestyle = '--', linewidth = 1)
plt.text(Highest_VBM + VBM_text_spacing,Pb_s_VBM_Label, "Pb s VBM", color = '#1f77b4', fontsize=8)
plt.arrow(Highest_VBM+ VBM_arrow_spacing,Pb_s_VBM_Label+0.04,-VBM_arrow_spacing-Highest_VBM+Pb_s_VBM, 0, color = '#1f77b4', width = 0.0000005, head_width = 0.0000000001, fc='k', ec='k')
plt.axvline(x=Pb_p_VBM, color = '#ff7f0e', linestyle = '--', linewidth = 1)
plt.text(Highest_VBM + VBM_text_spacing,Pb_p_VBM_Label, "Pb p VBM", color = '#ff7f0e', fontsize=8)
plt.arrow(Highest_VBM+ VBM_arrow_spacing,Pb_p_VBM_Label+0.04,-VBM_arrow_spacing-Highest_VBM+Pb_p_VBM, 0, color = '#ff7f0e', width = 0.0000005, head_width = 0.0000000001, fc='k', ec='k')             
plt.axvline(x=Pb_s_CBM, color = '#1f77b4', linestyle = '--', linewidth = 1)
plt.text(Lowest_CBM - CBM_text_spacing,Pb_s_VBM_Label, "Pb s CBM", color = '#1f77b4', fontsize=8)
plt.arrow(Lowest_CBM - CBM_arrow_spacing,Pb_s_VBM_Label+0.04,CBM_arrow_spacing - Lowest_CBM + Pb_s_CBM, 0, color = '#ff7f0e', width = 0.0000005, head_width = 0.0000000001, fc='k', ec='k')             
plt.axvline(x=Pb_p_CBM, color = '#ff7f0e', linestyle = '--', linewidth = 1)
plt.text(Lowest_CBM - CBM_text_spacing,Pb_p_VBM_Label, "Pb p CBM", color = '#ff7f0e', fontsize=8)
plt.arrow(Lowest_CBM - CBM_arrow_spacing,Pb_p_VBM_Label+0.04,CBM_arrow_spacing - Lowest_CBM + Pb_p_CBM, 0, color = '#ff7f0e', width = 0.0000005, head_width = 0.0000000001, fc='k', ec='k')                          
 '''                      

# 0.25
for i in range(1,2):
    if i <= 2:
        plt.subplot2grid((nrows,ncols), (1,2))
    else:
        plt.subplot2grid((nrows,ncols), (3,i-2))
    plt.title('PEA$_2$Pb$_{0.75}$Sn$_{0.25}$I$_4$ DOS Permutation '+str(i))
    plt.xlim(xmin,xmax)
    plt.ylim(ymin,ymax)
    plt.grid()
    plt.yticks([])
    plt.plot(Pb_dict["string"+str(i)]['Energy'],Pb_dict["string"+str(i)]['s'], color = '#1f77b4')
    plt.fill_between(Pb_dict["string"+str(i)]['Energy'],Pb_dict["string"+str(i)]['s'], alpha=0.3, color = '#1f77b4')
    plt.plot(Pb_dict["string"+str(i)]['Energy'],Pb_dict["string"+str(i)]['p'], color = '#ff7f0e')
    plt.fill_between(Pb_dict["string"+str(i)]['Energy'],Pb_dict["string"+str(i)]['p'], alpha=0.3, color = '#ff7f0e')
    plt.plot(Sn_dict["string"+str(i)]['Energy'],Sn_dict["string"+str(i)]['s'], color = '#2ca02c')
    plt.fill_between(Sn_dict["string"+str(i)]['Energy'],Sn_dict["string"+str(i)]['s'], alpha=0.3, color = '#2ca02c')
    plt.plot(Sn_dict["string"+str(i)]['Energy'],Sn_dict["string"+str(i)]['p'], color = '#d62728')
    plt.fill_between(Sn_dict["string"+str(i)]['Energy'],Sn_dict["string"+str(i)]['p'], alpha=0.3, color = '#d62728')
    plt.plot(I_dict["string"+str(i)]['Energy'],I_dict["string"+str(i)]['s'], color = '#9467bd')
    plt.fill_between(I_dict["string"+str(i)]['Energy'],I_dict["string"+str(i)]['s'], alpha=0.3, color = '#9467bd')
    plt.plot(I_dict["string"+str(i)]['Energy'],I_dict["string"+str(i)]['p'], color = '#8c564b')
    plt.fill_between(I_dict["string"+str(i)]['Energy'],I_dict["string"+str(i)]['p'], alpha=0.3, color = '#8c564b')
    plt.legend(('Pb s', 'Pb p', 'Sn s', 'Sn p', 'I s', 'I p'), loc = 2, ncol = 3)

'''  
    # Find Highest VBM and Lowest CBM
    Highest_VBM_List = [Pb_s_VBM_dict["string"+str(i)],Pb_p_VBM_dict["string"+str(i)],Sn_s_VBM_dict["string"+str(i)],Sn_p_VBM_dict["string"+str(i)]]
    Highest_VBM = max(Highest_VBM_List)
    Lowest_CBM_List = [Pb_s_CBM_dict["string"+str(i)],Pb_p_CBM_dict["string"+str(i)],Sn_s_CBM_dict["string"+str(i)],Sn_p_CBM_dict["string"+str(i)]]
    Lowest_CBM = min(Lowest_CBM_List)
    
    # VBM and CBM Lines
    plt.axvline(x=Pb_s_VBM_dict["string"+str(i)], color = '#1f77b4', linestyle = '--', linewidth = 1)
    plt.text(Highest_VBM + VBM_text_spacing,Pb_s_VBM_Label, "Pb s VBM", color = '#1f77b4', fontsize=8)
    plt.arrow(Highest_VBM+ VBM_arrow_spacing,Pb_s_VBM_Label+0.04,-VBM_arrow_spacing-Highest_VBM+Pb_s_VBM_dict["string"+str(i)], 0, color = '#1f77b4', width = 0.0000005, head_width = 0.0000000001, fc='k', ec='k')
    plt.axvline(x=Pb_p_VBM_dict["string"+str(i)], color = '#ff7f0e', linestyle = '--', linewidth = 1)
    plt.text(Highest_VBM + VBM_text_spacing,Pb_p_VBM_Label, "Pb p VBM", color = '#ff7f0e', fontsize=8)
    plt.arrow(Highest_VBM+ VBM_arrow_spacing,Pb_p_VBM_Label+0.04,-VBM_arrow_spacing-Highest_VBM+Pb_p_VBM_dict["string"+str(i)], 0, color = '#ff7f0e', width = 0.0000005, head_width = 0.0000000001, fc='k', ec='k')             
    plt.axvline(x=Pb_s_CBM_dict["string"+str(i)], color = '#1f77b4', linestyle = '--', linewidth = 1)
    plt.text(Lowest_CBM - CBM_text_spacing,Pb_s_VBM_Label, "Pb s CBM", color = '#1f77b4', fontsize=8)
    plt.arrow(Lowest_CBM - CBM_arrow_spacing,Pb_s_VBM_Label+0.04,CBM_arrow_spacing - Lowest_CBM + Pb_s_CBM_dict["string"+str(i)], 0, color = '#ff7f0e', width = 0.0000005, head_width = 0.0000000001, fc='k', ec='k')             
    plt.axvline(x=Pb_p_CBM_dict["string"+str(i)], color = '#ff7f0e', linestyle = '--', linewidth = 1)
    plt.text(Lowest_CBM - CBM_text_spacing,Pb_p_VBM_Label, "Pb p CBM", color = '#ff7f0e', fontsize=8)
    plt.arrow(Lowest_CBM - CBM_arrow_spacing,Pb_p_VBM_Label+0.04,CBM_arrow_spacing - Lowest_CBM + Pb_p_CBM_dict["string"+str(i)], 0, color = '#ff7f0e', width = 0.0000005, head_width = 0.0000000001, fc='k', ec='k')                          
                           
    # VBM and CBM Lines
    plt.axvline(x=Sn_s_VBM_dict["string"+str(i)], color = '#2ca02c', linestyle = '--', linewidth = 1)
    plt.text(Highest_VBM + VBM_text_spacing,Sn_s_VBM_Label, "Sn s VBM", color = '#2ca02c', fontsize=8)
    plt.arrow(Highest_VBM+ VBM_arrow_spacing,Sn_s_VBM_Label+0.04,-VBM_arrow_spacing-Highest_VBM+Sn_s_VBM_dict["string"+str(i)], 0, color = '#1f77b4', width = 0.0000005, head_width = 0.0000000001, fc='k', ec='k')
    plt.axvline(x=Sn_p_VBM_dict["string"+str(i)], color = '#d62728', linestyle = '--', linewidth = 1)
    plt.text(Highest_VBM + VBM_text_spacing,Sn_p_VBM_Label, "Sn p VBM", color = '#d62728', fontsize=8)
    plt.arrow(Highest_VBM+ VBM_arrow_spacing,Sn_p_VBM_Label+0.04,-VBM_arrow_spacing-Highest_VBM+Sn_p_VBM_dict["string"+str(i)], 0, color = '#ff7f0e', width = 0.0000005, head_width = 0.0000000001, fc='k', ec='k')             
    plt.axvline(x=Sn_s_CBM_dict["string"+str(i)], color = '#2ca02c', linestyle = '--', linewidth = 1)
    plt.text(Lowest_CBM - CBM_text_spacing,Sn_s_VBM_Label, "Sn s CBM", color = '#2ca02c', fontsize=8)
    plt.arrow(Lowest_CBM - CBM_arrow_spacing,Sn_s_VBM_Label+0.04,CBM_arrow_spacing - Lowest_CBM + Sn_s_CBM_dict["string"+str(i)], 0, color = '#2ca02c', width = 0.0000005, head_width = 0.0000000001, fc='k', ec='k')             
    plt.axvline(x=Sn_p_CBM_dict["string"+str(i)], color = '#d62728', linestyle = '--', linewidth = 1)
    plt.text(Lowest_CBM - CBM_text_spacing,Sn_p_VBM_Label, "Sn p CBM", color = '#d62728', fontsize=8)                    
    plt.arrow(Lowest_CBM - CBM_arrow_spacing,Sn_p_VBM_Label+0.04,CBM_arrow_spacing - Lowest_CBM + Sn_p_CBM_dict["string"+str(i)], 0, color = '#d62728', width = 0.0000005, head_width = 0.0000000001, fc='k', ec='k')             
'''
# 0.5 
    
for i in range(5,6):
    plt.subplot2grid((nrows,ncols), (2,1))
    plt.title("PEA$_2$Pb$_{0.5}$Sn$_{0.5}$I$_4$ DOS 'Columns' Permutation "+str(i-4))
    plt.xlim(xmin,xmax)
    plt.ylim(ymin,ymax)
    plt.grid()
    plt.yticks([])
    plt.plot(Pb_dict["string"+str(i)]['Energy'],Pb_dict["string"+str(i)]['s'], color = '#1f77b4')
    plt.fill_between(Pb_dict["string"+str(i)]['Energy'],Pb_dict["string"+str(i)]['s'], alpha=0.3, color = '#1f77b4')
    plt.plot(Pb_dict["string"+str(i)]['Energy'],Pb_dict["string"+str(i)]['p'], color = '#ff7f0e')
    plt.fill_between(Pb_dict["string"+str(i)]['Energy'],Pb_dict["string"+str(i)]['p'], alpha=0.3, color = '#ff7f0e')
    plt.plot(Sn_dict["string"+str(i)]['Energy'],Sn_dict["string"+str(i)]['s'], color = '#2ca02c')
    plt.fill_between(Sn_dict["string"+str(i)]['Energy'],Sn_dict["string"+str(i)]['s'], alpha=0.3, color = '#2ca02c')
    plt.plot(Sn_dict["string"+str(i)]['Energy'],Sn_dict["string"+str(i)]['p'], color = '#d62728')
    plt.fill_between(Sn_dict["string"+str(i)]['Energy'],Sn_dict["string"+str(i)]['p'], alpha=0.3, color = '#d62728')
    plt.plot(I_dict["string"+str(i)]['Energy'],I_dict["string"+str(i)]['s'], color = '#9467bd')
    plt.fill_between(I_dict["string"+str(i)]['Energy'],I_dict["string"+str(i)]['s'], alpha=0.3, color = '#9467bd')
    plt.plot(I_dict["string"+str(i)]['Energy'],I_dict["string"+str(i)]['p'], color = '#8c564b')
    plt.fill_between(I_dict["string"+str(i)]['Energy'],I_dict["string"+str(i)]['p'], alpha=0.3, color = '#8c564b')
    plt.legend(('Pb s', 'Pb p', 'Sn s', 'Sn p', 'I s', 'I p'), loc = 2, ncol = 3)
'''
    # Find Highest VBM and Lowest CBM
    Highest_VBM_List = [Pb_s_VBM_dict["string"+str(i)],Pb_p_VBM_dict["string"+str(i)],Sn_s_VBM_dict["string"+str(i)],Sn_p_VBM_dict["string"+str(i)]]
    Highest_VBM = max(Highest_VBM_List)
    Lowest_CBM_List = [Pb_s_CBM_dict["string"+str(i)],Pb_p_CBM_dict["string"+str(i)],Sn_s_CBM_dict["string"+str(i)],Sn_p_CBM_dict["string"+str(i)]]
    Lowest_CBM = min(Lowest_CBM_List)
    
    # VBM and CBM Lines
    plt.axvline(x=Pb_s_VBM_dict["string"+str(i)], color = '#1f77b4', linestyle = '--', linewidth = 1)
    plt.text(Highest_VBM + VBM_text_spacing,Pb_s_VBM_Label, "Pb s VBM", color = '#1f77b4', fontsize=8)
    plt.arrow(Highest_VBM+ VBM_arrow_spacing,Pb_s_VBM_Label+0.04,-VBM_arrow_spacing-Highest_VBM+Pb_s_VBM_dict["string"+str(i)], 0, color = '#1f77b4', width = 0.0000005, head_width = 0.0000000001, fc='k', ec='k')
    plt.axvline(x=Pb_p_VBM_dict["string"+str(i)], color = '#ff7f0e', linestyle = '--', linewidth = 1)
    plt.text(Highest_VBM + VBM_text_spacing,Pb_p_VBM_Label, "Pb p VBM", color = '#ff7f0e', fontsize=8)
    plt.arrow(Highest_VBM+ VBM_arrow_spacing,Pb_p_VBM_Label+0.04,-VBM_arrow_spacing-Highest_VBM+Pb_p_VBM_dict["string"+str(i)], 0, color = '#ff7f0e', width = 0.0000005, head_width = 0.0000000001, fc='k', ec='k')             
    plt.axvline(x=Pb_s_CBM_dict["string"+str(i)], color = '#1f77b4', linestyle = '--', linewidth = 1)
    plt.text(Lowest_CBM - CBM_text_spacing,Pb_s_VBM_Label, "Pb s CBM", color = '#1f77b4', fontsize=8)
    plt.arrow(Lowest_CBM - CBM_arrow_spacing,Pb_s_VBM_Label+0.04,CBM_arrow_spacing - Lowest_CBM + Pb_s_CBM_dict["string"+str(i)], 0, color = '#ff7f0e', width = 0.0000005, head_width = 0.0000000001, fc='k', ec='k')             
    plt.axvline(x=Pb_p_CBM_dict["string"+str(i)], color = '#ff7f0e', linestyle = '--', linewidth = 1)
    plt.text(Lowest_CBM - CBM_text_spacing,Pb_p_VBM_Label, "Pb p CBM", color = '#ff7f0e', fontsize=8)
    plt.arrow(Lowest_CBM - CBM_arrow_spacing,Pb_p_VBM_Label+0.04,CBM_arrow_spacing - Lowest_CBM + Pb_p_CBM_dict["string"+str(i)], 0, color = '#ff7f0e', width = 0.0000005, head_width = 0.0000000001, fc='k', ec='k')                          
                           
    # VBM and CBM Lines
    plt.axvline(x=Sn_s_VBM_dict["string"+str(i)], color = '#2ca02c', linestyle = '--', linewidth = 1)
    plt.text(Highest_VBM + VBM_text_spacing,Sn_s_VBM_Label, "Sn s VBM", color = '#2ca02c', fontsize=8)
    plt.arrow(Highest_VBM+ VBM_arrow_spacing,Sn_s_VBM_Label+0.04,-VBM_arrow_spacing-Highest_VBM+Sn_s_VBM_dict["string"+str(i)], 0, color = '#1f77b4', width = 0.0000005, head_width = 0.0000000001, fc='k', ec='k')
    plt.axvline(x=Sn_p_VBM_dict["string"+str(i)], color = '#d62728', linestyle = '--', linewidth = 1)
    plt.text(Highest_VBM + VBM_text_spacing,Sn_p_VBM_Label, "Sn p VBM", color = '#d62728', fontsize=8)
    plt.arrow(Highest_VBM+ VBM_arrow_spacing,Sn_p_VBM_Label+0.04,-VBM_arrow_spacing-Highest_VBM+Sn_p_VBM_dict["string"+str(i)], 0, color = '#ff7f0e', width = 0.0000005, head_width = 0.0000000001, fc='k', ec='k')             
    plt.axvline(x=Sn_s_CBM_dict["string"+str(i)], color = '#2ca02c', linestyle = '--', linewidth = 1)
    plt.text(Lowest_CBM - CBM_text_spacing,Sn_s_VBM_Label, "Sn s CBM", color = '#2ca02c', fontsize=8)
    plt.arrow(Lowest_CBM - CBM_arrow_spacing,Sn_s_VBM_Label+0.04,CBM_arrow_spacing - Lowest_CBM + Sn_s_CBM_dict["string"+str(i)], 0, color = '#2ca02c', width = 0.0000005, head_width = 0.0000000001, fc='k', ec='k')             
    plt.axvline(x=Sn_p_CBM_dict["string"+str(i)], color = '#d62728', linestyle = '--', linewidth = 1)
    plt.text(Lowest_CBM - CBM_text_spacing,Sn_p_VBM_Label, "Sn p CBM", color = '#d62728', fontsize=8)                    
    plt.arrow(Lowest_CBM - CBM_arrow_spacing,Sn_p_VBM_Label+0.04,CBM_arrow_spacing - Lowest_CBM + Sn_p_CBM_dict["string"+str(i)], 0, color = '#d62728', width = 0.0000005, head_width = 0.0000000001, fc='k', ec='k')             
   
for i in range(9,11):
    plt.subplot2grid((nrows,ncols), (5,i-8))
    plt.title("PEA$_2$Pb$_{0.5}$Sn$_{0.5}$I$_4$ DOS 'Columns' Permutation "+str(i-6))
    plt.xlim(xmin,xmax)
    plt.ylim(ymin,ymax)
    plt.grid()
    plt.yticks([])
    plt.plot(Pb_dict["string"+str(i)]['Energy'],Pb_dict["string"+str(i)]['s'], color = '#1f77b4')
    plt.fill_between(Pb_dict["string"+str(i)]['Energy'],Pb_dict["string"+str(i)]['s'], alpha=0.3, color = '#1f77b4')
    plt.plot(Pb_dict["string"+str(i)]['Energy'],Pb_dict["string"+str(i)]['p'], color = '#ff7f0e')
    plt.fill_between(Pb_dict["string"+str(i)]['Energy'],Pb_dict["string"+str(i)]['p'], alpha=0.3, color = '#ff7f0e')
    plt.plot(Sn_dict["string"+str(i)]['Energy'],Sn_dict["string"+str(i)]['s'], color = '#2ca02c')
    plt.fill_between(Sn_dict["string"+str(i)]['Energy'],Sn_dict["string"+str(i)]['s'], alpha=0.3, color = '#2ca02c')
    plt.plot(Sn_dict["string"+str(i)]['Energy'],Sn_dict["string"+str(i)]['p'], color = '#d62728')
    plt.fill_between(Sn_dict["string"+str(i)]['Energy'],Sn_dict["string"+str(i)]['p'], alpha=0.3, color = '#d62728')
    plt.plot(I_dict["string"+str(i)]['Energy'],I_dict["string"+str(i)]['s'], color = '#9467bd')
    plt.fill_between(I_dict["string"+str(i)]['Energy'],I_dict["string"+str(i)]['s'], alpha=0.3, color = '#9467bd')
    plt.plot(I_dict["string"+str(i)]['Energy'],I_dict["string"+str(i)]['p'], color = '#8c564b')
    plt.fill_between(I_dict["string"+str(i)]['Energy'],I_dict["string"+str(i)]['p'], alpha=0.3, color = '#8c564b')
    plt.legend(('Pb s', 'Pb p', 'Sn s', 'Sn p', 'I s', 'I p'), loc = 2, ncol = 3)

    # Find Highest VBM and Lowest CBM
    Highest_VBM_List = [Pb_s_VBM_dict["string"+str(i)],Pb_p_VBM_dict["string"+str(i)],Sn_s_VBM_dict["string"+str(i)],Sn_p_VBM_dict["string"+str(i)]]
    Highest_VBM = max(Highest_VBM_List)
    Lowest_CBM_List = [Pb_s_CBM_dict["string"+str(i)],Pb_p_CBM_dict["string"+str(i)],Sn_s_CBM_dict["string"+str(i)],Sn_p_CBM_dict["string"+str(i)]]
    Lowest_CBM = min(Lowest_CBM_List)
    
    # VBM and CBM Lines
    plt.axvline(x=Pb_s_VBM_dict["string"+str(i)], color = '#1f77b4', linestyle = '--', linewidth = 1)
    plt.text(Highest_VBM + VBM_text_spacing,Pb_s_VBM_Label, "Pb s VBM", color = '#1f77b4', fontsize=8)
    plt.arrow(Highest_VBM+ VBM_arrow_spacing,Pb_s_VBM_Label+0.04,-VBM_arrow_spacing-Highest_VBM+Pb_s_VBM_dict["string"+str(i)], 0, color = '#1f77b4', width = 0.0000005, head_width = 0.0000000001, fc='k', ec='k')
    plt.axvline(x=Pb_p_VBM_dict["string"+str(i)], color = '#ff7f0e', linestyle = '--', linewidth = 1)
    plt.text(Highest_VBM + VBM_text_spacing,Pb_p_VBM_Label, "Pb p VBM", color = '#ff7f0e', fontsize=8)
    plt.arrow(Highest_VBM+ VBM_arrow_spacing,Pb_p_VBM_Label+0.04,-VBM_arrow_spacing-Highest_VBM+Pb_p_VBM_dict["string"+str(i)], 0, color = '#ff7f0e', width = 0.0000005, head_width = 0.0000000001, fc='k', ec='k')             
    plt.axvline(x=Pb_s_CBM_dict["string"+str(i)], color = '#1f77b4', linestyle = '--', linewidth = 1)
    plt.text(Lowest_CBM - CBM_text_spacing,Pb_s_VBM_Label, "Pb s CBM", color = '#1f77b4', fontsize=8)
    plt.arrow(Lowest_CBM - CBM_arrow_spacing,Pb_s_VBM_Label+0.04,CBM_arrow_spacing - Lowest_CBM + Pb_s_CBM_dict["string"+str(i)], 0, color = '#ff7f0e', width = 0.0000005, head_width = 0.0000000001, fc='k', ec='k')             
    plt.axvline(x=Pb_p_CBM_dict["string"+str(i)], color = '#ff7f0e', linestyle = '--', linewidth = 1)
    plt.text(Lowest_CBM - CBM_text_spacing,Pb_p_VBM_Label, "Pb p CBM", color = '#ff7f0e', fontsize=8)
    plt.arrow(Lowest_CBM - CBM_arrow_spacing,Pb_p_VBM_Label+0.04,CBM_arrow_spacing - Lowest_CBM + Pb_p_CBM_dict["string"+str(i)], 0, color = '#ff7f0e', width = 0.0000005, head_width = 0.0000000001, fc='k', ec='k')                          
                           
    # VBM and CBM Lines
    plt.axvline(x=Sn_s_VBM_dict["string"+str(i)], color = '#2ca02c', linestyle = '--', linewidth = 1)
    plt.text(Highest_VBM + VBM_text_spacing,Sn_s_VBM_Label, "Sn s VBM", color = '#2ca02c', fontsize=8)
    plt.arrow(Highest_VBM+ VBM_arrow_spacing,Sn_s_VBM_Label+0.04,-VBM_arrow_spacing-Highest_VBM+Sn_s_VBM_dict["string"+str(i)], 0, color = '#1f77b4', width = 0.0000005, head_width = 0.0000000001, fc='k', ec='k')
    plt.axvline(x=Sn_p_VBM_dict["string"+str(i)], color = '#d62728', linestyle = '--', linewidth = 1)
    plt.text(Highest_VBM + VBM_text_spacing,Sn_p_VBM_Label, "Sn p VBM", color = '#d62728', fontsize=8)
    plt.arrow(Highest_VBM+ VBM_arrow_spacing,Sn_p_VBM_Label+0.04,-VBM_arrow_spacing-Highest_VBM+Sn_p_VBM_dict["string"+str(i)], 0, color = '#ff7f0e', width = 0.0000005, head_width = 0.0000000001, fc='k', ec='k')             
    plt.axvline(x=Sn_s_CBM_dict["string"+str(i)], color = '#2ca02c', linestyle = '--', linewidth = 1)
    plt.text(Lowest_CBM - CBM_text_spacing,Sn_s_VBM_Label, "Sn s CBM", color = '#2ca02c', fontsize=8)
    plt.arrow(Lowest_CBM - CBM_arrow_spacing,Sn_s_VBM_Label+0.04,CBM_arrow_spacing - Lowest_CBM + Sn_s_CBM_dict["string"+str(i)], 0, color = '#2ca02c', width = 0.0000005, head_width = 0.0000000001, fc='k', ec='k')             
    plt.axvline(x=Sn_p_CBM_dict["string"+str(i)], color = '#d62728', linestyle = '--', linewidth = 1)
    plt.text(Lowest_CBM - CBM_text_spacing,Sn_p_VBM_Label, "Sn p CBM", color = '#d62728', fontsize=8)                    
    plt.arrow(Lowest_CBM - CBM_arrow_spacing,Sn_p_VBM_Label+0.04,CBM_arrow_spacing - Lowest_CBM + Sn_p_CBM_dict["string"+str(i)], 0, color = '#d62728', width = 0.0000005, head_width = 0.0000000001, fc='k', ec='k')             
'''    
    
for i in range(7,8):
    plt.subplot2grid((nrows,ncols), (2,2))
    plt.title("PEA$_2$Pb$_{0.5}$Sn$_{0.5}$I$_4$ DOS 'Battenberg' Permutation "+str(i-6))
    plt.xlim(xmin,xmax)
    plt.ylim(ymin,ymax)
    plt.grid()
    plt.yticks([])
    plt.plot(Pb_dict["string"+str(i)]['Energy'],Pb_dict["string"+str(i)]['s'], color = '#1f77b4')
    plt.fill_between(Pb_dict["string"+str(i)]['Energy'],Pb_dict["string"+str(i)]['s'], alpha=0.3, color = '#1f77b4')
    plt.plot(Pb_dict["string"+str(i)]['Energy'],Pb_dict["string"+str(i)]['p'], color = '#ff7f0e')
    plt.fill_between(Pb_dict["string"+str(i)]['Energy'],Pb_dict["string"+str(i)]['p'], alpha=0.3, color = '#ff7f0e')
    plt.plot(Sn_dict["string"+str(i)]['Energy'],Sn_dict["string"+str(i)]['s'], color = '#2ca02c')
    plt.fill_between(Sn_dict["string"+str(i)]['Energy'],Sn_dict["string"+str(i)]['s'], alpha=0.3, color = '#2ca02c')
    plt.plot(Sn_dict["string"+str(i)]['Energy'],Sn_dict["string"+str(i)]['p'], color = '#d62728')
    plt.fill_between(Sn_dict["string"+str(i)]['Energy'],Sn_dict["string"+str(i)]['p'], alpha=0.3, color = '#d62728')
    plt.plot(I_dict["string"+str(i)]['Energy'],I_dict["string"+str(i)]['s'], color = '#9467bd')
    plt.fill_between(I_dict["string"+str(i)]['Energy'],I_dict["string"+str(i)]['s'], alpha=0.3, color = '#9467bd')
    plt.plot(I_dict["string"+str(i)]['Energy'],I_dict["string"+str(i)]['p'], color = '#8c564b')
    plt.fill_between(I_dict["string"+str(i)]['Energy'],I_dict["string"+str(i)]['p'], alpha=0.3, color = '#8c564b')
    plt.legend(('Pb s', 'Pb p', 'Sn s', 'Sn p', 'I s', 'I p'), loc = 2, ncol = 3)
'''
    # Find Highest VBM and Lowest CBM
    Highest_VBM_List = [Pb_s_VBM_dict["string"+str(i)],Pb_p_VBM_dict["string"+str(i)],Sn_s_VBM_dict["string"+str(i)],Sn_p_VBM_dict["string"+str(i)]]
    Highest_VBM = max(Highest_VBM_List)
    Lowest_CBM_List = [Pb_s_CBM_dict["string"+str(i)],Pb_p_CBM_dict["string"+str(i)],Sn_s_CBM_dict["string"+str(i)],Sn_p_CBM_dict["string"+str(i)]]
    Lowest_CBM = min(Lowest_CBM_List)
    
    # VBM and CBM Lines
    plt.axvline(x=Pb_s_VBM_dict["string"+str(i)], color = '#1f77b4', linestyle = '--', linewidth = 1)
    plt.text(Highest_VBM + VBM_text_spacing,Pb_s_VBM_Label, "Pb s VBM", color = '#1f77b4', fontsize=8)
    plt.arrow(Highest_VBM+ VBM_arrow_spacing,Pb_s_VBM_Label+0.04,-VBM_arrow_spacing-Highest_VBM+Pb_s_VBM_dict["string"+str(i)], 0, color = '#1f77b4', width = 0.0000005, head_width = 0.0000000001, fc='k', ec='k')
    plt.axvline(x=Pb_p_VBM_dict["string"+str(i)], color = '#ff7f0e', linestyle = '--', linewidth = 1)
    plt.text(Highest_VBM + VBM_text_spacing,Pb_p_VBM_Label, "Pb p VBM", color = '#ff7f0e', fontsize=8)
    plt.arrow(Highest_VBM+ VBM_arrow_spacing,Pb_p_VBM_Label+0.04,-VBM_arrow_spacing-Highest_VBM+Pb_p_VBM_dict["string"+str(i)], 0, color = '#ff7f0e', width = 0.0000005, head_width = 0.0000000001, fc='k', ec='k')             
    plt.axvline(x=Pb_s_CBM_dict["string"+str(i)], color = '#1f77b4', linestyle = '--', linewidth = 1)
    plt.text(Lowest_CBM - CBM_text_spacing,Pb_s_VBM_Label, "Pb s CBM", color = '#1f77b4', fontsize=8)
    plt.arrow(Lowest_CBM - CBM_arrow_spacing,Pb_s_VBM_Label+0.04,CBM_arrow_spacing - Lowest_CBM + Pb_s_CBM_dict["string"+str(i)], 0, color = '#ff7f0e', width = 0.0000005, head_width = 0.0000000001, fc='k', ec='k')             
    plt.axvline(x=Pb_p_CBM_dict["string"+str(i)], color = '#ff7f0e', linestyle = '--', linewidth = 1)
    plt.text(Lowest_CBM - CBM_text_spacing,Pb_p_VBM_Label, "Pb p CBM", color = '#ff7f0e', fontsize=8)
    plt.arrow(Lowest_CBM - CBM_arrow_spacing,Pb_p_VBM_Label+0.04,CBM_arrow_spacing - Lowest_CBM + Pb_p_CBM_dict["string"+str(i)], 0, color = '#ff7f0e', width = 0.0000005, head_width = 0.0000000001, fc='k', ec='k')                          
                           
    # VBM and CBM Lines
    plt.axvline(x=Sn_s_VBM_dict["string"+str(i)], color = '#2ca02c', linestyle = '--', linewidth = 1)
    plt.text(Highest_VBM + VBM_text_spacing,Sn_s_VBM_Label, "Sn s VBM", color = '#2ca02c', fontsize=8)
    plt.arrow(Highest_VBM+ VBM_arrow_spacing,Sn_s_VBM_Label+0.04,-VBM_arrow_spacing-Highest_VBM+Sn_s_VBM_dict["string"+str(i)], 0, color = '#1f77b4', width = 0.0000005, head_width = 0.0000000001, fc='k', ec='k')
    plt.axvline(x=Sn_p_VBM_dict["string"+str(i)], color = '#d62728', linestyle = '--', linewidth = 1)
    plt.text(Highest_VBM + VBM_text_spacing,Sn_p_VBM_Label, "Sn p VBM", color = '#d62728', fontsize=8)
    plt.arrow(Highest_VBM+ VBM_arrow_spacing,Sn_p_VBM_Label+0.04,-VBM_arrow_spacing-Highest_VBM+Sn_p_VBM_dict["string"+str(i)], 0, color = '#ff7f0e', width = 0.0000005, head_width = 0.0000000001, fc='k', ec='k')             
    plt.axvline(x=Sn_s_CBM_dict["string"+str(i)], color = '#2ca02c', linestyle = '--', linewidth = 1)
    plt.text(Lowest_CBM - CBM_text_spacing,Sn_s_VBM_Label, "Sn s CBM", color = '#2ca02c', fontsize=8)
    plt.arrow(Lowest_CBM - CBM_arrow_spacing,Sn_s_VBM_Label+0.04,CBM_arrow_spacing - Lowest_CBM + Sn_s_CBM_dict["string"+str(i)], 0, color = '#2ca02c', width = 0.0000005, head_width = 0.0000000001, fc='k', ec='k')             
    plt.axvline(x=Sn_p_CBM_dict["string"+str(i)], color = '#d62728', linestyle = '--', linewidth = 1)
    plt.text(Lowest_CBM - CBM_text_spacing,Sn_p_VBM_Label, "Sn p CBM", color = '#d62728', fontsize=8)                    
    plt.arrow(Lowest_CBM - CBM_arrow_spacing,Sn_p_VBM_Label+0.04,CBM_arrow_spacing - Lowest_CBM + Sn_p_CBM_dict["string"+str(i)], 0, color = '#d62728', width = 0.0000005, head_width = 0.0000000001, fc='k', ec='k')             
'''
# 0.75
    
for i in range(11,12):
    if i <= 12:
        plt.subplot2grid((nrows,ncols), (3,1))
        plt.xlabel('Energy (eV)')
    else:
        plt.subplot2grid((nrows,ncols), (3,1))
        plt.xlabel('Energy (eV)')
    plt.title('PEA$_2$Pb$_{0.25}$Sn$_{0.75}$I$_4$ DOS Permutation '+str(i-10))
    plt.xlim(xmin,xmax)
    plt.ylim(ymin,ymax)
    plt.grid()
    plt.yticks([])
    plt.plot(Pb_dict["string"+str(i)]['Energy'],Pb_dict["string"+str(i)]['s'], color = '#1f77b4')
    plt.fill_between(Pb_dict["string"+str(i)]['Energy'],Pb_dict["string"+str(i)]['s'], alpha=0.3, color = '#1f77b4')
    plt.plot(Pb_dict["string"+str(i)]['Energy'],Pb_dict["string"+str(i)]['p'], color = '#ff7f0e')
    plt.fill_between(Pb_dict["string"+str(i)]['Energy'],Pb_dict["string"+str(i)]['p'], alpha=0.3, color = '#ff7f0e')
    plt.plot(Sn_dict["string"+str(i)]['Energy'],Sn_dict["string"+str(i)]['s'], color = '#2ca02c')
    plt.fill_between(Sn_dict["string"+str(i)]['Energy'],Sn_dict["string"+str(i)]['s'], alpha=0.3, color = '#2ca02c')
    plt.plot(Sn_dict["string"+str(i)]['Energy'],Sn_dict["string"+str(i)]['p'], color = '#d62728')
    plt.fill_between(Sn_dict["string"+str(i)]['Energy'],Sn_dict["string"+str(i)]['p'], alpha=0.3, color = '#d62728')
    plt.plot(I_dict["string"+str(i)]['Energy'],I_dict["string"+str(i)]['s'], color = '#9467bd')
    plt.fill_between(I_dict["string"+str(i)]['Energy'],I_dict["string"+str(i)]['s'], alpha=0.3, color = '#9467bd')
    plt.plot(I_dict["string"+str(i)]['Energy'],I_dict["string"+str(i)]['p'], color = '#8c564b')
    plt.fill_between(I_dict["string"+str(i)]['Energy'],I_dict["string"+str(i)]['p'], alpha=0.3, color = '#8c564b')
    plt.legend(('Pb s', 'Pb p', 'Sn s', 'Sn p', 'I s', 'I p'), loc = 2, ncol = 3)
'''
    # Find Highest VBM and Lowest CBM
    Highest_VBM_List = [Pb_s_VBM_dict["string"+str(i)],Pb_p_VBM_dict["string"+str(i)],Sn_s_VBM_dict["string"+str(i)],Sn_p_VBM_dict["string"+str(i)]]
    Highest_VBM = max(Highest_VBM_List)
    Lowest_CBM_List = [Pb_s_CBM_dict["string"+str(i)],Pb_p_CBM_dict["string"+str(i)],Sn_s_CBM_dict["string"+str(i)],Sn_p_CBM_dict["string"+str(i)]]
    Lowest_CBM = min(Lowest_CBM_List)
    
    # VBM and CBM Lines
    plt.axvline(x=Pb_s_VBM_dict["string"+str(i)], color = '#1f77b4', linestyle = '--', linewidth = 1)
    plt.text(Highest_VBM + VBM_text_spacing,Pb_s_VBM_Label, "Pb s VBM", color = '#1f77b4', fontsize=8)
    plt.arrow(Highest_VBM+ VBM_arrow_spacing,Pb_s_VBM_Label+0.04,-VBM_arrow_spacing-Highest_VBM+Pb_s_VBM_dict["string"+str(i)], 0, color = '#1f77b4', width = 0.0000005, head_width = 0.0000000001, fc='k', ec='k')
    plt.axvline(x=Pb_p_VBM_dict["string"+str(i)], color = '#ff7f0e', linestyle = '--', linewidth = 1)
    plt.text(Highest_VBM + VBM_text_spacing,Pb_p_VBM_Label, "Pb p VBM", color = '#ff7f0e', fontsize=8)
    plt.arrow(Highest_VBM+ VBM_arrow_spacing,Pb_p_VBM_Label+0.04,-VBM_arrow_spacing-Highest_VBM+Pb_p_VBM_dict["string"+str(i)], 0, color = '#ff7f0e', width = 0.0000005, head_width = 0.0000000001, fc='k', ec='k')             
    plt.axvline(x=Pb_s_CBM_dict["string"+str(i)], color = '#1f77b4', linestyle = '--', linewidth = 1)
    plt.text(Lowest_CBM - CBM_text_spacing,Pb_s_VBM_Label, "Pb s CBM", color = '#1f77b4', fontsize=8)
    plt.arrow(Lowest_CBM - CBM_arrow_spacing,Pb_s_VBM_Label+0.04,CBM_arrow_spacing - Lowest_CBM + Pb_s_CBM_dict["string"+str(i)], 0, color = '#ff7f0e', width = 0.0000005, head_width = 0.0000000001, fc='k', ec='k')             
    plt.axvline(x=Pb_p_CBM_dict["string"+str(i)], color = '#ff7f0e', linestyle = '--', linewidth = 1)
    plt.text(Lowest_CBM - CBM_text_spacing,Pb_p_VBM_Label, "Pb p CBM", color = '#ff7f0e', fontsize=8)
    plt.arrow(Lowest_CBM - CBM_arrow_spacing,Pb_p_VBM_Label+0.04,CBM_arrow_spacing - Lowest_CBM + Pb_p_CBM_dict["string"+str(i)], 0, color = '#ff7f0e', width = 0.0000005, head_width = 0.0000000001, fc='k', ec='k')                          
                           
    # VBM and CBM Lines
    plt.axvline(x=Sn_s_VBM_dict["string"+str(i)], color = '#2ca02c', linestyle = '--', linewidth = 1)
    plt.text(Highest_VBM + VBM_text_spacing,Sn_s_VBM_Label, "Sn s VBM", color = '#2ca02c', fontsize=8)
    plt.arrow(Highest_VBM+ VBM_arrow_spacing,Sn_s_VBM_Label+0.04,-VBM_arrow_spacing-Highest_VBM+Sn_s_VBM_dict["string"+str(i)], 0, color = '#1f77b4', width = 0.0000005, head_width = 0.0000000001, fc='k', ec='k')
    plt.axvline(x=Sn_p_VBM_dict["string"+str(i)], color = '#d62728', linestyle = '--', linewidth = 1)
    plt.text(Highest_VBM + VBM_text_spacing,Sn_p_VBM_Label, "Sn p VBM", color = '#d62728', fontsize=8)
    plt.arrow(Highest_VBM+ VBM_arrow_spacing,Sn_p_VBM_Label+0.04,-VBM_arrow_spacing-Highest_VBM+Sn_p_VBM_dict["string"+str(i)], 0, color = '#ff7f0e', width = 0.0000005, head_width = 0.0000000001, fc='k', ec='k')             
    plt.axvline(x=Sn_s_CBM_dict["string"+str(i)], color = '#2ca02c', linestyle = '--', linewidth = 1)
    plt.text(Lowest_CBM - CBM_text_spacing,Sn_s_VBM_Label, "Sn s CBM", color = '#2ca02c', fontsize=8)
    plt.arrow(Lowest_CBM - CBM_arrow_spacing,Sn_s_VBM_Label+0.04,CBM_arrow_spacing - Lowest_CBM + Sn_s_CBM_dict["string"+str(i)], 0, color = '#2ca02c', width = 0.0000005, head_width = 0.0000000001, fc='k', ec='k')             
    plt.axvline(x=Sn_p_CBM_dict["string"+str(i)], color = '#d62728', linestyle = '--', linewidth = 1)
    plt.text(Lowest_CBM - CBM_text_spacing,Sn_p_VBM_Label, "Sn p CBM", color = '#d62728', fontsize=8)                    
    plt.arrow(Lowest_CBM - CBM_arrow_spacing,Sn_p_VBM_Label+0.04,CBM_arrow_spacing - Lowest_CBM + Sn_p_CBM_dict["string"+str(i)], 0, color = '#d62728', width = 0.0000005, head_width = 0.0000000001, fc='k', ec='k')             
'''
    
# Sn 
plt.subplot2grid((nrows,ncols), (3,2))
plt.xlabel('Energy (eV)')
plt.title('PEA$_2$SnI$_4$ DOS')
plt.xlim(xmin,xmax)
plt.ylim(ymin,ymax)
plt.grid()
plt.yticks([])
plt.plot(Sn['Energy'],Sn['s'], color = '#2ca02c')
plt.fill_between(Sn['Energy'],Sn['s'], alpha=0.3, color = '#2ca02c')
plt.plot(Sn['Energy'],Sn['p'], color = '#d62728')
plt.fill_between(Sn['Energy'],Sn['p'], alpha=0.3, color = '#d62728')
plt.plot(I2['Energy'],I2['s'], color = '#9467bd')
plt.fill_between(I2['Energy'],I2['s'], alpha=0.3, color = '#9467bd')
plt.plot(I2['Energy'],I2['p'], color = '#8c564b')
plt.fill_between(I2['Energy'],I2['p'], alpha=0.3, color = '#8c564b')  
plt.legend(('Sn s', 'Sn p', 'I s', 'I p'), loc = 2, ncol = 2)
'''

# Find Highest VBM and Lowest CBM
Highest_VBM_List = [Sn_s_VBM,Sn_p_VBM]
Highest_VBM = max(Highest_VBM_List)
Lowest_CBM_List = [Sn_s_CBM,Sn_p_CBM]
Lowest_CBM = min(Lowest_CBM_List)     

# VBM and CBM Lines
plt.axvline(x=Sn_s_VBM, color = '#2ca02c', linestyle = '--', linewidth = 1)
plt.text(Highest_VBM + VBM_text_spacing,Sn_s_VBM_Label, "Sn s VBM", color = '#2ca02c', fontsize=8)
plt.arrow(Highest_VBM+ VBM_arrow_spacing,Sn_s_VBM_Label+0.04,-VBM_arrow_spacing-Highest_VBM+Sn_s_VBM, 0, color = '#2ca02c', width = 0.0000005, head_width = 0.0000000001, fc='k', ec='k')
plt.axvline(x=Sn_p_VBM, color = '#d62728', linestyle = '--', linewidth = 1)
plt.text(Highest_VBM + VBM_text_spacing,Sn_p_VBM_Label, "Sn p VBM", color = '#d62728', fontsize=8)
plt.arrow(Highest_VBM+ VBM_arrow_spacing,Sn_p_VBM_Label+0.04,-VBM_arrow_spacing-Highest_VBM+Sn_p_VBM, 0, color = '#d62728', width = 0.0000005, head_width = 0.0000000001, fc='k', ec='k')             
plt.axvline(x=Sn_s_CBM, color = '#2ca02c', linestyle = '--', linewidth = 1)
plt.text(Lowest_CBM - CBM_text_spacing,Sn_s_VBM_Label, "Sn s CBM", color = '#2ca02c', fontsize=8)
plt.arrow(Lowest_CBM - CBM_arrow_spacing,Sn_s_VBM_Label+0.04,CBM_arrow_spacing - Lowest_CBM + Sn_s_CBM, 0, color = '#2ca02c', width = 0.0000005, head_width = 0.0000000001, fc='k', ec='k')             
plt.axvline(x=Sn_p_CBM, color = '#d62728', linestyle = '--', linewidth = 1)
plt.text(Lowest_CBM - CBM_text_spacing,Sn_p_VBM_Label, "Sn p CBM", color = '#d62728', fontsize=8)
plt.arrow(Lowest_CBM - CBM_arrow_spacing,Sn_p_VBM_Label+0.04,CBM_arrow_spacing - Lowest_CBM + Sn_p_CBM, 0, color = '#d62728', width = 0.0000005, head_width = 0.0000000001, fc='k', ec='k')                          
 '''
 

plt.tight_layout(pad=1)
plt.savefig('PPDOS_Paper.pdf')