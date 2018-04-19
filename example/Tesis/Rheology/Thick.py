from pyomo.environ import*
from pyomo.opt     import SolverFactory

def model(I_muo=30, kpo=1, Cto=0.6,Sro=100, Reo=1):
    """Thickner Model """ 
    m=ConcreteModel()
    b=Block()
    #---------------------------------------------------------------------------------------------
    #Parameters-----------------------------------------------------------------------------------
    #--------------------------------------------------------------------------------------------

    
    
    #----------------------------------------------------------------------------------------------
    #Variables-------------------------------------------------------------------------------------
    #----------------------------------------------------------------------------------------------

    #Model variables
    m.I_mu=Var(bounds=(0,70), initialize=I_muo)                   #Intrinsec Viscosity
    m.kp  =Var(bounds=(0,10000), initialize=kpo)                  #Huggins slope
    m.Ct  =Var(initialize=Cto, domain=PositiveReals )             #Thickener concentration [g/dL]
    m.Rel =Var(domain=PositiveReals, initialize=Reo)              #Relative viscosity [-]
    
    #Conection variables
    m.Sr=  Var(initialize=Sro, bounds=(1e0, 1e7))                 #Shear rate  [1/s]

    #---------------------------------------------------------------------------------------------
    #Constraints----------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------

    def muh_def(m):                             #Intrinsec Viscosity definition [Xhantam gum]
        return m.I_mu==45.819*exp(-0.005*m.Sr)
    m.muh_def=Constraint(rule=muh_def) 
    
    def kp_def(m):                              #Huggins slope definition
        return m.kp==0.0047*m.Sr-0.005
    m.kp_def=Constraint(rule=kp_def)    
       
    def Hug_eq(m):                            #Huggins equation 
        return m.Rel-1==m.I_mu*m.Ct +m.kp*(m.I_mu)**2*m.Ct**2
    m.Hug_eq=Constraint(rule=Hug_eq)

    #--------------------------------------------------------------------------------------------
    # Block Generation
    #-------------------------------------------------------------------------------------------

    b=m
    return b

def Thick_model(Sro, Cto):

    m=model(I_muo=30, kpo=1, Cto=0.5*100/70,Sro=100, Reo=1)

    #Bounds
    m.bounds=ConstraintList()
    m.bounds.add(expr= m.Sr==Sro)
    m.bounds.add(expr= m.Ct==Cto)

    opt=SolverFactory('ipopt')
    results=opt.solve(m,)

    m.del_component(m.bounds)
    
    return m

__all__=['Thick_model']

if __name__=='__main__':
    import sys

    a=Thick_model(float( sys.argv[1]), float(sys.argv[2]))
    a.pprint()

