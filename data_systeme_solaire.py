from universal import *


#Radii of solar system bodies
rlune = 1737.1e5  # km
reuropa = 1560.8E5
rganymede = 2631.2E5
rcallisto = 2410.3E5
rio = 1821E5
rtitan = 2575e5
rmercury = 2439.7e5
rearth = 6371.E5
rmoon = 1737.1E5
rmercury = 2439.7E5
rjeq = 71492E5
rjpolar = 66854E5  # ?69911.E5
rjupiter = rjeq
rsaturn = 60268.E5  # 58232km
rpluto = 1153E5
rcharon = 606E5
rfy9 = 750E5
renceladus = 252E5  # km
rrhea = 763.8E5
rdione = 561.4E5  # km
rceres = 463E5
rmars = 3389.5E5
rvenus = 6051E5
rpluto = 1187E5  # New Horizons// Lellouch
reris = 1163. * 1E5  ##  leslie 2400./2
rmakemake = 733. * 1E5
ror10 = 640. * 1E5  # leslie where?
rcharon = 606. * 1E5  ## 606 L.A Young
rquaoar = 534. * 1E5  ## 585 !!!! 1260./2   ## Braga ribas 2013 #!!! 10-2014 555 km  534#
rsedna = 498. * 1E5  ## 500 * !!! 1600./2 * 1E5
r67p = 4.1E5  # 3.2 * 1.3 km
rtriton = 1353. * 1E5
Rsaturn = 58232e5  # cm
rsaturn = Rsaturn

#
##############
# density of solar system bodies
######
rhoeuropa = 3.013  # +/- 5 kg/m^3  Should get from Lodders & Fegley 1998
rhomercury = 5.427
rhojupiter = 1.326
rhosun = 1.408
rhosaturn = 0.687
rhoneptune = 1.638
rhoio = 3.5
rhoganymede = 1.942
rhocallisto = 1.834
rhotitan = 1.88
rhomimas = 1.15
rhoenceladus = 1.6
rhotethys = 0.9
rhodione = 1.478
rhorhea = 1.2
rhoiapetus = 1.088
rholune = 3.344  #
rho67p = 0.4
rhoearth = 5.514
rhomoon = 3.3464
rhoeuropa = 3.013  # +/- 5 kg/m^3  Should get from Lodders & Fegley 1998
e90 = 3.532
rhomercury = 5.427
rhojupiter = 1.326
rhosun = 1.408
rhosaturn = 0.687
rhoneptune = 1.638
rhoio = 3.5
rhoganymede = 1.942
rhocallisto = 1.834
rhoenceladus = 1.61
rhorhea = 1.233
rhodione = 1.469
rhopluto = 2.03
rhocharon = 1.72
rhorhea = 1.236
rhodione = 1.478
rhoceres = 2.161  #
rhomars = 3.9335
rhovenus = 5.243
##!!!!!!!!!!!!!!!!
rhojigglypuff = 3.1  # 1.1 -- 8
rhosuperearth = 24.2  # all based off of Lee & Chiang definitions 2015
rhocrit = 2.01  # guess for it to lose all of its atmosphere
rhosb = 1.8  # np.float(rhosb)
rho1 = 1.6
rho2 = 2.1
rhomoonless = 1.85  # g/cm^3 based on a chosen range of 1.6 - 2.1 Charon to Pluto/Triton like... with a bit of an edge.
rhoplutoEL = 2.04
rhotriton = 2.06
rhopluto = 1.88  # # 1.91 #2.05 # 2.05 we are using  (Brozovic  et al. 2014)/Buie et al 2006.1.30e22 kg. 1150 km, then 2.05
rhoeris = 2.52  # leslie
rhocharon = 1.72  # 10-31 ; Brozovic update values with Marc Buie.
rhoquaoar = 2.18  # 2.18 # 2.18 #http://arxiv.org/abs/1305.0449v2 ; Fornasier et al. 2013 # 3.79!? g/cc  ##10-2014 1.99 Braga Ribas et al. 2013
# moonless KBOs (unknown mass)
rhomakemake = rhosb  # 1.80 # 10-31 2014 ; 1.6--2.1
rhoor10 = rhosb  # rhosb#1.80 #!!! 10-2014 1.71--2.00
rhosedna = rhosb  # 1.80 # 10-31 2014 ; 1.6--2.1
######
# masses of solar system objects
#########
mlune = 7.342e25  # g
mmoon = mlune
msaturn = 5.683e29  # g

