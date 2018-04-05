from pyomo.opt import SolverFactory
import pyomo.environ as pe 

__all__ = ['oldroyd_viscosity_model',
           'yaron_viscosity_model'] 

# Shared parameters

atr = ['v', 'k', 'c_mu',
       'Sr', 'st', 'dB']  # List of commom fixed variables


def initialize_model(m, disp = False):

    """
    Initializes viscosity models  
   
    Returns
    -------
    m : Concrete model
    """

    # Initializaion parameters
    m.bounds = pe.ConstraintList()

    for i in atr:
        try :
            m.bounds.add(expr = getattr(m,i) == getattr(m,i).value)

        except :
            pass 

    opt = SolverFactory('ipopt')  # Solver
    opt.solve(m, tee=disp)        # Initialize
    m.del_component(m.bounds)     # Delets initial specification 
    
    return m



def oldroyd_viscosity_model(v0=0.3, k0=0.3, c_mu0=0.01, st0=13, dD0=4, mu0=10, Sr0=100, disp = False):

    """
    Oldroyd viscosity model

    Parameters
    ----------
    v0 : float
       Intial volume fraction
    k0 : float
       Initial viscosity ratio
    c_mu0 : float
       Initial continous phase viscosity [P]
    
    mu0 : float
       Initial emulsion viscosity [P]
    
    dD0 : float
       Initial drop diameter
    Sr0 : float
       Initial shear rate [-] 

    Returns
    -------
    m : Concrete model
    """

    m = pe.ConcreteModel() # Oldroyd model 

    #
    # Intialization parameters
    #
    
    l10 = (19*k0+16)*(2*k0+3)/(40*(k0+1))*(1+(19*k0+16)*v0/(5*(k0+1)*(2*k0+3)))     # l1 initialization
    l20 = (19*k0+16)*(2*k0+3)/(40*(k0+1))*(1-3*(19*k0+16)*v0/(10*(k0+1)*(2*k0+3)))  # l2 initializatiom
    Nca0 = 1e-4*c_mu0*dD0*Sr0/(2*st0)                                               # Capilarity number iniialization
    y10 = (1+(5*k0+2)*v0/(2*(k0+1))+(5*k0+2)**2/(10*(k0+1)**2))*v0**2               # Y1 initialization
    y20 = (1+l10*l20*Nca0**2)/(1+l10**2*Nca0**2)                                    # Y2 initialization

    #
    # Variables 
    #
    
    # Oldroyod Variables
    m.l1 = pe.Var(initialize=l10)  # Oldroyd parameter l1
    m.l2 = pe.Var(initialize=l20)  # Oldroyd parameter l2
    m.Nca = pe.Var(domain=pe.PositiveReals, initialize=Nca0)  # Capilarity number [-]

    m.y1 = pe.Var(domain=pe.PositiveReals, initialize=y10)  # Oldroyod y1
    m.y2 = pe.Var(domain=pe.PositiveReals, initialize=y20)  # Oldroyod y1
    
    # Shared variables
    m.Sr = pe.Var(initialize=Sr0, bounds=(1e1, 1e7))  # Shear rate [s-1]
    m.st = pe.Var(initialize=st0, bounds=(3, 100))    # I.Tension [mN/m]
    m.dD = pe.Var(initialize=dD0, bounds=(0.5,100))   # Dropplet size [1e-6 m]

    m.v = pe.Var(bounds=(0.001, 0.7), initialize=v0)       # Oil volume fraction [-]
    m.k = pe.Var(bounds=(1e-7, 300), initialize=k0)         # Viscosity ratio [-]
    m.c_mu = pe.Var(domain=pe.PositiveReals, initialize=c_mu0)  # Continuous phase dynamic viscosity [P]
    m.mu = pe.Var(domain=pe.PositiveReals, initialize=mu0)    # Emulsion phase dynamic viscosity [P]
    
    #
    # Constraints
    #
    
    def l1_def(m):  # L1 equation
        return m.l1 == (19*m.k+16)*(2*m.k+3)/(40*m.k+40)*(1+(19*m.k+16)*m.v/(5*(m.k+1)*(2*m.k+3)))
    m.l1_def = pe.Constraint(rule=l1_def)
    
    def l2_def(m):  # L2  equation
        return m.l2 == (19*m.k+16)*(2*m.k+3)/(40*m.k+40)*(1-3*(19*m.k+16)*m.v/(10*(m.k+1)*(2*m.k+3)))
    m.l2_def = pe.Constraint(rule=l2_def)

    def y1_def(m):  # Oldroyod 1 def
        return m.y1 == 1+(5*m.k+2)*m.v/(2*(m.k+1))+pow(5*m.k+2,2)*pow(m.v,2)/(10*pow(m.k+1,2))
    m.y1_def = pe.Constraint(rule=y1_def)
        
    def y2_def(m):  # Oldroyod 2 def
        return m.y2==(1+m.l1*m.l2*pow(m.Nca,2))/(1+pow(m.l1,2)*pow(m.Nca,2))
    m.y2_def=pe.Constraint(rule=y2_def)

    def Nca_def(m):  # Capilarity definition
        return m.Nca*(2*m.st) == 1e-4*m.c_mu*m.dD*m.Sr
    m.Nca_def = pe.Constraint(rule=Nca_def) 

    def mu_def(m):   # Viscosity equation 
        return m.mu == m.c_mu*m.y1*m.y2
    m.mu_def = pe.Constraint(rule=mu_def)    

    return initialize_model(m, disp)


def yaron_viscosity_model(v0=0.3, c_mu0=0.01, mu0=1, k0=0.3,):

    """
    Pal viscosity model

    Parameters
    ----------
    v0 : float
       Intial volume fraction
    k0 : float
       Initial viscosity ratio
    c_mu0 : float
       Initial continous phase viscosity [Pa.s]
    mu0 : float
       Initial emulsion  viscosity [Pa.s]
    
    Returns
    -------
    m : Concrete model
      Initialized model
    """

    m = pe.ConcreteModel() # Yaron viscosity model 

    #
    # Variables 
    #

    # Dummy variables
    m.lamb = pe.Var(domain = pe.PositiveReals) # ^1/3 oil fracton root
    
    # Shared variables
    m.v = pe.Var(bounds=(0.001, 0.7), initialize=v0)          # Oil volume fraction [-]
    m.k = pe.Var(bounds=(1e-7, 30), initialize=k0)            # Viscosity ratio [-]
    m.c_mu = pe.Var(domain=pe.PositiveReals, initialize=cmu)  # Continuous phase dynamic viscosity [P]
    m.mu = pe.Var(domain=pe.PositiveReals, initialize=mu0)    # Emulsion phase dynamic viscosity [P]

    
    
    #
    # Constraints
    #

       
    return m


if __name__ == '__main__':
    import sys
    m = oldroyd_viscosity_model(disp=False)
    m.pprint()
