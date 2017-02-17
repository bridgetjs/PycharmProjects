import numpy as np
import scipy as sc


def gaus(x,x0=0,sigma=1):
    exponent= (x-x0)**2 / (2*sigma**2)
    return np.exp(-exponent)

def downslope(x,end,L):

    sigma= L/np.sqrt(2*np.log(10))

    logic_1 = (x >= end )
    logic_2 = ( x <= end + 2 * L )
    G=gaus(x,end,sigma)

    return logic_1*logic_2*G


def upslope(x, end, L):

    sigma= L/np.sqrt(2*np.log(10))

    logic_1 = (x <= end )
    logic_2 = ( x >= end - 2 * L )
    G=gaus(x,end,sigma)

    return logic_1*logic_2*G

def tophat(x,center,width):

    y=np.zeros(np.shape(x))

    y[ abs (x -center) <= width/2] = 1
    return y

def Z_Torch(x,center,PL,TL):

    X01 = center-PL/2
    X02 = center+PL/2

    US = upslope(x,X01,TL)
    DS = downslope(x,X02,TL)
    Plat=tophat(x,center,PL)
    return US + DS + Plat



