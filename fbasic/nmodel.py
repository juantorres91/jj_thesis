import pyomo.environ as pe
import pyomo.opt as pot

# Nuevo modelo

datafile = 'basico.dat' 

m = pe.AbstractModel()  # Modelo de optimizacion

# Conjuntos
m.I = pe.Set(initialize = ['Wat', 'Oil', 'Thick', 'Surf'])
m.Pr = pe.Set(initialize = ['appli', 'mix'])


# Parametros
m.rho = pe.Param(m.I, default=0)   # Densidad [kg/m3]
m.dymu = pe.Param(m.I, default=0)  # Viscosidad dinamica [Pa.s]
m.cost = pe.Param(m.I, default=0)  # Costo unitario [$/kg]

m = m.create_instance(datafile)

# Variables

def sr_bounds(m, i):  # Regla de limites de shear
    if i == 'appli':
        return (100, 100)
    else:
        return (100, 1200)
m.sr = pe.Var(m.Pr, bounds=sr_bounds)                      # Shear rate [s^-1]
m.xm = pe.Var(m.I, domain=pe.PositiveReals, bounds=(0,1))  # Fraccion masica [-]
m.mu_mix = pe.Var(m.Pr, domain=pe.PositiveReals)           # Viscosidad de mezcla [mPa.s]     

# Restricciones
def mass_bal_rule(m,):
    return sum(m.xm[i] for i in m.I) == 1
m.mass_bal = pe.Constraint(rule = mass_bal_rule)


m.pprint()
