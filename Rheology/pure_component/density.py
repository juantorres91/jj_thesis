import pyomo.environ as pe


__all__ = ['custom']


def custom(m, i, value = 0):
    """
    Fixed density method
    """

    return m.rho[i] == v



    
