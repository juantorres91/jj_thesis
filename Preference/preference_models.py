import pyomo.environ as pe

__all__ = ['shp_pref_model',
           'pws_pref_model',
           'py_pws_pref_model']


def shp_pref_model(in_file):
    """ 
    Supporting hyperplanes model

    Parameters
    ----------

    pref_file : str
       Path to dat file
    
    Returns
    -------
    m : ConcreteModel
       Initilized preference model    

    """

    m = pe.AbstractModel()

    #
    # Sets
    #

    m.MacroP = pe.Set()        # Macroscopic properties
    m.Cuts = pe.RangeSet(1,6)  # Supporting hyperplanes

    #
    # Parameters
    #

    m.w = pe.Param(m.MacroP, default=0)           # Properties ponderation weights
    m.m1 = pe.Param(m.MacroP, m.Cuts, default=0)  # Slope
    m.b1 = pe.Param(m.MacroP, m.Cuts, default=0)  # Intersect
    
    #
    # Variables
    #

    m.y = pe.Var(m.MacroP, initialize= 100, bounds=(-30,100))  # Customer preference
    m.x = pe.Var(m.MacroP, domain=pe.PositiveReals)            # Assorted property values
    m.Pr = pe.Var(domain=pe.PositiveReals)                     # Customer Preference

    #
    # Constraints
    # 
    
    def shp_rule(m,i,j): 
        if m.m1[i,j] != 0 and m.b1[i,j] != 0:
            return m.y[i] <= m.m1[i,j]*m.x[i] + m.b1[i,j]
        else:
            return Constraint.Skip
    m.shp_cons = pe.Constraint(m.MacroP, m.Cuts, rule=shp_rule)  # Supporting hyperplane constraint
    
    def prop_est_rule(m):
        return m.Pr == pe.summation(m.w, m.y)
    m.prop_est_cons = pe.Constraint(rule=prop_est_rule)  # Customer preference estimation

    return m.create_instance(in_file)  # Computes model from data file
    


def pws_pref_model(pref_file):

    """
    Custom piecewise preference model
    
    Parameters
    ----------

    pref_file : str
       Path to dat file
    
    Returns
    -------
    m : ConcreteModel
       Initilized preference model     
    """
    
    m = pe.AbstractModel()  # Algebraic model

    #
    # Sets
    #

    m.MacroP = pe.Set()       # Macroscopic properties
    m.Cuts = pe.RangeSet(0,6) # Piesewise fragments
    
    #
    # Parameters
    #
    m.w = pe.Param(m.MacroP, default=0)           # Correlation weights 
    m.F = pe.Param(m.MacroP, m.Cuts, default=0)   # Fuction at vertex
    m.xo = pe.Param(m.MacroP, m.Cuts, default=0)  # Vertex values

    def Point_init(m,i): # Number of points
        s = 0            # Point counter
        for j in m.Cuts :
            if m.F[i,j] > 0:
                s = s+1
        return s-1
    m.P = pe.Param(m.MacroP, rule=Point_init)

    #
    # Variables
    #
    m.Pr = pe.Var(domain=pe.PositiveReals)  # Averaged preference
    m.x = pe.Var(m.MacroP, within=pe.PositiveReals)   # x value  
    m.f = pe.Var(m.MacroP, bounds=(0,100))  # Preference value 
    m.t = pe.Var(m.MacroP, m.Cuts, bounds=(0,1))  # Weighting function
    m.y = pe.Var(m.MacroP, m.Cuts, domain=pe.Binary)  # Fragment variable

    #
    # Constraints
    # 
    
    def x_cons(m, i):         #x value constraint
        return m.x[i] == sum(m.xo[i,j]*m.t[i,j] for j in m.Cuts  if j<=m.P[i])
    m.x_cons = pe.Constraint(m.MacroP, rule=x_cons) 
    
    def t_cons(m,i,j):        #t value constraint
        if j==0:
            return m.t[i,j] <= m.y[i,j]
        elif j>0 and j < m.P[i]:
            return m.t[i,j] <= m.y[i,j-1]+m.y[i,j]
        elif j == m.P[i]:
            return m.t[i,j] <= m.y[i,j-1]
        else:
            return Constraint.Skip
    m.t_cons = pe.Constraint(m.MacroP, m.Cuts)

    def t_equ(m,i):           #t equivalence constraint 
        return sum(m.t[i,j] for j in m.Cuts if j<=m.P[i])==1
    m.t_equ = pe.Constraint(m.MacroP, rule=t_equ)

    def y_equ(m,i):           #y equivalence constraint
        return sum(m.y[i,j] for j in m.Cuts if j<m.P[i])==1
    m.y_equ=pe.Constraint(m.MacroP, rule=y_equ)

    def f_def(m,i):           #f definition
        return m.f[i]==sum(m.t[i,j]*m.F[i,j] for j in m.Cuts if j<=m.P[i])
    m.f_def=pe.Constraint(m.MacroP, rule=f_def)

    #
    # Objective Definition
    #
    
    def pr_def(m):
        return m.Pr == pe.summation(m.w,m.f)
    m.pr_def = pe.Constraint(rule=pr_def)
       
    return m.create_instance(pref_file)



def py_pws_pref_model(pref_file, kwds='BIGM_BIN'):
    """ 
    Pyomo-type piecewise model

    Parameters
    ----------
    pref_file : str
       Path to preference data
    kwds : str
       PieceWise types [see pyomo_guide]
    
    Returns
    -------
    m : ConcreteModel
       Initialized preferece model
    """

    m = pe.ConcreteModel()  # Preference model

    #
    # Sets
    #

    m.MacroP = pe.Set()       # Macroscopic properties
    m.Cuts = pe.RangeSet(0,6) # Piesewise fragments
    

    #
    # Parameters 
    #
    
    m.w = pe.Param(m.MacroP, default=0)           # Correlation weights 
    m.F = pe.Param(m.MacroP, m.Cuts, default=0)   # Fuction at vertex
    m.xo = pe.Param(m.MacroP, m.Cuts, default=0)  # Vertex values

    #
    # Variables 
    # 
    
    m.y = pe.Var(m.MacroP, initialize= 100, bounds=(-30,100))   # Customer preference
    m.x = pe.Var(m.MacroP, domain=PositiveReals)                # Assorted property values
    m.Pr = pe.Var(domain=PositiveReals)                         #  Customer Preference


    #
    # Constraints
    #

    # TODO set cutting constraint 
    
    m.pwconst = pe.Piecewise(m.y, m.x, )
    
if __name__ == '__main__':
    import sys
    
    m = pws_pref_model(sys.argv[1])
    m.pprint()
