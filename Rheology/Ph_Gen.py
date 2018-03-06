from pyomo.environ import*
from pyomo.opt import SolverFactory

def model(data_file):

    m=AbstractModel()     #Model 
    g=Block()             #BLock
    
    #Sets
    m.C=Set()     #Fase Component

    # Active component 
    m.Hum=Set()   #Humectant set
    m.Ocl=Set()   #Ocluyent  set
    m.Emo=Set()   #Emolient  set
    m.Exf=Set()   #Exfoliant set 
    
    m.Oil=Set()   #Oil components 
    
    #Parameters

    m.EACN=  Param(m.C, default=18) #EACN 
    m.MW=   Param(m.C, default=1)   #Molecular weight 
    m.rho=  Param(m.C, default=1)   #Component density
    m.mu=   Param(m.C, default=1)   #Component kinematic viscocity
    m.cost= Param(m.C, default=0)   #Component cost [$/g]

    
    def vnb_def(m, i):
        return 14.534*log( log( m.mu[i]+0.8) ) +10.975
    m.vnb=Param(m.C, rule=vnb_def)                          #Viscosity blending number

    #Variables
    m.x=    Var(m.C, initialize=0.1, bounds=(0,1))          #Mass fraction [-]
    m.n=    Var(m.Hum | m.Exf , initialize=0.1)             #Humectant mol number [ mol/ g]
    
    m.oil=  Var()                                           #Total oil fraction

    m.TH=   Var(domain= PositiveReals)                      #Total humectant number [mol/g]
    m.kmu=  Var(initialize=1, domain=PositiveReals)         #Kinematic Viscosity [cSt]
    m.vnb_m=Var(initialize=5, domain=PositiveReals)         #Mixture VNB [-]
    m.den  =Var(initialize=1, domain=PositiveReals)         #Mixture density  [g/cm3]
    m.dymu =Var(initialize=2, domain=PositiveReals)         #Dynamic viscosity [P]
        
    m.Cost =Var(initialize=1, domain=PositiveReals)         #Fase cost
    
    #-----------------------------------------------------------
    #------------------------Constraints------------------------
    #-----------------------------------------------------------

    #Mass Fractions  -------------------------------
    def mass_balance(m):                                    #Fase mass balance
        return sum(m.x[i] for i in m.C)==1
    m.mass=Constraint(rule=mass_balance)

    
    #Humectant calculations    --------------------------------
    def n_def(m,i):                                          #Humectant Mol calculation
        if len(m.Hum | m.Exf)==0:
            return Constraint.Skip
        else:
            return m.n[i]==m.x[i]/m.MW[i]
    m.n_def=Constraint(m.Hum |m.Exf, rule=n_def)

    def TH_def(m):                                           #Total humectant mol calculation
        return m.TH==summation(m.n)
    m.TH_def=Constraint(rule=TH_def)

    #Viscosity equations ---------------------------------------
    def Oil_def(m):                                         #Oil and fat values
        return m.oil==sum(m.x[i] for i in m.Oil)
    m.Oil_def=Constraint( rule=Oil_def)
    
    def vnb_rule(m):                                         #VNB rule
        return sum(m.vnb[i]*m.x[i] for i in m.C)==m.vnb_m
    m.vnb_def=Constraint(rule=vnb_rule)

    def kmu_rule(m):                                         #Kinematic V
        return m.kmu==exp( exp((m.vnb_m-10.975)/14.534))-0.8
    m.kmu_def=Constraint( rule=kmu_rule)

    def mi_rho(m):                                           #Mixture rho
        return m.den*sum(m.x[i]/m.rho[i] for i in m.C)==1  
    m.rho_def=Constraint(rule=mi_rho)

    def dymu_def(m):                                         #Mixture dynamic viscosity
        return m.dymu==m.den*m.kmu/100
    m.dymu_def=Constraint(rule=dymu_def)

    #Cost calculations 
    def cost_cal(m):                                        # Cost Calculation
        return summation(m.cost,m.x)==m.Cost
    m.cost_cal=Constraint(rule=cost_cal)


    g= m.create_instance(data_file)

    return g

def Ph_model(data_file, x0=2):

    
    blo=model(data_file)
    blo.Obj=Objective(expr= (blo.dymu-x0)**2)
        
    opt=SolverFactory('ipopt')
    opt.solve(blo)
    #blo.pprint()

    blo.del_component(blo.Obj)

    #blo.pprint()
    return blo

if __name__=="__main__":
    import sys
    a=Ph_model(sys.argv[1],float( sys.argv[2]))
    a.pprint()

__all__= [ "Ph_model"]
