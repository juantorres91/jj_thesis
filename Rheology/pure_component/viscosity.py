import pyomo.environ as pe

__all__ = ['arrhenius_type',
           'modified_wlf_type',
           'power_law_type']


def arrhenius_type(m, i, a1 = 3, a2 = 20,):

    """
    Arrehenius type visocosity model
    Parameters
    ----------
    i : str 
      Component index 
    a1 : mPa . s
      Correlation parameter
    a2 : MJ/ kg mol k
      Activation energy
    
    Return
    ------
    Viscosity constraint rule
    dymu : Pa . s
      Component dynamic viscosity
    """
    R = 8.314e-3 # Ideal gas constant [MJ/ kg mol k] 

    return 1e-3*m.dymu[i] == a1*pe.exp(a2/(R*m.T))


def modified_wlf_type(m, i, a1 = 0.658, a2 = -255,):
    """
    Modified WLF viscosity model
    Parameters
    ---------- 
    i : str 
      Component index 
    a1 : 1/k
      Correlation parameter
    a2 : k
      Correlation parameter   
    Return
    ------
    Viscosity constraint rule
    dymu : Pa . s
      Component dynamic viscosity
    """

    return pe.ln(m.dymu[i]*1e-3) == (a1*m.T)/(a2 + m.T)


def powerlaw_type(m, i, a1 = 10.33e-3, a2 = -1.535, a3 = 273.15):

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




                                  

