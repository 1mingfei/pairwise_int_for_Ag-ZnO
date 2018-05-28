#!/usr/bin/python
import numpy as np
#import matplotlib.pyplot as plt
np.set_printoptions(precision=24)
def get_setfl():
    with open('AgO_hand.eam.alloy','r') as fin:
        mylines=fin.readlines()
    Nrho=mylines[4].split()[0]
    drho=mylines[4].split()[1]
    Nr  =mylines[4].split()[2]
    dr  =mylines[4].split()[3]
    rc  =mylines[4].split()[4]
    
    #with open('AgO_auto.eam.alloy','w') as fout:
    #    for i in range(50007):
    #        fout.write(mylines[i])
    #    for i in range(10000):
    #        fout.write('   0.0000000000000000E+00\n')
    #    for i in range(60007,70007):
    #        fout.write(mylines[i])
    return [Nrho,drho,Nr,dr,rc]


def get_L_J(sigma,epsilon,name):
    a=get_setfl()
    Nrho = int(a[0])
    drho = float(a[1])
    Nr   = int(a[2])
    dr   = float(a[3])
    rc   = float(a[4])

    data=np.zeros((Nr,3))
    data[0][0]=0.0
    data[0][1]=0.0
    data[0][2]=0.0
    for i in range(1,Nr):
        data[i][0]=(i)*float(dr)   #r
        data[i][1]=4.0*epsilon*((sigma/data[i][0])**12.0-(sigma/data[i][0])**6.0)        
        data[i][2]=data[i][0]*data[i][1]        
    with open(name,'w') as fout:
        for i in range(Nr):
            fout.write('   %+24.16E   %+24.16E   %+24.16E\n'%(data[i][0],data[i][1],data[i][2]))

    #plt.plot(data[:,0],data[:,1])
    #plt.plot(data[:,0],data[:,2])
    #plt.xlim(0.8, 6) 
    #plt.ylim(-2.5, 2)
    #plt.show()
    return data[:,2]
def get_output_EAM_alloy_3():
    d1_w=get_L_J(2.3/1.12,0.2,'L-J-Ag-O.0.2')   #Ag atomic radius 1.7 O 0.6
    d1_s=get_L_J(2.3/1.12,0.4,'L-J-Ag-O.0.2')   #Ag atomic radius 1.7 O 0.6
    d2=get_L_J(3.3/1.12,0.5,'L-J-X.tmp')   #ZnO lattice const.
    with open('AgO_hand.eam.alloy','r') as fin:
        mylines=fin.readlines()
    Nele=int(mylines[3].split()[0])
    Nrho=int(mylines[4].split()[0])
    Nr  =int(mylines[4].split()[2])
    
    with open('AgO_auto.eam.alloy','w') as fout:
        #Nrho and Nr for each element:
        for i in range(5+Nele*(1+Nrho+Nr)):
            fout.write(mylines[i])
        #phi terms ele1: weak ele2: strong ele3: Ag
        """
        # i,j = (1,1), (2,1), (2,2), (3,1), (3,2), (3,3), (4,1),..., (Nelements, Nelements)
        """
        for i in range(Nr):
            fout.write('   %+24.16E\n'%d2[i])
        for i in range(Nr):
            fout.write('   %+24.16E\n'%d2[i])
        for i in range(Nr):
            fout.write('   %+24.16E\n'%d2[i])
        for i in range(Nr):
            fout.write('   %+24.16E\n'%d1_w[i])
        for i in range(Nr):
            fout.write('   %+24.16E\n'%d1_s[i])
        for i in range(80008,90007):
            fout.write(mylines[i])
    return

def get_output_EAM_alloy_4():
    d1_w=get_L_J(2.3/1.12,0.2,'L-J-Ag-O.0.2')   #Ag atomic radius 1.7 O 0.6
    d1_s=get_L_J(2.3/1.12,0.20,'L-J-Ag-O.0.2')   #Ag atomic radius 1.7 O 0.6
    d1_0=get_L_J(2.3/1.12,0.02,'L-J-Ag-O.0.2')   #Ag atomic radius 1.7 O 0.6
    d2=get_L_J(3.3/1.12,0.5,'L-J-X.tmp')   #ZnO lattice const.
    with open('AgO_hand.eam.alloy','r') as fin:
        mylines=fin.readlines()
    Nele=int(mylines[3].split()[0])
    Nrho=int(mylines[4].split()[0])
    Nr  =int(mylines[4].split()[2])
    with open('AgO_auto.eam.alloy','w') as fout:
        #Nrho and Nr for each element:
        print 5+Nele*(1+Nrho+Nr)
        for i in range(5+Nele*(1+Nrho+Nr)):
            fout.write(mylines[i])
        #phi terms ele1: regular ele2: strong ele3: very weak ele4: Ag
        """
        # i,j = (1,1), (2,1), (2,2), (3,1), (3,2), (3,3), (4,1),..., (Nelements, Nelements)
        """
        for i in range(Nr):
            fout.write('   %+24.16E\n'%d2[i]) # 1,1
        for i in range(Nr):
            fout.write('   %+24.16E\n'%d2[i]) # 2,1
        for i in range(Nr):
            fout.write('   %+24.16E\n'%d2[i]) # 2,2
        for i in range(Nr):
            fout.write('   %+24.16E\n'%d2[i]) # 3,1
        for i in range(Nr):
            fout.write('   %+24.16E\n'%d2[i]) # 3,2
        for i in range(Nr):
            fout.write('   %+24.16E\n'%d2[i]) # 3,3
        for i in range(Nr):
            fout.write('   %+24.16E\n'%d1_w[i]) #4,1
        for i in range(Nr):
            fout.write('   %+24.16E\n'%d1_s[i]) #4,2
        for i in range(Nr):
            fout.write('   %+24.16E\n'%d1_0[i]) #4,3
        for i in range(100009,110009):
            fout.write(mylines[i])   #4,4
    return


    
    


get_output_EAM_alloy_4()
