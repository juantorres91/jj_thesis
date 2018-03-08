import pyomo.environ as pe
import balances as bal
from pure_component import Chemical 
from pyomo.opt import SolverFactory

__all__ = ['Stream']


class Stream(pe.ConcreteModel):

    """ Stream type object  

    Attributes
    ----------
    """

    def __init__(self):

        pe.ConcreteModel.__init__(self)

        #
        # Metadata [Component Objects]
        
        self.__chem = dict() # Name to chemical mapping
        
        #
        # Model sets 
        self.comp = pe.Set()  # Stream components 

        #
        # Model parameters
        self.MW = pe.Param(self.comp, default=0)       # Molecular weight
        self.tc = pe.Param(self.comp, default=298)     # Critric temperature
        self.pc = pe.Param(self.comp, default=101325)  # Critic pressure
        
        #
        # Model variables
        
        # Basic properties
        self.mass_flow = pe.Var(domain = pe.PositiveReals)              # Mass flow [kg/s]
        self.molar_flow = pe.Var(domain = pe.PositiveReals)             # Mole flow [mol/s]
        self.vol_flow = pe.Var(domain = pe.PositiveReals)               # Volume flow [m3/s]
        self.T = pe.Var(domain = pe.PositiveReals, initialize=298)      # Temperature [K]
        self.P = pe.Var(domain = pe.PositiveReals, initialize=101325)   # Pressure [Pa]

        # TODO : Implement new types of properties 
        # Component properties
        self.xw = pe.Var(self.comp, bounds=(0,1))  # Mass fraction
        self.xm = pe.Var(self.comp, bounds=(0,1))  # Molar fraction
        self.vf = pe.Var(self.comp, bounds=(0,1))  # Volume fraction 
        self.rho = pe.Var(self.comp, domain = pe.PositiveReals)   # Component density [kg/m3]
        self.dymu = pe.Var(self.comp, domain = pe.PositiveReals)  # Component absolut viscosity [Pa.s] 
        self.kmu = pe.Var(self.comp, domain = pe.PositiveReals)   # Component kynetic viscosiy [cSt]
        
        # Mixture properties
        self.Rho = pe.Var(domain = pe.PositiveReals)  # Mixture density [kg/m3]
        self.Dmu = pe.Var(domain = pe.PositiveReals)  # Mixture dynamic viscosity

        #
        # Balance constraints flags
        self.__massbal_flag = False   # Boolean : Activated mass balance
        self.__molarbal_flag = False  # Boolean : Activated molar balance
        self.__volbal_flag = False    # Boolean : Activated 
        
    #
    # Component methods
    #

    def add_chemical(self, ch):
        """
        Adds new chemical element
        """
        self.__chem[ch.name] = ch
        self.comp.add(ch.name) 

    def del_chemical(self, name):
        """
        Deletes chemical from list
        """
        self.__chem.pop(name, None) 
        self.comp.remove(name)

    #
    # Balance constraints
    #

    def enable_mass_balance(self):
        """
        Construct mass balance
        """
        self.mass_balance = pe.Constraint(rule = bal.mass_balance_rule)

            
    def disable_mass_balance(self):
        """
        Disables mass balance
        """
        try:
            x = self.find_component('mass_balance')
            x.deactivate()
        except:
            pass
                   
    #
    # Temperature methods
    #
        
    @property
    def temperature(self):
        return self.T.value

    @temperature.setter
    def temperature(self, t):
        if t < 0.0:
            raise Exception('Temperature must be positive')
        else :
            self.T.fix(t)

    def initialize_temperature(self, t):
        """
        Initializes stream temperature
        """
        if t < 0.0:
            raise Exception('Temperature must be positive')
        else :
            self.T.value = t

    def set_temperature_bounds(self, tmin = 0, tmax = float('inf')):
        """
        Sets temperature limits
        """
        
        if tmin < 0 or tmax < 0:
            raise Exception('Temperature must be positive')
        elif tmin > tmax:
            raise Exception('tmin must be lower or equal tmax')
        else:
            self.T.setlb(tmin)
            self.T.setub(tmax)

    #
    # Pressure methods
    #
        
    @property
    def pressure(self):
        return self.P.value

    @pressure.setter
    def pressure(self, p):
        if p < 0.0:
            raise Exception('Pressure must be positive')
        else :
            self.P.fix(p)

    def initialize_pressure(self, p):
        """
        Initializes stream pressure
        """
        if p < 0.0:
            raise Exception('Presure must be positive')
        else :
            self.T.value = t

    def set_pressure_bounds(self, pmin = 0, pmax = float('inf')):
        """
        Sets pressure limits
        """
        
        if pmin < 0 or pmax < 0:
            raise Exception('Pressure must be positive')
        elif pmin > pmax:
            raise Exception('pmin must be lower or equal pmax')
        else:
            self.P.setlb(pmin)
            self.P.setub(pmax)

            
if __name__ == '__main__':

    x = Chemical(name = 'a')
    y = Chemical(name = 'b')
    m = Stream()

    m.add_chemical(x)
    m.add_chemical(y)
    m.enable_mass_balance()

    m.del_chemical('a')
    m.enable_mass_balance()
    
    m.pprint()
