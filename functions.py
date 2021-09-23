from universal import *
"""
@author: Apurva V Oza, JPL/Caltech ; u^b, 2021
email : apurva.oza.space@gmail.com
MODULE FUNCTION: # Functions from fundamental physics textbooks 
Book references: 
"Ellipsoidal Figures of Equilibrium" by Subrahmanyan Chandrasekhar , 1969
"Radiative Processes in Astrophysics" by Rybicki & Lightman, 1979
"Energetic Charged-Particle Interactions with Atmospheres and Surfaces" by Robert E. Johnson , University of Virginia/ New York University 1990.
"Theoretical Astrophysics" by Phil Arras, University of Virginia . 2012

DISHOOM Recipe: You'll need this spice to get your modules to function.

Notes: 
-all inputs are CGS unless otherwise noted. 
-_jaldi = rapid calculation with canonical assumptions (to be checked)
 
Legend:
$$ Name of physical process
! input
% detailed description 
~ references
[] units 


"""



#--------------------------------------------------------------------#
#####
# Tidal physics
######
#--------------------------------------------------------------------#
def Ktide(a_s, rho_s, mp): # !semimajor axis in cm, rho_p or rho_s in g/cm^3, mp or ms in grams. ~(Erkaev et al. 2007)
	phi = a_s * ((4.0 * pi * rho_s)/(9.0 * mp))**(1./3)
	return 1.0 - 3.0/(2.0 * phi) + 1.0/(2.0 * phi**3)






#--------------------------------------------------------------------#
############# orbital and dynamical quantities ######################
#--------------------------------------------------------------------#

def vesc(Mp, Rp):
	return np.sqrt(2.0*G*Mp/Rp)


#--------------------------------------------------------------------#
###
# Exosphere (collisionless atmosphere) physics
####
#--------------------------------------------------------------------#


#--------------------------------------------------------------------#
###
# Radial structure
####
#--------------------------------------------------------------------#

###########
#  Areas of a plasma torus and occulting dust cloud. Assuming it is tau > 1 at continuum wavelengths
############

##radiation pressure ##

#--------------------------------------------------------------------#
####
# Heating and Cooling ; Escape parameters
####
#--------------------------------------------------------------------#

def eta_xuv(Mp, Rp): #~(Wu et al. 2019)
	v_esc =vesc(Mp, Rp)
	return 0.17 * (v_esc/23e5)**(-0.42)

def lambdaj(mi, T, Mp, rp): # % Jeans parameter
	g = G*Mp/rp**2
	return mi*g*rp/(boltz * T)

#--------------------------------------------------------------------#
######
# Outgassing
#######
#--------------------------------------------------------------------#
def Pvap_rocks(A, B, Ts): # %isothermal process; ideal gas P=nkT
	return np.exp(np.divide(-A, Ts) +B)

# $$ Thermal evaporation / sublimation due to a vapor pressure ^
# -->  $$ dM/dt_0 $$
# ~ References:  Oza et al. 2019B Eqn 10, Affolter et al. Eqns 1 & 2

def dMdt_0_sublimation(xi, A, B, Teq, mu_mineral, rs):
		mmineral = amu * mu_mineral
		Mdot0 = Pvap_rocks(A, B, Teq) * np.sqrt(mmineral / (2.0 * pi * boltz * Teq)) * 4.0 * pi * rs ** 2
		return xi * Mdot0  # [g/s]


#--------------------------------------------------------------------#
######
# Atmospheric Escape
#######
#--------------------------------------------------------------------#

# $$ Upper atmospheric escape --> $$ dM/dt_U $$
# ~ References: Johnson et al. 2015 and Oza et al. 2019B Eqn 9, Affolter et al. Eqns 1 & 2



def dMdt_EL_jaldi(xi = 1.0, eleff = 0.1, Fxuv, ms, rs):
	Eg = G*ms/rs
	rabs = rs
	Q = pi * Fxuv * rabs**2
	return xi* eleff * Q/Eg # [g/s]

def dMdt_U(xi, eleff, Lxuv, ap, z_abs,  ms, rs, Mp ): #ap in au, z_abs in planetary/satellite radii
	Eg = G*ms/rs
	Fxuv = Lxuv / (4. * pi * (ap*au2cm)**2)
	r_abs = z_abs * rs
	Q = pi * Fxuv * r_abs**2
	rho_s = ms/(4./3 * pi * rs**3)
	ktide = Ktide(ap*au2cm, rho_s, Mp)
	print('Ktide =', ktide)
	return xi* eleff * Q/Eg * 1./(ktide) # [g/s]

##
# Surface atmospheric escape --> dM/dt_S $$
# ~ References: Johnson et al. 2015 and Oza et al. 2019B Eqn 12, Affolter et al. Eqns 1 & 2
##