import pyomo.environ as pe


def vnb_rule(m):
    """
    Estimate mixture viscosity form VNB method
    """

    g = pe.ConcreteModel()
    
