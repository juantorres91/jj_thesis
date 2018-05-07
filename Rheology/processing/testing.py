import pyomo.environ as pe
import pyomo.gdp as gdp
from premixing_models import premixing_model

m = pe.ConcreteModel()
m.pre_mix = premixing_model(model = 'hybrid')


m.Reynolds = pe.Var(within = pe.PositiveReals)

# Disjunts
m.pre_mix.re_turbulent.re_cons = pe.Constraint(expr = m.Reynolds >= 1e4)
m.pre_mix.re_transition.re_cons = pe.Constraint(expr = m.Reynolds <= 9e3)

# Disjuntions
m.regim = gdp.Disjunction(expr = [m.pre_mix.re_turbulent, m.pre_mix.re_transition])  


m.BigM = pe.Suffix(direction=pe.Suffix.LOCAL)
m.BigM[None] = 1000

bigM = pe.TransformationFactory("gdp.bigm")
bigM.apply_to(m)

m.pprint()
