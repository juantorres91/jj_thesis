from pyomo.environ import*
from pyomo.opt import*
from math import pi
from Tesis.Molecular import*
from Tesis.Rheology import*
from Tesis.Preference import*

#------------------------------------------------------------------------------------------------------------------
#                            S. 1  Model Blocks Definition
#------------------------------------------------------------------------------------------------------------------

m=ConcreteModel() #Model object

con_file='./Rheology/Cont.dat'
dis_file='./Rheology/Disp.dat'
surf_file='./Molecular/InputTable.xlsx'
pref_file='./Preference/Pref2.dat'

surf=MoleBlock(surf_file)
def Surf_Gen(m):
    return surf
m.surf=Block(rule=Surf_Gen) #Surfactant block genertator

#Model Initialization
con= Ph_model(con_file, 0.01)   #Continous phase block 
dis= Ph_model(dis_file, 0.5)    #Disperse phase blocks

#Product phases and components
m.Ph=Set(initialize={'cont','disp', 'surf', 'Thick'})
def blo_init(m,i):                                    #Block indexing initialization
    if i=='cont':
        return con
    else:
        return dis
m.blo=Block(['cont','disp'], rule=blo_init)

#Preference block
m.pref=piece_model(pref_file)                           #Preference block integration

#------------------------------------------------------------------------------------------------------------------
#                            S. 2  Phase variables and bounds
#------------------------------------------------------------------------------------------------------------------

#Initialization rules and parameters

m.T_Rho=Param(initialize=1.5)  #Thickener Density [g/cm3]

def mass_bound(m,i):           #Mass initialization rule 
    if i =='cont':
        return (40, 90)
    elif i=='disp':
        return (0.5, 35)
    elif i=='Thick':
        return (0.001,3)
    else :
        return (0.05,15)
    
def mass_ini(m,i):             #Mass initialization rule
    if i=='cont':
        return 80
    elif i=='disp':
        return 20
    elif i=='Thick':
        return 2
    else:
        return 10

def vol_ini(m,i):             #Volume initialization rule
    return m.mass[i].value

#Variables--------------------------------------------------------------
m.mass=Var(m.Ph, initialize=mass_ini, bounds=mass_bound)            #Fase Total Mass [g]
m.vol= Var(m.Ph, initialize=vol_ini, domain=PositiveReals)          #Fase total volume [cm**3]
m.tvol=    Var(domain=PositiveReals, initialize=100)                #Total volume   [cm3]
m.surf_rho=Var(domain=PositiveReals, initialize=1, bounds=(1,1))    #Surfactant density [g/cm3]
m.t_den=   Var(domain=PositiveReals, initialize=1, bounds=(0.5,5))  #Total density  [g/cm3]

#Water Concentration limits--------------------------------------------- 
m.blo['cont'].x['Wat'].setlb(0.6)                                   #Water lower bound [-]
m.blo['cont'].x['Wat'].setub(0.95)                                  #Water upper bound [-]

#------------------------------------------------------------------------
# Component type limits
#------------------------------------------------------------------------

m.Sol=Var(domain=PositiveReals, bounds=(65,75))     #Total solvent mass
m.Hum=Var(domain=PositiveReals, bounds=(0.05, 15))  #Total humectant mass
m.Ocl=Var(domain=PositiveReals, bounds=(0.1,  10))  #Total oclusive mass
m.Emo=Var(domain=PositiveReals, bounds=(0.05, 15))  #Total emolient mass
m.Exf=Var(domain=PositiveReals, bounds=(0.1, 1))    #Total Exfoliant mass

def Sol_Def(m):                                     # Total solvent mass definition
    return m.Sol==m.mass['cont']*m.blo['cont'].x['Wat']
m.Sol_Def=Constraint(rule=Sol_Def)

#-------------------------------------------------------------------------------------------
#                      S.3  Mass and Volume Balance  Definition
#-------------------------------------------------------------------------------------------

def m_bal(m):                     #Total mass balance               
    return sum(m.mass[i] for i in m.Ph)==100
m.m_bal=Constraint(rule=m_bal)

def v_def(m,i):                   #Volume definition
    if i=='Thick':
        return m.vol[i]==m.mass[i]/m.T_Rho
    elif i=='surf':
        return m.vol[i]==m.mass[i]/m.surf_rho
    else:
        return m.blo[i].den*m.vol[i]==m.mass[i]
