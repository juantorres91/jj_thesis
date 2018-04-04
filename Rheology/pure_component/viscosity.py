__all__ = ['custom',
           'arrhenius_type',
           'modified_wlf_type',
           'power_law_type']

import os
import pyomo.environ as pe
import pandas as pd



def custom(m, i):
    """
    fixed viscosity
    Parameters
    ----------
    i : str
       Component index
    mu_coef[0] : Pa.s
       Fixed viscosity
    """ 

    return m.dymu[i] == m.mu_coef[i,0]
    

def arrhenius_type(m, i):

    """
    Arrehenius type visocosity model
    Parameters
    ----------
    i : str 
      Component index 
    mu_coef[0]: mPa . s
      Correlation parameter
    mu_coef[1] : MJ/ kg mol k
      Activation energy
    
    Return
    ------
    Viscosity constraint rule
    dymu : Pa . s
      Component dynamic viscosity
    """
    R = 8.314e-3 # Ideal gas constant [MJ/ kg mol k] 

    return m.dymu[i] == m.mu_coef[i,0] * pe.exp(m.mu_coef[i,1] / (R*m.T))


def modified_wlf_type(m, i):
    """
    Modified WLF viscosity model
    Parameters
    ---------- 
    i : str 
      Component index 
    mu_coef[0] : 1/K
      Correlation parameter
    mu_coef[1] : K
      Correlation parameter   
    Return
    ------
    Viscosity constraint rule
    dymu : Pa . s
      Component dynamic viscosity
    """
    
    return pe.ln(m.dymu[i]) == (m.mu_coef[i,0]*m.T)/(m.mu_coef[i,1] + m.T)


def power_law_type(m, i, a1 = 10.33e-3, a2 = -1.535, a3 = 273.15):

    """
    Power law viscosity model
    
    Parameters
    ----------

    i : str 
      Component index 
    a1 : mPa .s 
      Correlation parameter
    a2 : int
      Correlation parameter
    a3 : k
      Reference temperature
    Return
    ------
    Viscosity constraint rule

    dymu : Pa . s
      Component dynamic viscosity
    """

    return m.dymu[i] == a1*(m.T - a3)**a2



class ViscosityModel(object):

    def __init__(self, name =''):

        self._name = name()


      

        

                                  

