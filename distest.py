# import pyomo.core
import pyomo.environ as pe
import pyomo.gdp as gdp
from pyomo.opt import SolverFactory

m = pe.ConcreteModel()

# VAriables
m.x1 = pe.Var(within = pe.PositiveReals)
m.x2 = pe.Var(bounds = (0, 5))

# Outter constraints
m.ocons = pe.Constraint( expr =m.x1**2 + m.x2**2 >= 2) 

# Disjuctions
m.Re1 = gdp.Disjunct()
m.Re2 = gdp.Disjunct()

m.Re1.x1_cons1 = pe.Constraint( expr = pe.exp(m.x1) >= pe.exp(2))
m.Re2.x1_cons2 = pe.Constraint( expr = m.x1 <= 1)

m.r1or2 = gdp.Disjunction(expr = [m.Re1, m.Re2])

# Objetivo
m.obj = pe.Objective( expr = 3*m.x1 + 4*m.x2)

#m.pprint()

# SOlucion

m.BigM = pe.Suffix(direction=pe.Suffix.LOCAL)
m.BigM[None] = 1000

bigM = pe.TransformationFactory("gdp.chull")
bigM.apply_to(m)

opt = SolverFactory("bonmin")
opt.solve(m, tee = True)

m.pprint()
