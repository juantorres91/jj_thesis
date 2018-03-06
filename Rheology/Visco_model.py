from pyomo.environ import*
from pyomo.opt     import SolverFactory

def model(v0=0.3, k0=0.3, cmu=0.01, Sr0=100,st0=13, d0=4, mu0=10 ):

    """Ordoyold viscosity analysis"""

    m=ConcreteModel()
    b=Block()
    #--------------------------------------------------------
    #Parameters----------------------------------------------
    #--------------------------------------------------------

    l10=(19*k0+16)*(2*k0+3)/(40*(k0+1))*(1+(19*k0+16)*v0/(5*(k0+1)*(2*k0+3)))    #l1 initialization
    l20=(19*k0+16)*(2*k0+3)/(40*(k0+1))*(1-3*(19*k0+16)*v0/(10*(k0+1)*(2*k0+3))) #l2 initializatiom
    Nca0=1e-4*cmu*d0*Sr0/ (2*st0)   #Capilarity iniialization
    y10=(1+(5*k0+2)*v0/(2*(k0+1))+(5*k0+2)**2/(10*(k0+1)**2))*v0**2              #Y1 initialization
    y20=(1+l10*l20*Nca0**2)/(1+l10**2*Nca0**2)                                   #Y2 initialization

    
    
    #--------------------------------------------------------
    #Variables-----------------------------------------------
    #--------------------------------------------------------

    #Oldroyod Variables
    m.l1=Var(initialize=l10) #O parameter l1
    m.l2=Var(initialize=l20) #O parameter l2
    m.Nca=Var(domain=PositiveReals, initialize=Nca0)#Capilarity number [-]

    m.y1=Var(domain=PositiveReals, initialize=y10)  #Oldroyod y1
    m.y2=Var(domain=PositiveReals, initialize=y20)  #Oldroyod y1
    
    #Shared variables
    m.Sr=Var(initialize=Sr0, bounds=(1e1, 1e7))    #Shear rate [s-1]
    m.st=Var(initialize=st0, bounds=(3, 100))      #I. Tension [mN/m]
    m.dD=Var(initialize=d0,  bounds=(0.5,100))     #Dropplet size [1e-6 m]

    m.v=Var(bounds=(0.001, 0.7), initialize=v0)       #Oil volume fraction [-]
    m.k=Var(bounds=(1e-7, 30), initialize=k0)         #Viscosity ratio [-]
    m.c_mu=Var(domain=PositiveReals, initialize=cmu)  #Continuous phase dynamic viscosity [P]
    m.mu=Var(domain=PositiveReals, initialize=mu0)    #Emulsion phase dynamic viscosity [P]
    
        
    #--------------------------------------------------------
    #Constraints----------------------------------------------
    #--------------------------------------------------------
    
    def l1_def(m):             #L1 equation
        return m.l1==(19*m.k+16)*(2*m.k+3)/(40*m.k+40)*(1+(19*m.k+16)*m.v/(5*(m.k+1)*(2*m.k+3))  )
    m.l1_def=Constraint(rule=l1_def)
    
    def l2_def(m):             #L2  equation
        return m.l2==(19*m.k+16)*(2*m.k+3)/(40*m.k+40)*(1-3*(19*m.k+16)*m.v/(10*(m.k+1)*(2*m.k+3)))
    m.l2_def=Constraint( rule=l2_def)

    def y1_def(m):             #Oldroyod 1 def
        return m.y1==1+(5*m.k+2)*m.v/(2*(m.k+1))+ pow(5*m.k+2,2)*pow(m.v,2)/(10*pow(m.k+1,2))
    m.y1_def=Constraint(rule=y1_def)
        
    def y2_def(m):             #Oldroyod 2 def
        return m.y2==(1+m.l1*m.l2*pow(m.Nca,2))/(1+ pow(m.l1,2)*pow(m.Nca,2))
    m.y2_def=Constraint(rule=y2_def)

    def Nca_def(m):            #Capilarity definition
        return m.Nca*(2*m.st)==1e-4*m.c_mu*m.dD*m.Sr
    m.Nca_def=Constraint(rule=Nca_def) 

    def mu_def(m):             #Viscosity equation 
        return m.mu== m.c_mu*m.y1*m.y2
    m.mu_def=Constraint(rule=mu_def)    


        
    #--------------------------------------------------------
    #Block Construction--------------------------------------
    #--------------------------------------------------------
    b=m
    return b


def mu_model(v0=0.1, k0=0.3, cmu=0.01, Sr0=100,st0=13, d0=4, mu0=10):

    m=model(v0, k0, cmu, Sr0,st0, d0, mu0)

    #Bounds
    m.bounds=ConstraintList()
    
    m.bounds.add(expr= m.v==v0)
    m.bounds.add(expr= m.k==k0)
    m.bounds.add(expr= m.c_mu== cmu)
    m.bounds.add(expr= m.Sr==Sr0)
    m.bounds.add(expr= m.st==st0)
    m.bounds.add(expr= m.dD==d0)

        
    opt=SolverFactory('ipopt')
    results=opt.solve(m)
    m.del_component(m.bounds)
    
    
    return m


__all__=['mu_model']

if __name__=="__main__":
    import sys

    m=mu_model()
    m.pprint()
