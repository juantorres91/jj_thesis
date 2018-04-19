#------------------------------
#Molecular parameter information
#------------------------------
from pandas import read_excel
from pandas import DataFrame
from math import isnan

def ParamReading(filen, sname):

    from sets import Set
   
    
    table=read_excel(filen, sheetname=sname, header=0 )
    Matrix=DataFrame.as_matrix(table)
    n=len(Matrix)
    m=len(Matrix[0])

    SMI=Set()  #Smileset
    Second=Set()
    L={}       #Propery dictionary
    #Smiles data
    for i in range(1,n):
        xs=[]
        
        #Set addition--------
        for j in range(0,3):
            xs.append(str(Matrix[i,j]))
        SMI.add(tuple(xs))

        #List addition------
        for j in range(3,m):
            if isnan(Matrix[i,j])==False:
                L[tuple(xs),str(Matrix[0,j])]=Matrix[i,j]

    #Second index informatio
    for j in range(3,m):
        Second.add(str( Matrix[0,j]))
    return SMI, Second, L

#List reading 
def ListReading(filname, sname):
    table=read_excel(filname, sheetname=sname, header=0 )
    Matrix=DataFrame.as_matrix(table)
    n=len(Matrix)
    m=len(Matrix[0])

    NPOS={}
    Bond={}
    C0={}
    C1={}

    for i in range(1,n):
        for j in range(1,m):
            if i==1:
                NPOS[str(Matrix[0,j])]=Matrix[i,j]
            elif i==2:
                Bond[(str(Matrix[0,j]),'Sin')]=Matrix[i,j]
            elif i==3:
                Bond[(str(Matrix[0,j]),'Dou')]=Matrix[i,j]
            elif i==4:
                C0[str(Matrix[0,j])]=Matrix[i,j]
            elif i==5:
                C1[str(Matrix[0,j])]=Matrix[i,j]

    return NPOS, Bond, C0, C1

#Correction reading------------------------------
def CorReading(filname, sname):
    table=read_excel(filname, sheetname=sname, header=0 )
    Matrix=DataFrame.as_matrix(table)
    n=len(Matrix)
    m=len(Matrix[0])

    L={}

    for i in range(1,n):
        for j in range(1,m):
            if isnan(Matrix[i,j])==False:
                L[(str(Matrix[0,j]),str(Matrix[i,0]))]=Matrix[i,j]
    return L