meuropa = rhoeuropa * 4. / 3 * pi * np.power(reuropa, 3)
mtriton = 0.003582 * mearth
mganymede = 1.4815E26  # g
mcallisto = 1.0759838E26  # g
mmercury = 3.285E26  # g
mio = 8.93E25  # g
mtitan = 1.3452E26  # g
mcharon = rhocharon * 4. / 3 * pi * np.power(rcharon, 3)
mpluto = rhopluto * 4. / 3 * pi * np.power(rpluto, 3)
# Saturnian
menceladus = 1.8E-5 * mearth  # Jacobson 2006
msaturn = rhosaturn * 4. / 3 * pi * np.power(rsaturn, 3)  # g
mtitan = 0.0225 * mearth  # jacobson 2006 Earths)
mjupiter = 1.8983E30  # grams  http://nssdc.gsfc.nasa.gov/planetary/factsheet/jupiterfact.html
msun = 1.989E33  # g
mrhea = rhorhea * 4. / 3 * pi * np.power(rrhea, 3)
mdione = rhodione * 4. / 3 * pi * np.power(rdione, 3)
mmimas = 6.3e-6 * mearth
mtethys = 0.000103 * mearth
miapetus = 3.023e-4 * mearth
meris = 0.0028 * mearth
mor10 = 3.5e24  # g #### 1.3–6 × 1021 kg
msedna = rhosedna * 4. / 3 * pi * np.power(rsedna, 3)


###
# semi-major axes of solar system objects
###
ajupiter = 5.2
as_europa = 670.9E8  # cm ## nasa fact sheet (9.4Rj) . 11*rjupiter
as_ganymede = 1070400E5
as_callisto = 1882700E5
as_io = 421700E5
as_titan = 1221870E5  # cm
as_lune = 385000E5
as_moon = as_lune
## Saturnien / satellites
as_enceladus = 3.94 * rsaturn
as_dione = 6.26 * rsaturn
as_rhea = 8.74 * rsaturn
as_rhea = 527108E5
# Plutonian satellites / KBOs
as_charon = 17. * rpluto

aceres = 2.7675
##
ejupiter = 0.04839266
eeuropa = 0.009  # 0.01 oscillates to this value.  # should get from Murray and Dermott 1999
eganymede = 0.0013
ecallisto = 0.0074
eio = 0.0041
etitan = 0.0288
##!!!!!!!!!!!!!!!!


#### geophysical tidal parameters: mu (rigidity: dynes/cm^2) , Qs #####################
mu_europa = 4E10  # dynes/cm^2  # Cassidy et al. 2009
mu_io = 6.5E11  # dynes/cm^2
# etav_io =
# etav_europa =
Rmu = mu_io / mu_europa
Qs_europa = 100.  # ^peters & turner 13 --- very difficult to estimate. we strongly stress this.
Qs_io = 100.  # Peale 79

### plasma pressures from Johnson 2004, and Johnson 1990?
Pearth = 2.0  # N/m2 1e-9 at 1AU
Pio = 1800.0  # N/m2 1e-9
Peuropa = 140.0
Pganymede = 20.0
Pcallisto = 1.6
Ptitan = 0.16

####
############
nii = 1e3
sigmaNa = 2.3e-13  # cm^2 from Huang et al. calculation p/
sigmaii = sigmaNa
sigmaSO2 = 1.62366654692663e-14

NaK_39B = 1500.0  # ppm =/- 800 fischer 2016 ; 45 +/- 31 % solar value !!!
Tjupiter = 110.0  # K
gjupiter = 2479.0
Hjupiter = 27e5  # boltz*Tjupiter/(2.3*amu*gjupiter)
njupiter = 10 ** 6 / (boltz * Tjupiter)  #
vorb_io = 17.3e5
njupiter_Na = 1.5 * njupiter * 1e-6
Njupiter_Na = njupiter_Na * Hjupiter
################################################################################
############ Geophysical rock compositions #############

####planetary constants
# Bulk Silicate Earth
Xmgbse = 0.2217
Xsiobse = 0.2122
Xnabse = 5.93e-3
Xkbse = 3.5e-4
Xznbse = 4.95e-4
Xfebse = 0.063
Xcbse = 0.2e-2  # Fischer 2020 'the carbon content of earth and its core'

# van Lieshout et al. # 1573K - 1923 K
# enstatite
mu_mgsio3 = 100.389
alpha_mgsio3 = 0.1
A_mgsio3 = 68908.0  # K +/-8773
B_mgsio3 = 38.1  #

##forsterite Io mantle is 76-85% Sohl 2002
# very similar to CI chondrites ( L and LL chondrites)
mu_mg2sio4 = 140.694
alpha_mg2sio4 = 0.1
A_mg2sio4 = 65308.
B_mg2sio4 = 34.1
# fayalite
mu_fe2sio4 = 203.774
alpha_fe2sio4 = 0.1
A_fe2sio4 = 60377.
B_fe2sio4 = 37.7



