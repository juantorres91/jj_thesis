from pyomo.environ import*
from pyomo.opt import SolverFactory
from Tesis.Molecular.model import*

SFile='/home/juan/Desktop/Tesis/Molecular/InputTable.xlsx'

def MoleBlock(SFIL,n=1):


    #Surfactant Blocks

    """
    def block_clone(m,i):
        return MoleIni(SFIL)
    m.blo=Block(m.S, rule=block_clone)

     
    #Sets 
    m.Fa=Set(initialize= m.blo[1].MoleF.value)   #Molecular Families
    m.Pro=Set(initialize= m.blo[1].MoleP.value)  #Molecular properties 
    m.Fra=Set(initialize= m.blo[1].MoleL.value)  #Molecular fragments
    m.Exp=Set(initialize= m.blo[1].Expo)         #Frament expantion 
    
    #Arc set
    m.arc=Set(dimen=2)         #Component Arc
    for i in m.S:
        for j in m.S:
            if i<j:
                m.arc.add( (i,j) )      
    #Parameters-----------------------------------------
    m.Rat=Param(default=5)     #Molecular Ratio

    #Variables------------------------------------------
    m.x=Var(m.S, bounds=(0,1))        #Molar Fraction [-]
    m.x_fa=Var(m.Fa, bounds=(0,1) )   # "Molecular neighborhood"
    m.x_nr=Var( domain=PositiveReals) # N-Range variable

    m.p_arc=Var(m.arc, m.Fra, m.Exp, bounds=(0,1))   #Positive arc
    m.n_arc=Var(m.arc, m.Fra, m.Exp, bounds=(0,1))   #Negative arc

    def y_bound(m,i):
        if i=='HLB':
            return (12,16)
        elif i=='CP':
            return (30, 90)
        else:
            return (-float("inf"),float(" inf"))
    m.y=Var(m.Pro, bounds= y_bound)                  #Surfactant Properties
    #Constraints-----------------------------------------
    def mass_bal(m):
        return summation(m.x)==1
    m.mass_bal=Constraint(rule=mass_bal)          #Mass Balance

    def Fa_Cons(m):
        return summation(m.x_fa)==1
    m.Fa_Cons=Constraint(rule=Fa_Cons)            #Just one molecular neighborhood

    def Fa_Neig(m,i,j):
        return m.blo[i].NB[j]==m.x_fa[j]
    m.Fa_Neig=Constraint(m.S, m.Fa, rule=Fa_Neig) #Molecular neigh definition

    def n_range(m,i):
        return (-m.Rat, m.blo[i].N['n']-m.x_nr, m.Rat)
    m.n_range=Constraint(m.S, rule=n_range)       #Molecular Range

    #Comparison constraints---------------------------------
    def com_rule1(m, s1, s2, f, ex):
        if (s1, s2) in m.arc:
            return m.blo[s1].Nexp[f,ex]-m.blo[s2].Nexp[f,ex]==m.p_arc[s1,s2,f,ex]-m.n_arc[s1,s2,f,ex]

        else:
            return Constraint.Skip
    m.com_rule1=Constraint(m.S, m.S, m.Fra, m.Exp, rule=com_rule1) # Binary difference between fragments

    def com_rule2(m,s1,s2):
        if (s1,s2) in m.arc:
            return sum( m.p_arc[s1,s2,f,ex]+m.n_arc[s1,s2,f,ex] for f in m.Fra for ex in m.Exp)>=1
        else:
            return Constraint.Skip
    m.com_rule2=Constraint(m.S, m.S, rule=com_rule2)

    #Property calculation---------------------------------

    def pro_calc(m, i):
        return m.y[i]==sum(m.x[j]*m.blo[j].y_prop[i] for j in m.S)
    m.pro_calc=Constraint(m.Pro, rule=pro_calc) #Ideal Mixing Property
 """   
    #----------------------------------------------------------------
    # Module Initialization 
    #----------------------------------------------------------------
        

    return MoleIni(SFIL) 

if __name__=="__main__":
    import sys
    MoleBlock(SFile,3) 
