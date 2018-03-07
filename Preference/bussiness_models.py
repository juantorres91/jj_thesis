import pyomo.environ as pe
from pyomo.opt import SolverFactory

__all__ = ['elastic_model']



def elastic_model(h1,a=1,rho=0.5, p2= 0.0150, Y=8648277.12955084, h2=6348.615200000):

    m = ConcreteModel()  # Pyomo model

    #
    # Parameters
    #
    
    m.a = pe.Param(default=a)      # Product Awareness [-]
    m.rho = pe.Param(default=rho)  # Market elasticity [-]
    m.H2 = pe.Param(default=h2)    # Competition preference [-]
    m.p2 = pe.Param(default=p2)    # Competence price [$]
    m.Y = pe.Param(default=Y)      # Market total budget 
    m.D = pe.Param(default=Y/p2)   # Total product demand

    #
    # Variable initalization
    # 
    gao = (a/(h2/h1))**(rho/(rho+1))

    # 
    # Variables
    #
    
    m.d1 = pe.Var(domain=PositiveReals, initialize=m.Y/2)   # Competence demand
    m.d2 = pe.Var(domain=PositiveReals, initialize=m.Y/2 )  # Product demand
    m.p1 = pe.Var(domain=PositiveReals, initialize=m.p2)    # Product price

    m.H1 = pe.Var(domain=PositiveReals, initialize=h1)      # Product preference 
    m.b =  pe.Var(domain=PositiveReals, initialize=h2/h1, bounds=(0.5, 2))   #Preference ratio
    m.ga = pe.Var(domain=PositiveReals, initialize=gao)     # Parameter gamma
    m.U = pe.Var(domain=PositiveReals, initialize=m.Y/2) 

    #
    #Constraints
    #
    
    def su_mod(m):  # Economic model definition
        return m.p1*m.d1==(m.a*m.b)**m.rho*( m.U)**(1-m.rho)*m.d1**m.rho
    m.su_mod = pe.Constraint(rule=su_mod)

    def h_def(m):   # Preference ratio definition
        return m.b==m.H1/m.H2
    m.h_def = pe.Constraint(rule=h_def)

    def d2_def(m):  # Product demand definition
        return m.U*m.p2==(m.Y-m.d1*m.p1)
    m.d2_def = pe.Constraint(rule=d2_def)

    def TD_cons(m): # Total demand constraint
        return m.D==m.d1+m.d2
    m.TD_cons = pe.Constraint(rule=TD_cons)

    def d1_def(m):  # D1 definition
        return m.d1==m.D/(1+m.ga)
    m.d1_def = pe.Constraint(rule=d1_def)

    def ga_def(m):  # Gamma definition
        return m.ga==(m.a/m.b)**(m.rho/(m.rho-1))
    m.ga_def = pe.Constraint(rule=ga_def) 

    return m 

def bu_model(h1):

    m=model(h1)

    m.hlim = pe.ConstraintList()
    m.hlim.add(expr= m.H1==h1)

    opt=SolverFactory('bonmin')

    retults=opt.solve(m, )

    m.del_component(m.hlim)
    return m


