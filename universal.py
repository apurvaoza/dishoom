import numpy as np

# -*- coding: utf-8 -*-
# universal constants.py
"""
@author: Apurva V Oza, JPL/Caltech, 2021
email : apurva.oza.space@gmail.com
MODULE FUNCTION: # Universal constants along with atomic & molecular data along with a little bit of dissociation/recombination rate spices are stored here.
Recipe: UNIVERSAL to all recipes :) . Add if you have discovered something new and fundamental to the universe.  
"""
import numpy as np
from math import *

# from constants import *
# ! Physical constants. ###########################################################################################################################################################################################################
h = 6.62606896e-27  # erg * s
boltz = 1.3806488E-16  # ergs/K
sb = 5.67E-5  # stefan boltzmann constant cgs
kb = 8.617385E-5  # eV/K
Cstegra = 6.672598E-08  # cm3/g/s^2 ## 6.67384E-8
G = 6.67384E-08
amu = 1.66053892E-24  # g ##atomic mass = molecules2moles = 1./ (6.022E23)  # 1 gram/mole #1.66053892E-24
# conversions
au2cm = 1.49597870700E13  # cm in an AU
cm2mA = 1e11  # cm to milliangstroms
fullorbit = 2. * pi  # full orbit
y2s = 3.15581498E7  # seconds in a year
kgs = 1. / 1000
erg2ev = 1.60217646E-12  # convert ergs to eV
cmks = 3E8  # m/s
c = 2.99792458E10  # cm/s
m_e = 9.10938214e-28  # grams
qe = 4.8032047e-10  # statcoulombs
sigmaH = 1e-15  # cm2 Hydrogen cross section ; Shu
r_e = qe ** 2 / (m_e * c ** 2)  # 8.852822093424571e-13/pi cm see Draine eqn. 9.14

sigma_NaD_photo = 6.471557992502263e-20  # cm2 by using gamma_na_hd189 from Huang et al. 2017

########## Photodissoc rates Huebner et al. 1992 AT 1 AU ##################
# k_hv_Na = 1.62e-5 # s-1 p.25
k_hv_Na = 5.92e-6  # s-1 Huebner & Mukherjee 2015!
k_hv_K = 2.22e-5  # s-1 p.35 of waht
ke_jupiter = 6.94e-5  # s-1 # yields 4 hours at JUPITER, Johnson et al. 2009 review and & Burger & Johnson -- schmidt correspondance
k_hv_H2O = 1.03e-5 + 5.97e-7 + 7.54e-7 + 3.31e-7 + 1.31e-8 + 5.85e-9 + 5.54e-8

k_hv_SO2_1 = 1.59e-4  # SO+O p.149
k_hv_SO2_2 = 5.09e-4  # S + O2
k_hv_SO2_3 = 1.06e-6  # SO2+ + e-
k_hv_SO2_tot = k_hv_SO2_1 + k_hv_SO2_2 + k_hv_SO2_3
# OH p.47
# H2O p.102
# SO p.95
# CO2 P.12-
########### Sodium ##########
fD2 = 0.641  # oscillator strength JH 06 OR DRAINE TABLE 9.3
fD1 = 0.320  #
lamD10 = 5897.558  # vacuum
lamD20 = 5891.582
lamD1 = 5895.92424  # NIST DATA BASE AND DRAINE
la2mD2 = 5889.95095  # NIST

########### Potassium ##########
fKD2 = 0.682
fKD1 = 0.34

"""
Parameters for the sodium D lines Prometheus 
"""
f_NaD2 = 0.6405  # 0.6401 Oscillator strength Na D2 (Steck Los Alamos 2000) (Draine 2011)
fNaD2 = f_NaD2
lambda_NaD2 = 5891.582e-8  # Wavelength of Na D2 in vacuum (Draine 2011)
gamma_NaD2 = 3.833e8  # Natural linewidth Na D2 x 2 pi (Steck 2000)

f_NaD1 = 0.3199  # Oscillator strength Na D1 (Draine 2011)
fNaD1 = f_NaD1
lambda_NaD1 = 5897.567e-8  # Wavelength of Na D1 in vacuum (Draine 2011)
gamma_NaD1 = 3.855e8  # Natural linewidth Na D1 x 2 pi (Steck 2000)

Xna = 1.7e-6  # solar abundance asplund 2009
"""
Parameters for the potassium D lines Prometheus.
"""
f_KD2 = 0.682  # Oscillator strength K D2 (Draine 2011)
lambda_KD2 = 7667.01e-8  # Wavelength of K D2 in vacuum (Draine 2011)
gamma_KD2 = 2.3825e8  # Natural linewidth K D2 x 2 pi (Tiecke 2011)

f_KD1 = 0.34  # Oscillator strength K D1 (Draine 2011)
lambda_KD1 = 7701.08e-8  # Wavelength of K D1 in vacuum (Draine 2011)
gamma_KD1 = 2.3513e8  # Natural linewidth K D1 x 2 pi (Tiecke 2011)

lamNaDs = (lambda_NaD1 + lambda_NaD2) / 2
lamKDs = (lambda_KD1 + lambda_KD2) / 2
Prad_Na_mercury = 1.04805e-13  # dynes/cm^2

gval_chamberlain_earth = 0.888  # 1961 for Na D2 D1 average resonant scattering photons/s/cm2/angstrom

