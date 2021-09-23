from universal import *
from data_systeme_solaire import *
"""
@author: Apurva V Oza, JPL/Caltech ; u^b, August 2021
email : apurva.oza.space@gmail.com
MODULE FUNCTION: # Atmospheric evolution literature
References: 
Hodges & Johnson 1968
Oza et al. 2018


DISHOOM Recipe: This is the churning of the atmosphere over time, just sit back and rotate with the tides.
"""
## See equation Oza et al. 2018; 2022

##m dN/dt = (F - N  dm/dt )

#integrator