m.v_def=Constraint(m.Ph, rule=v_def)

def Tv_def(m):                    #Total volume definition
    return summation(m.vol)==m.tvol
m.Tv_def=Constraint(rule=Tv_def)

def Rho_def(m):                   #Density definition
    return m.t_den==m.tvol/100
m.Rho_def=Constraint(rule=Rho_def) 

#Active compounds Constraints----------------------------------------------------------------

def Hum_Def(m): #Humectant mass definition
    return m.Hum==sum( m.mass[i]*m.blo[i].x[j] for i in ('cont', 'disp')  for j in m.blo[i].Hum)
m.Hum_Def= Constraint(rule=Hum_Def)

def Ocl_Def(m): #Oclusive mass definition
    return m.Ocl==sum( m.mass[i]*m.blo[i].x[j] for i in ('cont', 'disp')  for j in m.blo[i].Ocl)
m.Ocl_Def= Constraint(rule=Ocl_Def)

def Emo_Def(m): #Emolient mass definition
    return m.Emo==sum( m.mass[i]*m.blo[i].x[j] for i in ('cont', 'disp')  for j in m.blo[i].Emo)
m.Emo_Def= Constraint(rule=Emo_Def)

def Exf_Def(m): #Emolient mass definition
    return m.Exf==sum( m.mass[i]*m.blo[i].x[j] for i in ('cont', 'disp')  for j in m.blo[i].Exf)
m.Exf_Def= Constraint(rule=Exf_Def)

#------------------------------------------------------------------------------------------------------------------
#                            S. 4  Viscosity Evaluation
#------------------------------------------------------------------------------------------------------------------

#Sets---------------------
m.Cond=Set(initialize={'appli', 'mix'})  #Shear conditions


#---------------------------------------------------------
#Blocks 
#---------------------------------------------------------

#Drop size block
m.DpB=Particle(30, mu0=m.blo['disp'].dymu.value)

#Thickner models-----------------------

Cto=m.mass['Thick'].value*100/m.vol['cont'].value   #Thick initial concentration 
mix_t=Thick_model(Sro=m.DpB.Sr.value,Cto=Cto)   
app_t=Thick_model(Sro=1e2,Cto=Cto)

cdym_mix=m.blo['cont'].dymu.value*mix_t.Rel.value
cdym_app=m.blo['cont'].dymu.value*app_t.Rel.value

k_mix=cdym_mix/m.blo['disp'].dymu.value
k_app=cdym_app/m.blo['disp'].dymu.value


#Viscosity block model 
mix=mu_model( k0=k_mix,cmu=cdym_mix,v0=0.2, Sr0=m.DpB.Sr.value, d0=m.DpB.dD.value)
appli=mu_model(k0=k_app, v0=0.2, Sr0=1e2, cmu=cdym_app,d0=m.DpB.dD.value)

def Mu_Init(m,i):                        #Viscosity model initialization
    if i=='mix':
        return mix 
    else:
        return appli
m.Vis=Block(m.Cond, rule=Mu_Init)


#Thickner block model
def Thi_Init(m,i):
    if i=='mix':
        return mix_t 
    else:
        return app_t
m.Thick=Block(m.Cond, rule=Thi_Init)
    


#Parameter bounds-------
m.St0=Param(default=49.254)              #Specific Oil-Water Tension [nM/m]

def Sr_bounds(m,i):                      #Shear rate bounds 
    if i=='appli':
        return (1e2,1e2)
    else:
        return (1e0,1e7)

def Sr_init(m,i):                    #Shear rate initialization
    if i=='appli':
        return 1e2
    else:
        return m.DpB.Sr.value

def Dymu_init(m,i):
    if i=='appli':
        return 80
    else:
        return 0.01
    
#Variables--------------

m.st=Var(initialize=13)                                    #I. Tension [mN/m] 
m.N=Var( bounds=(1e0, 1e6) )                               #Revolution nuber [1/s]
m.dD=Var(domain=PositiveReals, initialize=m.DpB.dD.value)  #Dropplet size [micro meters]

m.Sr=Var(m.Cond, bounds=Sr_bounds, initialize=Sr_init)     #Shear rate[s-1]

