import chemical as ch
import pyomo.environ as pe

m = pe.ConcreteModel()
m.comp = pe.Set(initialize = ['a', 'b'])
m.dymu = pe.Var(m.comp)

m.T = pe.Var()


wat = ch.Chemical(name = 'wat')
wat.viscosity_model = 'power_law_type'


m.mu_const = pe.ConstraintList()

for i in m.comp:
    m.mu_const.add( wat.get_viscosity_model()(m,i))
if __name__ == '__main__':

    print wat.viscosity_model
    m.pprint()
