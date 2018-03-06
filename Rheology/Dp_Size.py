from pyomo.environ import*

def model(den=1.1, st0=13, mu0=1):

    m=ConcreteModel()
    b=Block() 
    #----------------------------------------------------------------------------------------------
    #Parameters
    #----------------------------------------------------------------------------------------------

    #Otto metzner
    m.ks=Param(default=11.5)             #Otto Metzner Constant 
    
    #Max drop size
    m.A_t=Param(default=0.54)         #Davis- Hinze Kolmogorov [1]
    m.A_n=Param(default=4.1)           #Davis- Hinze Kolmogorov [2]

    #Mixing parameters
    m.D_I=Param(default=0.06)                 #Imperler Diameter [m]

    #----------------------------------------------------------------------------------------------
    #Variables
    #----------------------------------------------------------------------------------------------
    
    m.Ep=Var(domain=PositiveReals,initialize=30)                         #Energy dissipation [W/kg]
     
    m.dKI=Var(domain=PositiveReals,initialize=5)                         #Dimensional group [m]
    m.dD =Var(domain=PositiveReals,initialize=20, bounds=(1, 100))       #D32  [1e-6 m]

    #External variables

    m.c_den=Var(domain=PositiveReals, initialize=den)                    #Continuos phase viscosity [g/cm3]
    m.Sr =Var(domain=PositiveReals, initialize=100)                      #Shear rate         [s-1]
    m.N=Var(initialize=4, bounds=(1e-3, 1000))                           #Revolution Number  [s-1]
    m.st =Var(domain=PositiveReals, initialize=st0)                      #S. Tension [mN/m]
    m.d_mu= Var(domain=PositiveReals, initialize=mu0)                    #Disperse phase dynamic viscosity [P]
              
    #----------------------------------------------------------------------------------------------
    #Constraint
    #----------------------------------------------------------------------------------------------
       
    def Sh_def(m):                            #Shear rate definition
        return m.Sr==m.ks*m.N
    m.Sh_def=Constraint(rule=Sh_def)

    def Ep_def(m):                              #Dissipation definition
            return m.Ep==0.407*pow(m.N,3)*m.D_I**2
    m.Ep_def=Constraint(rule=Ep_def)

    def dKI_def(m):                             #dKI definition
        return m.dKI==(m.Ep**(-0.4))*( (1e-3*m.st)**(0.6))*((1e3*m.c_den)**(-0.6))
    m.dKI_def=Constraint(rule=dKI_def)

    def dD_def(m):                              #Particle constraint
        return 1e-6*m.dD==m.A_t*(1+m.A_n*(0.1*m.d_mu)*m.Ep**(0.33333) *(1e-6*m.dD)**(0.3333)/(1e-3*m.st))**0.6*m.dKI  
    m.dD_def=Constraint(rule=dD_def)

    #----------------------------------------------------------------------------------------------
    #Block construction
    #----------------------------------------------------------------------------------------------

    b=m
    return b

def Particle(dp, den=1.1, st0=13, mu0=0.2):
    """ Particle Block"""

    m=model(den, st0, mu0)

    #Fixed Variables
    m.bounds= ConstraintList()

    m.bounds.add(expr= m.c_den==den)
    m.bounds.add(expr= m.st==st0)
    m.bounds.add(expr= m.d_mu==mu0)

    m.Obj=Objective(expr= pow(dp-m.dD,2))

  
    # Solver

    opt=SolverFactory("ipopt")
    results=opt.solve(m, tee=True)

    
    m.del_component(m.bounds)
    m.del_component(m.Obj)
    return m

__all__=["Particle"]

if __name__=="__main__":
    import sys

    A=Particle( float (sys.argv[1]) )
    A.pprint()

   
