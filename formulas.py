
from uncertainties import ufloat
import numpy as np

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


def absorption_coefficent(T, R,L):
        '''
        absortption coefficent for light passing through a metrial of length L with reflectivity R that has observed trasnmission T
        '''
        return (1/L)*np.log(T/(1-R)**2)


def transmission(I, I0):
     return I/I0
def reflectivity(n):
     return ((n-1)**2)/((n+1)**2)