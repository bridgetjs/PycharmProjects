import numpy as np
import scipy as sc
import Torch as T
import matplotlib.pyplot as plt
x=np.linspace(0,1)
y=np.linspace(0,1)
[X,Y] = np.meshgrid(x,y)
x0=0.5
TL=0.1


# for x in x:
#     print(x,abs(x-x0)<TL/2)
plt.figure()
c=0.5  # Center
w=0.05 # HWHM
sigma = w/np.sqrt(2*np.log(2))


G=T.gaus(x,c,sigma)
# plt.plot(x,T.gaus(x,c,sigma))


# Slope

#
# plt.plot(x,T.upslope(x,0.5,.1))
# plt.plot(x,T.downslope(x,0.8,.1))
#
#
# plt.figure(2)


plt.plot(x,0.5*T.Z_Torch(x,0.5,0.25, 0.1))

plt.xlabel('x')
plt.ylabel('y')
plt.ylim(0,.75)
# print(T.tophat(x,0.5,0.25))

# plt.plot(x,T.tophat(x,0.5,.25  ))



plt.figure(2)
z=T.Z_Torch(X,0.5,0.25, 0.1)*T.Z_Torch(Y,0.5,0.25, 0.1)
plt.contourf(x,y,z)
plt.show()