Tsun = 5777.0
# Resonant Scattering Cross-section (Steck_2003):
#    D1 (5895 A) --->
sigmaD1_resonance = 5.558e-08  # cm^2
#    D2 (5891 A) --->
sigmaD2_resonance = 1.105e-09  # cm^2
# - g-values at R=0.35 AU (Killen+_2009):
#    D1 (5895 A) --->
g1 = 23.2  # ph/atom/s
#    D2 (5891 A) --->
g2 = 38.4  # ph/atom/s

# The photon flux at 0.35 AU for Na is:
F_v_NaD1 = g1 / sigmaD1_resonance  # 4.14e+08 ph/ cm2/s
F_v_NaD2 = g2 / sigmaD2_resonance  # 3.47e+10 ph/ cm2/s

'''
Verner & Ferland 1996.  The expression looks like 
  double T0=307.7;
  return 5.641E-12/sqrt(T/T0)/pow(1+sqrt(T/T0),0.825);
If plug in T = 8000 K and assume ne = 10^9 cm^-3, then the radiative recombination rate is about 2.5 * 10^-4 s^-1.

The rate for Na is 
5.641E-12/sqrt(T/T0)/pow(1+sqrt(T/T0),0.825) cm^3 s^-1, 
T0=307.7.  
So it on the order of 10^-12 cm^3 s^-1.

The rate for K is 
  double T4=T/1E4;
  double a[4]={2.762, 0.8023, 62.35, 51.28};
  return a[0]*1E-13*pow(T4,-a[1])+a[2]*1E-4*pow(T,-1.5)*exp(-a[3]/T4);
On the order of 10^-13 cm^3 s^-1.


 K0/F9 star for the propose of WASP-12b.  The rate is about 1.3*10^-5 s^-1 at 1AU.

 My result using MUSCLES spectrum suggests a photoionization rate at 1AU around a K2 star is about 9.5e-7 s^-1.
'''
khv_K = 9.5e-7  # s^-1  K2 -- !N.B: spectrum,metallicity & log g, also contribute ; Huang et al. 2017 using MUSCLES spectrum.
khv_G = 5.92e-6  # s^-1  G2
khv_F = 1.3e-5  # s^-1 at 1AU for K0/F9.

'''
I used the stellar parameters of KELT-9.  T=10170, R_star=2.362 R_Sun.
At 1AU, the photoionization rate for Na is 0.0298 s^-1, for K is 0.0796 s^-1
'''
k_hv_Na_Astar = 0.0298  # s-1
k_hv_Na_Gstar = khv_G
k_hv_Na_Kstar = khv_K
k_hv_Na_Fstar = khv_F
k_Na_recomb = 2.5e-4  # s-1
k_hv_K_Gstar = 2.22e-5  # s-1 p.35   #Chenliang gets from the cross section provided by Verner & Yakovlev 1995.  In table 2 of my paper, I listed the photoionization rates of K I at 0.031 AU.  Convert the number to 1AU, it is 2.00E-6 s^-1.
k_hv_K_Fstar = k_hv_K_Gstar / (khv_G / khv_F)
k_hv_K_Kstar = k_hv_K_Gstar / (khv_G / khv_K)
k_hv_K_Astar = 0.0796  # s-1

####
# collisional cross sections from Jaggi, Gamborino, Bower 2021 , depend on the element.
sigmacross_H = 8.82e-17  # cm^2
sigmacross_Na = 1.13e-15  # cm^2
sigmacross_K = 1.86e-15  # cm^2
sigmacross_O = 1.13e-16  # cm^2
sigmacross_C = 1.41e-16  # cm^2S
#
############ Volatile masses $mi$ ############################################################
mCO = 28.0101 * amu  ##
mCO2 = 44.01 * amu
mN2 = 28.0134 * amu  ##  28.0134 amu  = 4.6517340981528e-23 grams
mCH4 = 16.0425 * amu  #
mH2O = 18.0153 * amu  # g/mol
mD = 2.01410178 * amu  # 2H == deuterium
mO = 15.9994 * amu
mO2 = 31.9988 * amu
mOH = 17.0073 * amu
mH = 1.00826 * amu
mH2 = 2.01588 * amu  # H2
mHe = 4.002602 * amu
mNa = 22.9897 * amu
mK = 39.0983 * amu
mS = 32.065 * amu
mMg = 24.305 * amu
mC = 12.0107 * amu
mFe = 55.845 * amu
mNaCl = 58.443 * amu  # g/mol
mAr = 39.948 * amu
mSO2 = 64.066 * amu  # g
mNH3 = 17.031 * amu  # g
mbeer8abv = 20.2596 * amu  # g belgian beer

################################################################################
# D
# I
# S
# H
# O
# O
# M
################################################################################
mchandra = 7.342E25
rchandra = 173710000.0
rhochandra = 3.344
####
Msun = 1.988435E33  # grams
msun = Msun
Rsun = 6.957e10  # centimeters
rsun = Rsun
mearth = 5.972E27  # g
rhoearth = 5.515
mjupiter = 1.8983E30  # grams  http://nssdc.gsfc.nasa.gov/planetary/factsheet/jupiterfact.html
rjeq = 71492E5
rjpolar = 66854E5  # ?69911.E5
rjupiter = 69911.E5  # corrected from 4.25.2020 rjeq
rearth = 6371.E5  # cm
sc = 1361.  # watts /m^2 SOLAR CONSTANT (flux density)
Fsun = 1360800.  # erg s-1cm-2
Lsun = 3.848e33  # ergs/s

