import pyomo.environ as pe
import pyomo.gdp as gdp

def turbulent_mix_rule(m):
    return m.m_time == 5.20 * (m.dt**1.5)*(m.H**0.5) / (m.di**2 * pow(m.Po, 0.3333334)  * m.N)  

def transition_mix_rule(m):
    return m.m_time == (183)**2 * (m.dt**1.5)*(m.H**0.5)*(m.mu)/(m.rho * pow(m.Po, 0.666667) * pow(m.N,2) * pow(m.di, 4) )  

# Generador
def premixing_model(Po = 0.1, rho = 997, mu = 0.001, di = 0.9, dt = 1, H = 1, model = 'turbulent' ,fx_pn = False):

    m = pe.ConcreteModel()  # Concrete model

    # Parameters
    m.di = pe.Param(initialize = di, mutable = True)
    m.dt = pe.Param(initialize = dt, mutable = True)
    m.H = pe.Param(initialize = H, mutable = True)
    
    # Variables
    m.rho = pe.Var(initialize = rho, within = pe.PositiveReals)  # Stream density 
    m.mu = pe.Var(initialize = mu, within = pe.PositiveReals)    # Stream viscosity
    m.Po = pe.Var(within = pe.PositiveReals, initialize = Po)    # Mixing Power number
    m.N = pe.Var(within = pe.PositiveReals)                      # Mixing rpm 
    m.m_time = pe.Var()                 # Mixibg time

    # Fix power number?
    if fx_pn:
        m.Po.fix(Po)

    # Selects the mixing rule (regime)
    if model == 'turbulent':
        m.mixing_eq = pe.Constraint(rule = turbulent_mix_rule)
    elif model == 'transition':
         m.mixing_eq = pe.Constraint(rule = transition_mix_rule)
    elif model == 'hybrid':
        # Disjunctions - Blocks
        m.re_turbulent = gdp.Disjunct()
        m.re_transition = gdp.Disjunct()

        # Disjuntion constraints
        m.re_turbulent.mixing_eq = pe.Constraint(expr = turbulent_mix_rule(m))
        m.re_transition.mixing_eq = pe.Constraint(expr = transition_mix_rule(m))
    
    return m    

if __name__ == "__main__":
    import sys
    m = premixing_model(model='hybrid')
    m.pprint()