m.v=Var(bounds=(0.0001, 1), initialize=0.2)                #Oil volume fraction [-]
m.k=Var(m.Cond, bounds=(1e-5, 1e2))                        #Viscosity ratio [-]

m.Rel =Var(m.Cond, domain=PositiveReals, initialize=1)     #Relative viscosity [-]
m.Ct  =Var(initialize=Cto, domain=PositiveReals )          #Thickener concentration [g/dL]
m.Cdymu=Var(m.Cond,domain=PositiveReals, rule=Dymu_init)   #Continuous phase dynamic viscosity [P]

#Constraints------------

def vfrac_def(m):                                       #Volume Fraction def
    return m.v*m.tvol==m.vol['disp']
m.vfrac_def=Constraint(rule=vfrac_def)

def krat_def(m,i):                                      #Viscosity ratio def
    return m.k[i]*m.Cdymu[i]==m.blo['disp'].dymu
m.krat_def=Constraint(m.Cond,rule=krat_def) 

def T_visc(m,i):                                        #Continous viscosity
    return m.Cdymu[i]==m.blo['cont'].dymu*m.Rel[i]
m.T_visc=Constraint(m.Cond, rule=T_visc)

def Ct_def(m):                                          #Thickener concentration definition
    return m.Ct==m.mass['Thick']*100/m.vol['cont']
m.Ct_def=Constraint(rule=Ct_def)           

def st_def(m):                                           #Interfacial tension definition
    return m.st==m.St0-m.surf.y['STR']
m.st_def=Constraint(rule=st_def)                            


#Equivalence relationship ----------------------------

#Continous density equivalence
m.c_den_eq=Constraint(expr= m.blo['cont'].den==m.DpB.c_den)

#Disperse ph vicosity equivalence
m.d_mu_eq=Constraint(expr= m.blo['disp'].dymu==m.DpB.d_mu)

#Shear Rate equivalence
m.Sr_equ=ConstraintList() 
m.Sr_equ.add(expr= m.Sr['mix']==m.DpB.Sr)

#N equivalence
m.N_equ=Constraint(expr= m.N==m.DpB.N ) 

#I.T equivalence
m.st_equ=ConstraintList()
m.st_equ.add(expr= m.st==m.DpB.st)

#dD equivalence
m.dD_equ=ConstraintList()
m.dD_equ.add(expr= m.dD==m.DpB.dD)

#Oil fraction
m.v_equ=ConstraintList()

#Viscosity ratio
m.k_equ=ConstraintList()

#Continuous viscosity
m.cvis_equ=ConstraintList()

#Thickener Rel
Rel_equ=ConstraintList()

#Thickener Concentration
Ct_eq=ConstraintList()

for i in m.Cond:
    #Shear rate
    m.Sr_equ.add(expr= m.Sr[i]==m.Vis[i].Sr)
    m.Sr_equ.add(expr= m.Sr[i]==m.Thick[i].Sr)

    #Surface tension 
    m.st_equ.add(expr= m.st==m.Vis[i].st)

    #Drop size
    m.dD_equ.add(expr= m.dD==m.Vis[i].dD)
    
    #Oil fraction
    m.v_equ.add(expr= m.v==m.Vis[i].v)

    #Viscosity ratio
    m.k_equ.add(expr= m.k[i]==m.Vis[i].k)

    #Continuous viscosity
    m.cvis_equ.add(expr= m.Cdymu[i]==m.Vis[i].c_mu) 

    #Thickener Rel
    Rel_equ.add(expr= m.Rel[i]==m.Thick[i].Rel)

    #Thickener Concentration
    Ct_eq.add(expr= m.Ct==m.Thick[i].Ct)

#----------------------------------------------------------------------------------------
#     S.5  Power evaluation and energy consumption
#----------------------------------------------------------------------------------------

#Parameters

Reo=1500
m.Re_t=Param(default=1505.4)    #T reynolds
m.Pk=  Param(default=0.355)     #Power constant
m.SW=  Param(default=0.3)       #Sigmoidal weight
m.D_I= Param(default=m.DpB.D_I) #Impeler diameter [m]

#Variables
m.Re=Var(initialize=400, bounds=(100,3000))  #Reynolds number
m.P= Var(initialize=0.4, bounds=(0.3, 4))    #Power number
m.w= Var(initialize=1,   bounds=(0,1))       #Weighting Function
m.P1=Var(initialize=1)                       #First complementarity equation

