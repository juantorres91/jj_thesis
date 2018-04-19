from pyomo.environ import*
from pyomo.opt     import SolverFactory

def model(h1,a=1,rho=0.75, p2= 0.1205, Y=8648277.12955084, h2=7133.97106065432):

    m=ConcreteModel()
    g=Block()

    #Parameters
    m.a=Param(default=a)       #Product Awareness
    m.rho=Param(default=rho)   #Market elasticity
    m.H2=Param(default=h2)     #Competition preference
    m.p2=Param(default=p2)     #Competence price
    m.Y =Param(default=Y)      #Market total budget
    m.D= Param(default=Y/p2)   #Total demand

    
    #Var initalization

    gao=(a/(h2/h1))**(rho/(rho+1))

    
    
    #Variables
    m.d1=Var(domain=PositiveReals, initialize=m.Y/2)   #Competence demand
    m.d2=Var(domain=PositiveReals, initialize=m.Y/2 )  #Product demand
    m.p1=Var(domain=PositiveReals, initialize=m.p2)    #Product price

    m.H1=Var(domain=PositiveReals, initialize=h1)      #Product preference 
    m.b= Var(domain=PositiveReals, initialize=h2/h1, bounds=(0.5, 2))   #Preference ratio
    m.ga=Var(domain=PositiveReals, initialize=gao)     #Parameter gamma

    m.U=Var(domain=PositiveReals, initialize=m.Y/2) 
    
    #Constraints

    def su_mod(m):             #Economic model definition
        return m.p1*m.d1==(m.a*m.b)**m.rho*( m.U)**(1-m.rho)*m.d1**m.rho
    m.su_mod=Constraint(rule=su_mod)

    def h_def(m):              #Preference ratio definition
        return m.b==m.H1/m.H2
    m.h_def=Constraint(rule=h_def)

    def d2_def(m):             #Product demand definition
        return m.U*m.p2==(m.Y-m.d1*m.p1)
    m.d2_def=Constraint(rule=d2_def)

    def TD_cons(m):            #Total demand constraint
        return m.D==m.d1+m.d2
    m.TD_cons=Constraint(rule=TD_cons)

    def d1_def(m):             #D1 definition
        return m.d1==m.D/(1+m.ga)
    m.d1_def=Constraint(rule=d1_def)

    def ga_def(m):             #Gamma definition
        return m.ga==(m.a/m.b)**(m.rho/(m.rho-1))
    m.ga_def=Constraint(rule=ga_def) 

    #Block definition
    g=m
    
    return g 

def bu_model(h1):

    m=model(h1)

    m.hlim=ConstraintList()
    m.hlim.add(expr= m.H1==h1)

    opt=SolverFactory('scip')

    retults=opt.solve(m, )

    m.del_component(m.hlim)
    return m


__all__=['bu_model']


if __name__=='__main__':

    import sys
    m=bu_model(float(sys.argv[1]))
    m.pprint()
    
