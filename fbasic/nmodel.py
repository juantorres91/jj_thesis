import pyomo.environ as pe
import pyomo.opt as pot
import jj_thesis.Rheology as oldr

"""
Seccion (1) Definiciones basicas
Conjuntos: Fases / Condiciones de aplicacion
Parameteros: Densidad/ viscosidad nw / costo
Variables: Fraccion masica / shear rate / viscosidad 
Restricciones: Balance de masa
"""

# Nuevo modelo
datafile = 'basico.dat' 

m = pe.AbstractModel()  # Modelo de optimizacion

# Conjuntos
m.I = pe.Set(initialize = ['Wat', 'Oil', 'Thick', 'Surf'])  # Fases separadas
m.Pr = pe.Set(initialize = ['appli', 'mix'])                # Condiciones de proceso  

# Parametros
m.rho = pe.Param(m.I, default=0)   # Densidad [kg/m3]
m.dymu = pe.Param(m.I, default=0)  # Viscosidad dinamica [Pa.s]
m.cost = pe.Param(m.I, default=0)  # Costo unitario [$/kg]

m = m.create_instance(datafile)    # Creacion objeto modelo 

# Variables
def sr_bounds(m, i):  # Regla de limites de shear rate
    if i == 'appli':
        return (100, 100)
    else:
        return (100, 1200)
m.sr = pe.Var(m.Pr, bounds=sr_bounds)                      # Shear rate [s^-1]
m.xm = pe.Var(m.I, domain=pe.PositiveReals, bounds=(0,1))  # Fraccion masica [-]
m.mu_mix = pe.Var(m.Pr, domain=pe.PositiveReals)           # Viscosidad de mezcla [mPa.s]     

# Restricciones
def mass_bal_rule(m):
    return sum(m.xm[i] for i in m.I) == 1
m.mass_bal = pe.Constraint(rule = mass_bal_rule)


"""
Seccion 2 Operaciones avanzadas
Modelo de oldroyd
Distribucion de particulas d32
"""

def oldroyd_rule(m,i):
    if i == 'appli':
        return oldr.oldroyd_viscosity_model()
    else:
        return oldr.oldroyd_viscosity_model()
m.oldroyd = pe.Block(m.Pr, rule=oldroyd_rule)

m.oldroyd['mix'].pprint() 

