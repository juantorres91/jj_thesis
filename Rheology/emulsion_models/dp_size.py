import pyomo.environ as pe
from pyomo.opt import SolverFactory
__all__ = ['h_k_model']


_fixvar = ['c_den', 'st', 'd_mu']


def initialize_model (m, disp = False):
    """ Initializes drop 
    """

    #Fixed Variables
    m.bounds = pe.ConstraintList()

    for i in _fixvar:

        try:
            m.bounds.add(expr = m.getattr(i) == m.getattr(m).value)

        except:
            pass
        
    m.Obj = pe.Objective(expr= pow(5 -m.dD,2))

    # Solver

    opt = SolverFactory("ipopt")
    opt.solve(m, tee = disp)

    
    m.del_component(m.bounds)
    m.del_component(m.Obj)
    return m

def h_k_model(ks = 11, d_I = 0.06, den = 1.1, st0 = 20, mu0=100, disp = False):

    """
    Hinze - Kolmogorov drop model
    """
    
    m = pe.ConcreteModel()

    #
    # Parameters 
    #
   
    m.ks = pe.Param(default = ks)      # Otto Metzner Constant 
    m.A_t = pe.Param(default = 0.54)   # Davis- Hinze Kolmogorov [1]
    m.A_n = pe.Param(default = 4.1)    # Davis- Hinze Kolmogorov [2]
    m.D_I = pe.Param(default = d_I)    # Imperler Diameter [m]

    #
    # Variables
    #
    
    m.Ep = pe.Var(domain=pe.PositiveReals, initialize=30)                   # Energy dissipation [W/kg] 
    m.dKI = pe.Var(domain=pe.PositiveReals, initialize=5)                   # Dimensional group [m]
    m.dD = pe.Var(domain=pe.PositiveReals, initialize=20, bounds=(1, 100))  # D32  [1e-6 m]

    #
    # Shared Variables
    #
    
    m.c_den = pe.Var(domain=pe.PositiveReals, initialize=den)   # Continuos phase viscosity [g/cm3]
    m.Sr = pe.Var(domain=pe.PositiveReals, initialize=100)      # Shear rate [s-1]
    m.N = pe.Var(initialize=4, bounds=(1e-3, 1000))             # Revolution Number  [s-1]
    m.st = pe.Var(domain=pe.PositiveReals, initialize=st0)      # S.Tension [mN/m]
    m.d_mu = pe.Var(domain=pe.PositiveReals, initialize=mu0)    # Disperse phase dynamic viscosity [P]
              
    #
    # Constraints
    #
    
    def Sh_def(m):        # Shear rate definition
        return m.Sr == m.ks*m.N
    m.Sh_def = pe.Constraint(rule=Sh_def)

    def Ep_def(m):       # Dissipation definition
            return m.Ep == 0.407*pow(m.N,3)*m.D_I**2
    m.Ep_def = pe.Constraint(rule=Ep_def)

    def dKI_def(m):      # dKI definition
        return m.dKI == (m.Ep**(-0.4))*( (1e-3*m.st)**(0.6))*((1e3*m.c_den)**(-0.6))
    m.dKI_def = pe.Constraint(rule=dKI_def)

    def dD_def(m):                              #Particle constraint
        return 1e-6*m.dD == m.A_t*(1+m.A_n*(0.1*m.d_mu)*m.Ep**(0.33333) *(1e-6*m.dD)**(0.3333)/(1e-3*m.st))**0.6*m.dKI  
    m.dD_def = pe.Constraint(rule=dD_def)

    return initialize_model(m, disp)
    

   
