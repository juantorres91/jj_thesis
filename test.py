import pyomo.environ as pe
from jj_thesis.Rheology import Chemical, Stream


wat = Chemical(name = "wat")
wat.mu_parameters = {0 : 0.1, 1: 3}
wat.rho_parameters = {0: 1}

# wat.viscosity_model = 'arrheniusype'

oil = Chemical(name = "oil")
oil.mu_parameters = {0 : 0.1}
oil.rho_parameters = {0 : 0.8}

F1 = Stream()
F1.add_chemical(wat)
F1.add_chemical(oil)


F1.enable_mass_balance()
F1.enable_viscosity_calculation()
F1.enable_density_calculation()

#F1.pprint() 
F2 = Stream()
F2.add_chemical(wat)
F2.enable_viscosity_calculation()

F2.temperature = 298

print F2.viscosity

#F2.pprint()
