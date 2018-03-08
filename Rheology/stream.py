import pyomo.environ as pe
from pyomo.environ import ConcreteModel
from pure_component import Chemical 

__all__ = ['Stream']


class Stream(ConcreteModel):

    """ Stream type object  

    """

    def __init__(self):

        ConcreteModel.__init__(self)

        #
        # Model sets 
        #
        
        #
        # Model variables
        #
        
        self.mass_flow = pe.Var(domain = pe.PositiveReals)                # Mass flow [kg/s]
        self.molar_flow = pe.Var(domain = pe.PositiveReals)               # Mole flow [mol/s]
        self.T = pe.Var(domain = pe.PositiveReals, initialize = 298)      # Temperature [K]
        self.P = pe.Var(domain = pe.PositiveReals, initialize = 101325)   # Pressure [Pa]

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


if __name__ == '__main__':

    m = Stream()
    m.temperature = 5
    m.T.pprint()
    print m.temperature 
