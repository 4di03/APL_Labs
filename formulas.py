
from uncertainties import ufloat
from uncertainties import unumpy as unp
import numpy as np
import math
def resistivity(R : ufloat ,L :ufloat ,A :ufloat) -> ufloat:
    return R*A/L

def resistance(V : ufloat ,I :ufloat) -> ufloat:
    return V/I

def carrier_concentration(B,VhB):

    return 

def carrier_mobility(n : ufloat , p:ufloat, e = 1.602e-19) -> ufloat:

    return 1/(n*e*p)



def hall_voltage(B : ufloat, I_s : ufloat, n : ufloat , d :ufloat,  e = 1.602e-19) -> ufloat:

    return (B*I_s)/(n*e*d)

def pct_deviation(accepted, measured):

    return f"{(abs(accepted-measured)/accepted) * 100}%"

def deviation(accepted , measured: ufloat):
    err = measured.std_dev  
    return f"{(abs(measured.n-accepted)/err)}"

def get_deviations(accepted, measured: ufloat):
     
     return pct_deviation(accepted, measured), deviation(accepted, measured)

def absorption_coefficent(T, R,L):
        '''
        absortption coefficent for light passing through a metrial of length L with reflectivity R that has observed trasnmission T
        '''
        return (-1/L)*unp.log(T/((1-R)**2))


def transmission(I, I0):
     return I/I0
def reflectivity(n):
     return ((n-1)**2)/((n+1)**2)



def get_photon_energy_nm(wavelength):
    '''
    returns the energy of a photon in electron volts with wavelength in nm
    '''
    return 1239.513/wavelength

def get_photon_energy(wavelength):
    '''
    returns the energy of a photon with wavelength m
    '''
    return (6.626e-34 * 3e8)/(wavelength)


def speed_of_light(n,c= 299792458):
    '''
    returns the speed of light in a material with refractive index n
    '''
    return c/n


def t(d, v):
    '''
     Get time for an object to travel distance d with velocity v
    '''
    return d/v

def convert_nano(unit):
    '''
    convert unit to nano units
    '''
    return  unit * 1e9, "nano"

def convert_micro(unit):
    '''
    convert unit to micro units
    '''
    return unit * 1e6, "micro"

def convert_milli(unit):
    '''
    convert unit to milli units
    '''
    return unit * 1e3, "milli"

def convert_pico(unit):
    '''
    convert unit to pico units
    '''
    return unit * 1e12, "pico"


def inductance(w, C): 
    '''
    Get inductance for a given angular frequency and capacitance
    '''
    return 1/((w**2)*C)

def get_inductance(t, C):
    '''
    Get inductance for a given period
    '''
    f = 1/t
    w = 2*math.pi*f
    L = inductance(w, C)
    return f"Period :{t:.9f}\nFrequency: {f:.9f}\nAngular Frequency: {w:.9f}, \nInductance: {L:.9f}"