from pyomo.environ import*
from pyomo.opt import SolverFactory
from initial import*

SFile='/home/juan/Desktop/Tesis/Molecular/InputTable.xlsx'

def MolGen(SFIL):
    m=ConcreteModel()    
    g=Block()
    #-------------------------------------------------------------------------
    #Sets
    #-------------------------------------------------------------------------

    SMI,Fam,b=ParamReading(SFIL,"Hoja1")
    S1, Fra,an=ParamReading(SFIL,"Hoja2")
    S2, Pro,cw=ParamReading(SFIL,"Hoja3")

    m.S=Set(initialize={'C','ci','O','r','1','d','v'})
    m.SMI=Set(dimen=3, initialize=SMI)  #Complex SMILE set
    m.MoleP=Set(initialize=Pro)         #Molecular Properties
    m.MoleF=Set(initialize=Fam)         #Molecular Families
    m.MoleL=Set(initialize=Fra)         #Molecular fragment set
    m.Expo=RangeSet(0,4)                #Posible binary powers 

    m.Dob= Set(initialize={'F6','F7'})     #Doble bound set 
    m.Even=Set(initialize={'F2','F11'})    #Even Fragement Set
    m.Odd= Set(initialize={'F3','F12'})    #Odd  Fragment  Set

    m.Bon=Set( initialize={'Sin','Dou'})   #Bound Type

    #-------------------------------------------------------------------------
    #Parameters
    #-------------------------------------------------------------------------

    kn={('C','C','v'):-1, ('C','C','C'):-2, ('O','C','C'):-1, ('C','O','C'): 1}
    m.bn=Param(m.SMI, m.MoleF, initialize=b,default=0)   #Molecular Family parameter
    m.an=Param(m.SMI, m.MoleL, initialize=an,default=0)  #Molecular length parameter
    m.kn=Param(m.SMI, default=0, initialize=kn)          #Constant Array

    m.cw=Param(m.SMI, m.MoleP, initialize=cw, default=0) #Property weights


    NPOS,Bond,c0,c1=ListReading(SFIL,'Hoja4')
    Corr=CorReading(SFIL,'Hoja5')

    m.c1=Param(m.MoleP,default=1,initialize=c1)                          #Property coefficient
    m.c0=Param(m.MoleP, default=0, initialize=c0)                        #Property slope
    m.NPOS=Param(m.MoleP, default=0,initialize=NPOS)                     #Constant
    m.Bond=Param(m.MoleP, m.Bon, default=0, initialize=Bond)             # Bond type constant
    m.Corr=Param(m.MoleP, m.MoleF, default=0, initialize=Corr)           #Family property correction

    #-----------------------------------------------------------------------------
    #Variables
    #-----------------------------------------------------------------------------

    m.NS=Var( m.SMI, domain=PositiveReals, initialize=1)    #Number of Smile Atributes
    m.NB=Var( m.MoleF, domain=Binary)                       #Molecule family identifier
    m.N= Var( m.MoleL, domain=PositiveReals, initialize=1)  #Molecule length 
    m.Nexp=Var( m.MoleL, m.Expo, domain=Binary)             #Molecule binary variables

    m.Nvar=Var( domain=Binary)                              # Even n fragment 
    m.mod= Var( within=PositiveReals)                       # Module variable

    m.DCW=Var(m.MoleP)                                      #Optimal descriptor weight
    m.l_y=Var(m.MoleP)                                      #Property linearization
    m.y_prop=Var(m.MoleP)                                  #Property calculation

    #-------------------------------------------------------------------------------
    #Constraints
    #-------------------------------------------------------------------------------

    def FamilyConstraint(m,):                                     #Family constraint
        return sum(m.NB[j] for j in m.MoleF)==1
    m.FamilyConstraint=Constraint(rule=FamilyConstraint)

    def LengthDef(m, j):                                         #Molecular length definition- Binary
        return m.N[j]==sum(m.Nexp[j,k]*(2**k) for k in m.Expo)
    m.LengthDef=Constraint( m.MoleL, rule=LengthDef)

    def MoleculeBalance(m,i1,i2,i3):                              #Smile balance
        if (i1,i2,i3) in m.SMI:
            return sum(m.an[i1,i2,i3,j]*m.N[j] for j in m.MoleL)+sum(m.bn[i1,i2,i3,f]*m.NB[f] for f in m.MoleF)+m.kn[i1,i2,i3]==\
                m.NS[i1,i2,i3]
        else:
            return Constraint.Skip
    m.MoleculeBalance=Constraint(m.S, m.S, m.S, rule=MoleculeBalance)

    #------------------
    #Range Restriction---------------------------------------------------
    #------------------

    m.kmin=Param(default=1)
    m.kmax=Param(default=0)
        
    m.nmin=Param(default=3)
    m.nmax=Param(default=15)
        
    m.mmin=Param(default=2)
    m.mmax=Param(default=12)

    m.nter= Param(default=8) #Tert- Configuration

    def k_CMin(m,):                                   #Minimun k value
        return m.NB['F5']*m.kmin<=m.N['k']
    m.k_CMin=Constraint(rule=k_CMin)

    def k_CMax(m):                                   #Maximum value
        return m.N['k']<=m.kmax*m.NB['F5']
    m.k_CMax=Constraint( rule=k_CMax)

    def n_min(m):                                     #Minimun n value
        return m.nmin*(1-m.NB['F9'])+m.nter*m.NB['F9']<=m.N['n']
    m.n_min=Constraint(rule=n_min)

    def n_max(m):                                      #Maximun n value
        return m.N['n']<= m.nmax*(1-m.NB['F9'])+m.nter*m.NB['F9']
    m.n_max=Constraint(rule=n_max)

    def m_min(m):                                      #Minimun m value
        return m.mmin*(1-m.NB['F11']-m.NB['F12'])<=m.N['m']
    #m.m_min=Constraint(rule=m_min)

    def m_max(m):                                      #Maximun m value
        return m.N['m']<=m.mmax*(1-m.NB['F11']-m.NB['F12']) 
    #m.m_max=Constraint(rule=m_max)

    #-----------
    #Even values--------------------------------------
    #-----------
    def ev_def(m):                                  #Even definition
        return m.N['n']==2*m.mod+m.Nvar
    m.ev_def=Constraint( rule=ev_def)
        
    def ev_n(m,j):#Even n
        return m.NB[j]<=(1-m.Nvar)
    m.ev_n=Constraint(m.Even,rule=ev_n)

    def odd_n(m,j): #Odd n
        return m.NB[j]<=m.Nvar
    m.odd_n=Constraint(m.Odd, rule=odd_n)

    #-------------------------------------------------    
    #Property calculation
    #-------------------------------------------------
    def DCW_def(m,j):                                 #Coeficient weight calculation
        return m.DCW[j]== sum(m.NS[k]*m.cw[k,j] for k in m.SMI) + \
            m.Bond[j,'Sin']*(1-sum(m.NB[k] for k in m.Dob)) + m.Bond[j,'Dou']*sum(m.NB[k] for k in m.Dob) +\
            m.NPOS[j]
    m.DCW_def=Constraint(m.MoleP, rule=DCW_def)
        
    def QSPR(m,j):                                    #Property linearization calculation
        return m.c1[j]*m.DCW[j]+m.c0[j]+sum(m.NB[k]*m.Corr[j,k] for k in m.MoleF)==m.l_y[j]
    m.QSPR=Constraint( m.MoleP, rule=QSPR)

    #Additional properties
    m.MoleP.add('Et', 'dHf','STR') #Total molecular energy/ Formation enthalpy
        
    def Prop_Calc(m,j):                                #Property calculations
        if j=='CP':
            return m.y_prop[j]== exp(m.l_y[j])-273.15
        elif j=='CMC':
            return m.y_prop[j]== exp(-m.l_y[j])
        elif j=='Et':
            return m.y_prop[j]==191.4-12.97*m.l_y['MW']
        elif j=='dHf':
            return m.y_prop[j]==33.29+0.2434*m.y_prop['Et']
        elif j=='STR':
            return m.y_prop[j]==11.63+0.6750*(m.N['m']+m.N['k'])+ 0.6857*m.l_y['KH0']-0.01063*m.y_prop['dHf']-0.1387*(m.N['m']+\
                                                                                                                          m.N['k'])*m.l_y['KH0']
        else:
            return m.y_prop[j]==m.l_y[j]
    m.Prop_Calc=Constraint(m.MoleP, rule=Prop_Calc)




    g=m
    
    return g
 #--------------------------------------------------------------------------------------------------------------------------------------------------
# Initialization functions
#--------------------------------------------------------------------------------------------------------------------------------------------------

def MoleIni(SFIL):
    g=ConcreteModel()
    m=MolGen(SFIL)
    #Model Construction
    g.add_component('m',m)
    g.obj=Objective(expr=- (g.m.y_prop['STR']))
    g.con1=Constraint(expr= g.m.y_prop['CP']>=36)

    
    #Solver
    opt=SolverFactory('bonmin')
    results=opt.solve(g)
    
    
    return g.m 


if __name__=="__main__":
    import sys
    m=MoleIni(SFile)
    m.N.pprint()
    