#Constraints

def we_def(m):       #Weight function
    return m.w==1/(1+exp(-m.SW*(m.Re_t-m.Re)))
m.we_def=Constraint(rule=we_def)

def P1_def(m):       #Power curve definition
    return m.P1==10.457*m.Re**-0.47
m.P1_def=Constraint(rule=P1_def)

def P_def (m):       #Power number definition
    return m.P==m.P1*m.w+(1-m.w)*m.Pk
m.P_def=Constraint(rule=P_def)

def Re_def(m):       #Reynolds definition 
    return m.Re*(0.1*m.Vis['appli'].mu) ==(1e3*m.t_den)*m.N*m.D_I**2
m.Re_def=Constraint(rule=Re_def)

#----------------------------------------------------------------------------------------
#     S.6 Surfactant properties evatluation 
#----------------------------------------------------------------------------------------

m.Smol=Var(domain=PositiveReals, initialize=1)                #Surfactant mol  []
m.SM=  Var( domain=PositiveReals, initialize=1)               #Surfactant molar concentration [M]

def mol_ammo(m):                                              #Surfactant mol number definition
    return m.Smol*m.surf.y['MW']==m.mass['surf'] 
m.mol_ammo=Constraint(rule=mol_ammo)                          

def SM_def(m):                                                #Surfactant concentration definition
    return m.SM==1e3*m.Smol/m.tvol
m.SM_def=Constraint(rule=SM_def)                           

def CMC_Const(m):                                             #CMC constraint
    return m.SM>=m.surf.y['CMC']
m.CMC_Const=Constraint(rule=CMC_Const)    


#-------------------------------------------------------------------------------------------
#                      S.7 Preference Evaluation
#-------------------------------------------------------------------------------------------

#Humectant ammount definition-------------------------------------------------------------------------------
m.Hmol=Var( initialize=100, domain=PositiveReals, bounds=(0,7000)) #Humecatant ammount [mmol/ cm**2]

def Hmol_def(m):
    return m.Hmol==2e4*sum(m.blo[i].TH*m.mass[i] for i in ('cont','disp'))
m.Hmol_def=Constraint(rule=Hmol_def)

#Greassiness definition--------------------------------------------------------------------------------------
m.Oil=Var( initialize=10, domain=PositiveReals) #Greassiness (mass %)

def Oil_def(m):
    return m.Oil==sum( m.blo[i].oil*m.mass[i] for i in ('cont', 'disp'))
m.Oil_def=Constraint(rule=Oil_def)

#Smoothness definition----------------------------------------------------------------------------------------
m.Fri0=Param(default=0.4)    #Default coefficient of friction
m.Fri= Var(initialize=0.7)   #New coefficient of friction

m.frCh=Var( initialize=0.8)  #% Change in coefficient of friction
m.Smo =Var(initialize=0.6)   #Smoothness

def frCh_def(m):              # Change Coeffient of friction definition
    return m.frCh==-0.0472*m.Oil+1.0606
m.frCh_def=Constraint(rule=frCh_def)

def Fri_def(m):               #Coefficient of friction definition
    return m.Fri==m.Fri0*(1+m.frCh)
m.Fri_def=Constraint(rule=Fri_def)

def Smo_def(m):               #Smoothness definition
    return m.Smo*m.Fri==0.5
m.Smo_def=Constraint(rule=Smo_def)

#Thickness definition-----------------------------------------------------------------------------------------
m.Thi=Var(initialize=13, domain=PositiveReals)

def Thic_def(m):
    return m.Thi==sqrt(m.Vis['appli'].mu)
m.Thic_def=Constraint(rule=Thic_def)


#Creamness definition------------------------------------------------------------------------------------------
m.Cream=Var(initialize=10, domain=PositiveReals)

def Cream_def(m):
    return m.Cream==(m.Thi**0.54)*(m.Smo**0.84)
m.Cream_def=Constraint(rule=Cream_def)

#Spreadibility definition---------------------------------------------------------------------
m.SA_T= Param(default=27)                                        #Skin Air Tension [mN / m]
m.LA_To=Param(default=72)                                        #Lotion Air Standart Surface Tension [mN/m]

