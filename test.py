import pyomo.environ as pe
from jj_thesis.Rheology import Chemical, Stream
import jj_thesis.Rheology.emulsion_models.viscosity as em_v
import jj_thesis.Rheology.emulsion_models.dp_size as dps
from pyomo.opt import SolverFactory

################################
# Master model
################################

m = pe.ConcreteModel() # Modelo integrado de diseno
opt = SolverFactory("ipopt")

# 
# Propiedades de fluidos


# Agua 
wat = Chemical(name = "wat")
wat.mu_parameters = {0 : 1}
wat.rho_parameters = {0: 1}

CPh = Stream()          # Fase continua  
CPh.add_chemical(wat)    

CPh.temperature = 298

# Metodos de prediccion
CPh.enable_viscosity_calculation()
CPh.enable_density_calculation()
CPh.activate_w_to_v()

CPh.initialize_mass_flow(80)

m.CPh = CPh

# Aceite
oil = Chemical(name = "oil")
oil.mu_parameters = {0 : 100}
oil.rho_parameters = {0 : 0.8}

DPh = Stream()

# Metodos de prediccion
DPh.add_chemical(oil)
DPh.enable_viscosity_calculation()
DPh.enable_density_calculation()

DPh.activate_w_to_v()

DPh.initialize_mass_flow(20)

m.DPh = DPh

# Restriccion balance de materia

# m.DPh.mass_flow.setlb()
# m.DPh.mass_flow.setlb()

DPh.mass_flow.setub(30)


def bal_const_rule(m):
    return m.DPh.mass_flow + m.CPh.mass_flow == 100
m.bal_const = pe.Constraint(rule = bal_const_rule)


# Inicializar corrientes 
opt.solve(CPh)
opt.solve(DPh)


#####################################
# Modelo de emulsion
#####################################
m.cd = pe.Set(initialize = ['prop', 'appl'])  # Conjunto de condiciones


############### Viscosidad de emulsion
m.mu = pe.Var(m.cd, domain = pe.PositiveReals)  # Emulsion viscosity 
###############


# Variables compartidas
m.vo = pe.Var(domain = pe.PositiveReals, bounds = (0,1))        # Fraccion volumetrica O/W
m.dM = pe.Var(domain = pe.PositiveReals)        # D32 [mu m]
m.ti = pe.Var(domain = pe.PositiveReals)        # Tension interfacial

m.k = pe.Var(m.cd, domain = pe.PositiveReals)   # Ratio de viscosidades 
m.Sr = pe.Var(m.cd, domain = pe.PositiveReals)  # Shear rate

# Variables fijas  y limites

m.Sr['appl'].fix(100)       # Shear rate
m.Sr['prop'].value = 1000   #

m.dM.setlb(3)
m.dM.setub(30)

m.ti.fix(20) 

###################################
# Modelos de viscosidad de emulsion
###################################

# Calculo de variables de ensamble
def vo_rule(m):
    return m.DPh.vol_flow == m.vo *(m.DPh.vol_flow + m.CPh.vol_flow)
m.vo_cons = pe.Constraint(rule = vo_rule)
m.vo.value = m.DPh.vol_flow.value / (m.CPh.vol_flow.value + m.DPh.vol_flow.value)

def k_rule(m,i):
    return m.DPh.Dmu == m.k[i]*m.CPh.Dmu
m.k_cons = pe.Constraint(m.cd, rule = k_rule)
for i in m.cd:
    m.k[i].value = m.DPh.Dmu.value / m.CPh.Dmu.value

# Bloques de Oldroyd

old_prop = em_v.oldroyd_viscosity_model(v0 = 0.3,
                                        k0 = m.k[i].value,
                                        c_mu0 = m.CPh.Dmu.value)
old_appl = em_v.oldroyd_viscosity_model(v0 = 0.3,
                                        k0 = m.k[i].value,
                                        c_mu0 = m.CPh.Dmu.value)


def oldy_rule(m,i):
    if i == 'prop':
        return old_prop
    else:
        return old_appl
m.oldy = pe.Block(m.cd, rule = oldy_rule)

    
#
# Restricciones de ensamble
m.split_cs = pe.ConstraintList()  # Lista de split constraints

for i in m.cd:

    m.split_cs.add(expr = m.vo == m.oldy[i].v)     # Fraccion volumetrica
    m.split_cs.add(expr = m.k[i] == m.oldy[i].k)    # V. Ratio
    m.split_cs.add(expr = m.dM == m.oldy[i].dD)     # D32
    m.split_cs.add(expr = m.Sr[i] == m.oldy[i].Sr)  # Shear rate
    m.split_cs.add(expr = m.ti == m.oldy[i].st)     # ow surface tension

# split de viscosidad
m.split_mu = pe.ConstraintList() 

for i in m.cd:
    m.split_mu.add(expr = m.mu[i] == m.oldy[i].mu)
    m.split_mu.add(expr = m.CPh.Dmu == m.oldy[i].c_mu)
   
 

#####################################
# Diametro de particula
####################################

m.dps = dps.h_k_model()

# Restricciones de ensamble

m.split_dp = pe.ConstraintList()

m.split_dp.add(expr = m.CPh.Rho == m.dps.c_den)
m.split_dp.add(expr = m.Sr['prop'] == m.dps.Sr)
m.split_dp.add(expr = m.ti == m.dps.st)
m.split_dp.add(expr = m.DPh.Dmu == m.dps.d_mu)

####
m.split_dp.add(expr = m.dM == m.dps.dD)

m.split_dp.pprint()


#########################
# Caso de estudio
########################333




m.obj = pe.Objective(expr = -m.mu["appl"])
opt.solve(m, tee = True)

#m.CPh.pprint()
