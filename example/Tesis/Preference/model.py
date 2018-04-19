from pyomo.environ import*
from pyomo.opt import SolverFactory

def pref_model(in_file):
    """ Preference model generator"""

    m=AbstractModel()
    g=Block()
    #Sets----------------------
 
    m.MacroP=Set()       # Macroscopic properties set
    m.Cuts=RangeSet(1,6) # Cutting approximation  set
    
    #Param---------------------
    m.w =Param(m.MacroP, default=0)         #Properties ponderation weights
    m.m1=Param(m.MacroP, m.Cuts, default=0) #Cutting Planes Slope
    m.b1=Param(m.MacroP, m.Cuts, default=0) #Cutting Plane  Intersect
    
    #Variables-----------------
    m.y=Var(m.MacroP, initialize= 100, bounds=(-30,100))  #Customer preference

    def x_init(m,i):
        if i=='Efec':
            return 100
        elif i=='Smot':
            return 1.5
        else:
            return 50 
    m.x=Var(m.MacroP, domain=PositiveReals, initialize=x_init)            #Assorted property values
    m.Pr=Var(domain=PositiveReals)                  #Customer Preference

    #Equations------------------
    def Cutting(m,i,j):  #Property cutting approximation
        if m.m1[i,j]!=0 and m.b1[i,j]!=0:
            return m.y[i]<=m.m1[i,j]*m.x[i]+m.b1[i,j]
        else:
            return Constraint.Skip
    m.Cutting=Constraint(m.MacroP, m.Cuts, rule=Cutting)
    
    def Prop_Cal(m):
        return m.Pr==summation(m.w,m.y)
    m.Prop_Cal=Constraint(rule=Prop_Cal)

    #Model generation

    g=m.create_instance(in_file)

   # g.pprint() 

    return g


def piece_model(pref_file):

    from pyomo.opt import SolverFactory
    m=AbstractModel() #Preference Model
    g=Block()

    #Sets----------------------
    m.MacroP=Set()        # Macroscopic properties set
    m.Cuts=RangeSet(0,6) # Cutting approximation  set
    

    #Parameters
    m.w =Param(m.MacroP, default=0)         #Weights 
    m.F =Param(m.MacroP, m.Cuts, default=0) #Fuction values
    m.xo=Param(m.MacroP, m.Cuts, default=0) #Vertex values

    def Point_init(m,i): #Number of points
        s=0   #Point counter
        for j in m.Cuts :
            if m.F[i,j]>0:
                s=s+1
        return s-1
    m.P=Param(m.MacroP, rule=Point_init)

    
    #Variables
    m.Pr=Var(domain=PositiveReals)           #Total preference

    def x_init(m,i):
        if i=='Efec':
            return 500
        elif i=='Smot':
            return 1.5
        elif i=='Cream':
            return 10
        elif i=='Thic':
            return 10
        elif i=='Fat':
            return 4
        else:
            return 36
    m.x=Var(m.MacroP, within=PositiveReals, initialize=x_init)  #x value  
    m.f=Var(m.MacroP, bounds=(0,100))        #Preference value 
    m.t=Var(m.MacroP, m.Cuts, bounds=(0,1))  #Weighting function
    m.y=Var(m.MacroP, m.Cuts, domain=Binary) #Fragment variable
    
    #Constraints

    def x_cons(m, i):         #x value constraint
        return m.x[i]==sum(m.xo[i,j]*m.t[i,j] for j in m.Cuts  if j<=m.P[i])
    m.x_cons=Constraint(m.MacroP, rule=x_cons) 
    
    def t_cons(m,i,j):        #t value constraint
        if j==0:
            return m.t[i,j]<=m.y[i,j]
        elif j>0 and j<m.P[i]:
            return m.t[i,j]<=m.y[i,j-1]+m.y[i,j]
        elif j==m.P[i]:
            return m.t[i,j]<=m.y[i,j-1]
        else:
            return Constraint.Skip
    m.t_cons=Constraint(m.MacroP, m.Cuts)

    def t_equ(m,i):           #t equivalence constraint 
        return sum(m.t[i,j] for j in m.Cuts if j<=m.P[i])==1
    m.t_equ=Constraint(m.MacroP, rule=t_equ)

    def y_equ(m,i):           #y equivalence constraint
        return sum(m.y[i,j] for j in m.Cuts if j<m.P[i])==1
    m.y_equ=Constraint(m.MacroP, rule=y_equ)

    def f_def(m,i):           #f definition
        return m.f[i]==sum(m.t[i,j]*m.F[i,j] for j in m.Cuts if j<=m.P[i])
    m.f_def=Constraint(m.MacroP, rule=f_def)

    #Objective Definition
    def pr_def(m):
        return m.Pr==summation(m.w,m.f)
    m.pr_def=Constraint(rule=pr_def)
       
    g=m.create_instance(pref_file)

    
  
    
    return g

