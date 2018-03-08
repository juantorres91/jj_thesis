import viscosity as vi
import density as de
# import surface as sc

__all__ = ['Chemical']



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
        self._name = name

        # Physical properties @298.15 - 1 atm 
        self._MW = 0.0   # Molecular weight
        self._mu = 0.0   # Dynamic viscosity [mPa.s]
        self._rho = 0.0  # Density [kg/m3]

        # Product cost
        self._cost =0.0  # [$/kg]
        
        # Property methods
        self._mu_model = 'custom'   # Viscosity model
        self._rho_model = 'custom'  # Density model
        self._st_model = 'custom'   # Surface tension model

        
    @property
    def name(self):
        return self._name

    #
    # Viscosity models 
    #
    
    @property
    def viscosity_model(self):
        return self._mu_model

    @viscosity_model.setter
    def viscosity_model(self, model):
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
    m.viscosity_model = 'arrhenius_type'
    print m.viscosity_model
    

        


        
