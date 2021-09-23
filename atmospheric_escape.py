from universal import *
"""
@author: Apurva V Oza, JPL/Caltech ; u^b, August 2021
email : apurva.oza.space@gmail.com
MODULE FUNCTION: # Atmospheric escape literature
References: 
Johnson et al. 1981, 1982; Haff et al. 1981
Watson et al. 1982
Murray-Clay et al. 2009
Lammer et al. 2009
Oza 2017 Thesis
Oza et al. 2019B
Gebek & Oza 2020


DISHOOM Recipe: ! Caution --> This is the part when the pressure-cooker blasts off into space.
"""

def Rc_ppm(Rstar, ppm): # assuming a spherical shell
    dF_F = ppm * 1e-6
    Rc2 = dF_F*(Rstar **2 )
    Rc = np.sqrt(Rc2)
    Rc_lunar = Rc/rchandra
    return Rc_lunar

def Mc_ppm_rho(Rstar, ppm, rho=rhochandra, dR_bulge=100e5): #assuming the shell has a density rho
    dF_F = ppm * 1e-6
    Rc2 = dF_F*(Rstar **2 )
    Rc = np.sqrt(Rc2)
    dM = 4.0 * pi * Rc**2 * dR_bulge *rho
    dM_lunar= dM/mchandra
    return dM_lunar

