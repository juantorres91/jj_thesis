import viscosity as vi
__all__ = ['Chemical']


# Viscosity models
vi_types = ['arrhenius_type', 'modified_wlf_type',
            'power_law_type']  



class Chemical(object):
    
    """ 
    Chemical compound

    Parameters
    ----------
    
    ID : str
       Chemical identifier (i.e. CAS Number)
    name : str
       Compound name
    """ 
    
    def __init__(self,ID = '', name = '' ):

        # Component identification
        self._ID = ''
        self._name = ''

        # Physical properties @298.15 - 1 atm 
        self._MW = 0.0   # Molecular weight
        self._mu = 0.0   # Dynamic viscosity [mPa.s]
        self._rho = 0.0  # Density [kg/m3]

        # Product cost
        self._cost =0.0  # [$/kg]
        
        # Property methods
        self._mu_model = 'power_law_type' #  


        
    @Property
    def name(self):
        return self._name

    

        

    def set_viscosity_model(self, model):
        """
        Set viscosity equation
        
        Parameter
        ---------
        model : str
          model name
        """
        if model not in vi_types:
            raise('Viscosity model ' + model +
                  ' is not currently available')
        else:
            self._mu_model = model

    
            
if __name__ == '__main__':
    m = Chemical(name='a')
        
    

        


        
