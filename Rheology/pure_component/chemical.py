__all__ = ['Chemical']

import os
import pandas as pd
import viscosity as vi
import density as ro


"""
 folder = os.path.join(os.dirname(__file__), 'Identifiers')
_compounds = pd.read_csv(os.path.join(folder, 'compounds.csv'),
                         sep='\t', index_col=0)
_compounds_data = _compounds.values

""" 

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
    def __init__(self, ID = '', name = '' ):

        # Component identification
        self._ID = ''
        self._name = name

        # Physical properties @298.15 - 1 atm 
        self._MW = 0.0   # Molecular weight
        self._mu = 0.0   # Dynamic viscosity [mPa.s]
        self._rho = 0.0  # Density [kg/m3]

        # Model parameters
        self._mu_par = dict()   # Dinamic viscosity parameter
        self._rho_par = dict()  # Density parameter
        self._cp_par = dict()   # CP parameters
        
        # Product cost
        self._cost = 0.0  # [$/kg]
        
        # Property methods
        self._mu_model = 'custom'   # Viscosity model
        self._rho_model = 'custom'  # Density model
        self._st_model = 'custom'   # Surface tension model
       
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name
    
    #
    # Viscosity models  
    @property
    def viscosity_model(self):
        return self._mu_model

    @viscosity_model.setter
    def viscosity_model(self, model):
        """
        Set viscosity equation
        Parameters
        ---------
        model : str
          model name
        a : list 
          model parameters
        """
        if model not in vi.__all__:
            raise('Viscosity model ' + model +
                  ' is not currently available')
        else:
            self._mu_model = model

    def get_viscosity_model(self):
        """ 
        Returns viscosity model 
        """
        
        rule = getattr(vi, self.viscosity_model) #  
        return rule


    @property
    def mu_parameters(self):
        """
        Returns viscosity parameters
        """

        return self._mu_par

    @mu_parameters.setter
    def mu_parameters(self, mu_par = dict()):

        self._mu_par = mu_par
    
    #
    # Density models 
    @property
    def density_model(self):
        return self._rho_model
    
    @density_model.setter
    def density_model(self, model):
        """
        Set viscosity equation
        Parameters
        ---------
        model : str
          model name
        """
        if model not in ro.__all__:
            raise('Rho  model ' + model +
                  ' is not currently available')
        else:
            self._rho_model = model

    def get_density_model(self):
        """ 
        Returns viscosity model 
        """
        
        rule = getattr(ro, self.density_model) #  
        return rule

    @property
    def rho_parameters(self):
        """
        Returns viscosity parameters
        """

        return self._rho_par

    @rho_parameters.setter
    def rho_parameters(self, rho_par = dict()):

        self._rho_par = rho_par
    
    
        
