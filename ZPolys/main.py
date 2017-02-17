import numpy as np
import matplotlib.pyplot as plt
import Zernike


rad = np.linspace(0, 1, 100)
azm = np.linspace(0, 2 * np.pi, 100)
r, th = np.meshgrid(rad, azm)

m_range=np.linspace(-5,5,11)
n_range=np.linspace(0,5,6)

fig = plt.figure()
for n in n_range:
    for indx,m in enumerate(m_range):
        if not ((n - m) % 2 == 0) or abs(m) > n:
            continue
        # print('2n=', 2*n, ' indx=',indx)
        ax = plt.subplot2grid((12, 12), [2 * int(n), indx], 2, 2, projection='polar')
        f=ax.pcolormesh(th, r, Zernike.zern(m, n, r, th),cmap='viridis')
        plt.axis('off')
        y = 1.65
        if m < 0: y = 1.85

        plt.text(1.15*np.pi, y, r'$Z^{%d}_%d$' % (m, n))
        ax.set_rmax(1)

        
cbaxes = fig.add_axes([0.9, 0.1, 0.03, 0.8])
cb = plt.colorbar(ax=ax, cax = cbaxes,mappable=f)
# plt.savefig('21.png',dpi=1000)
plt.savefig('21-500dpi.png',dpi=500)
#
plt.figure(2)
ax=plt.subplot(projection='polar')
ax.pcolormesh(th,r,Zernike.zern(1, 5, r, th),cmap='viridis')
plt.axis('off')
plt.text(1.25*np.pi,1.2,r'$Z^{2}_4$',size=16)

# plt.show()