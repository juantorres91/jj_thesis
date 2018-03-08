import pyomo.environ as pe

__all__ = ['mass_balance_rule', 'molar_balance_rule']


def mass_balance_rule(m):
    """
    Mass balance constraint
    """
    if len(m.comp) > 0:
        return sum(m.xw[i] for i in m.comp) == 1
    else:
        return pe.Constraint.Skip
    
def molar_balance_rule(m):
    """
    Molar balance constraint
    """
    return sum(m.xm[i] for i in m.comp) == 1


