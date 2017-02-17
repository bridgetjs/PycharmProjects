import numpy as np
import matplotlib.pyplot as plt
from matplotlib import ticker
import scipy as sci

D_length= lambda n,KT_e: 7430 * np.sqrt(KT_e/n)
N_D = lambda n,KT_e: 4/3 * np.pi * n * D_length(n,KT_e)


D_range= np.logspace(-8, 1, 5)
N_D_Range = np.logspace(3, 9, 3)

KT_e_Range = np.logspace(1,6,10)

n = lambda D,KT_e : KT_e/(D/7430)**2
n2= lambda N_D, KT_e: 2.95e24 * KT_e**3 / N_D**2
f, (ax1, ax2) = plt.subplots(2,sharex=True,sharey=True)


for D in D_range:
    ax1.loglog(KT_e_Range,n(D,KT_e_Range))
for N_d in N_D_Range:
    ax2.loglog(KT_e_Range,n2(N_d,KT_e_Range))

plt.xlabel('KT_e (GeV)')
plt.ylabel('n ('+ r'$m^{-3}$' + ')')

plt.figure(2)
ax=plt.subplot(111)
n_range = np.logspace(6, 28, 50)
KT_e_Range = np.logspace(-2,5,50)
X,Y=np.meshgrid(n_range,KT_e_Range)

ax.contour(X,Y,D_length(X,Y),locator=ticker.LogLocator())
ax.contour(X,Y,N_D(X,Y),linestyles='dashed', locator=ticker.LogLocator())


ax.set_xscale('log')
ax.set_yscale('log')

plt.show()

