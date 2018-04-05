import pyomo.environ as pe

__all__ = ['mass_balance_rule',
           'molar_balance_rule',
           'volume_balance_rule',
           'w_to_v_rule']


def mass_balance_rule(m):
    """
    Mass balance constraint
    """
    if len(m.comp) > 0:
        return sum(m.xw[i] for i in m.comp) == 1
    else:
        print "WARNING: " 
        return pe.Constraint.Skip
    
def molar_balance_rule(m):
    """
    Molar balance constraint
    """
    if len(m.comp) > 0:
        return sum(m.xm[i] for i in m.comp) == 1
    else:
        print "WARNING "
        return pe.Constraint.Skip

def volume_balance_rule(m):
    """
    Volume balance constraint
    """
    if len(m.comp) > 0:
        return sum(m.vf[i] for i in m.comp) == 1
    else:
        print "WARNING "
        return pe.Constraint.Skip

def w_to_v_rule(m):
    """
    Estimates the volume flow from mass flo
    """

    return m.vol_flow == m.mass_flow * m.Rho