m.LA_T=Var(domain=PositiveReals, initialize=30)                  #Lotion Air Surface Tension [mN/m]
m.LS_T=Var(domain=PositiveReals, initialize=2.7)                 #Lotion Skin Surface Tension[mN/m]
m.ang=Var(domain=PositiveReals, initialize=pi/4, bounds=(0, pi)) #Contact angle [rad]
m.cos=Var(initialize=0.5, bounds=(-1,1))                         #Skin-Lotion Cosine ( contant angle)

def LA_def(m): #Lotion Air definition
    return m.LA_T==m.LA_To-m.surf.y['STR']
m.LA_def=Constraint(rule=LA_def) 

def LS_def(m): #Lotion Skin definition
    return m.LS_T==m.SA_T+m.LA_T-2*sqrt(m.SA_T*m.LA_T)
m.LS_def=Constraint(rule=LS_def)

def cos_def(m): #Lotion Skin cosine
    return m.cos*m.LA_T==m.SA_T-m.LS_T
m.cos_def=Constraint(rule=cos_def)

def ang_def(m): #Angle definition 
    return m.cos==1-pow(m.ang,2)/2+pow(m.ang,4)/24
m.ang_def=Constraint(rule=ang_def)


#Preference Calculation

def Assorted(m,i):   #Property assorted variable
    if i=='Thic':
        return m.pref.x[i]==m.Thi
    elif i=='Fat':
        return m.pref.x[i]==m.Oil 
    elif i=='Efec':
        return m.pref.x[i]==m.Hmol
    elif i=='Smot':
        return m.pref.x[i]==m.Smo
    elif i=='Cream':
        return m.pref.x[i]==m.Cream
    elif i=='Spread':
        return m.pref.x[i]== 90*m.ang/pi
    else:
        return Constraint.Skip
m.Assorted=Constraint(m.pref.MacroP, rule=Assorted)



#-------------------------------------------------------------------------------------------
#                      S.8  Objective Evaluation
#-------------------------------------------------------------------------------------------

m.Obj=Objective(expr= m.pref.Pr, sense=maximize)

opt=SolverFactory('bonmin')
results=opt.solve(m,tee=True)



print "Maximizing preference case"
print
print "Phase formulation: "

for i in ['cont','disp']:
    m.blo[i].x.pprint()

m.mass.pprint() 
    
print

print "Maximum preference " +str(m.pref.Pr.value/100)+ " %"


#-------------------------------------------------------------------------------------------
#                      S.9  Business model 
#------------------------------------------------------------------------


m.buss=bu_model(m.pref.Pr.value)
print
m.buss.pprint()
print
m.dD.pprint()
print
m.N.pprint()
print
m.Sr.pprint()
print
m.Cdymu.pprint()
print
m.Ct.pprint()
#m.st.pprint()
print
m.ang.pprint()
print
m.Smol.pprint()
print
m.SM.pprint()
print
m.surf.pprint()
    
#Variables
m.Cost=Var(initialize=1e-2*(m.mass['cont'].value*m.blo['cont'].Cost.value+m.mass['disp'].value*m.blo['disp'].Cost.value) )
 

#Constraints
def Cost_def(m): #Constraint def 
    return 100*m.Cost==sum(m.mass[i]*m.blo[i].Cost for i in ['cont', 'disp'])
m.Cost_def=Constraint(rule=Cost_def)

def H2_def(m):  #Preference equality
    return m.buss.H1==m.pref.Pr
m.H2_def=Constraint(rule=H2_def)

m.del_component(m.Obj)

#Objective
def Obj_def(m):
    return m.buss.d1*m.buss.p1-m.buss.d1*m.Cost
m.Obj=Objective(rule=Obj_def, sense=maximize)

opt2=SolverFactory('bonmin')

results=opt2.solve(m, tee=True)


print "Maximizing profit  case"
print
print "Phase formulation: "

for i in ['cont','disp']:
    m.blo[i].x.pprint()

m.mass.pprint() 
    
print

print "Maximum preference " +str(m.pref.Pr.value/100)+ " %"

print 
m.buss.pprint()

print
m.dD.pprint()
print
m.N.pprint()
print
m.Sr.pprint()
print
m.Cdymu.pprint()
print
m.Ct.pprint()
#m.st.pprint()
print
m.ang.pprint()
print
m.Smol.pprint()
print
m.SM.pprint()
print
m.surf.pprint()



