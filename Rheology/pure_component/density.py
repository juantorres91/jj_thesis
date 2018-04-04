import pyomo.environ as pe


__all__ = ['custom']


def custom(m, i):
    """
    Fixed density method
    """

    return m.rho[i] == m.rho_coef[i,0]



    
