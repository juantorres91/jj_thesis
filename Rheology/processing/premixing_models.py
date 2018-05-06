import pyomo.environ as pe


def turbulent_mix_time(Po = 0.1, di = 0.9, dt = 1, H = 1, fx_pn = True):

    """
    Estimates stream mixing time via turbulent model
    Parameters
    ----------

    Po : [-]
       Power number
    di : [m]
       Impeler diameter
    dt :[m]
       Tank diameter
    H : [m]
       Liquid height
    """
    
    m = pe.ConcreteModel()
    
    # Parameters
    m.di = pe.Param(initialize = di, mutable = True)
    m.dt = pe.Param(initialize = dt, mutable = True)
    m.H = pe.Param(initialize = H, mutable = True)

    # Variables
    m.Po = pe.Var(within = pe.PositiveReals, initialize = Po)  # Mixing Power number
    m.N = pe.Var(within = pe.PositiveReals)                    # Mixing rpm 
    m.m_time = pe.Var(within = pe.PositiveReals)               # Mixibg time
    
    if fx_pn:
        m.Po.fix(Po)


    # Constraint
    def mixing_rule(m):
        return m.m_time == 5.20 * (m.dt**1.5)*(m.H**0.5) / (m.di**2 * m.Po ** (1/3) * m.N)  

    m.mixing_const = pe.Constraint(rule = mixing_rule)
    
    return m



def transition_mix_time(Po = 0.1, rho = 997, miu = 0.001, di = 0.9, dt = 1, H = 1, fx_pn = True):

    """
    Estimates stream mixing time via transition model
    Parameters
    ----------

    Po : [-]
       Power number
    rho: [kg/m3]
       Density
    miu: [Pa*s]
       Viscosity
    di : [m]
       Impeler diameter
    dt :[m]
       Tank diameter
    H : [m]
       Liquid height
    """
    
    m = pe.ConcreteModel()
    
    # Parameters
    m.rho = pe.Param(initialize = rho, mutable = True)
    m.miu = pe.Param(initialize = miu, mutable = True)
    m.di = pe.Param(initialize = di, mutable = True)
    m.dt = pe.Param(initialize = dt, mutable = True)
    m.H = pe.Param(initialize = H, mutable = True)
    
    # Variables
    m.Po = pe.Var(within = pe.PositiveReals, initialize = Po)  # Mixing Power number
    m.N = pe.Var(within = pe.PositiveReals)                    # Mixing rpm 
    m.m_time = pe.Var(within = pe.PositiveReals)               # Mixibg time
    
    if fx_pn:
        m.Po.fix(Po)


    # Constraint
    def mixing_rule(m):
        return m.m_time == (183)**2 * (m.dt**1.5)*(m.H**0.5)*(m.miu)/(m.rho * m.N**2 * m.di**4 + m.Po**(2/3))  

    m.mixing_const = pe.Constraint(rule = mixing_rule)
    
    return m


if __name__ == "__main__":
    import sys
    m = turbulent_mix_time()
    m.pprint()
