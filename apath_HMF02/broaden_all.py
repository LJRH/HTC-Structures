import numpy as np 
from pylab import * 
ion()

import sys 
sys.path.append('/home/christoph/sources/XRStools')
from XRStools import xrs_calctools 
import os


folder_names = ['apath_HMF02_%d'%ii for ii in range(13) ]

data = {}

for ii,folder_name in enumerate(folder_names):
    try:
        os.system('grep \'Absolute energy correction\' %s/xch/erkale_xrs.log > tmp.txt '%folder_name)
        f = open('tmp.txt')
        shift = float(f.readlines()[0].split()[-2])
        print(shift)
        f.close()
    except:
        pass
    dipole = np.loadtxt('%s/xrs/dipole.dat'%folder_name)
    dipole[:,0] += (shift-dipole[0,0])
    dipoleb = xrs_calctools.broaden_linear(dipole[0:250,0:2],params=[0.5, 5, 285.5, 305],npoints=10000)
    data[folder_name] = dipoleb
    np.savetxt('apath_HMF02_broad_%02d.dat'%(ii+1), data[folder_name])

master_x = data[folder_names[0]][:,0]
for_mean = np.zeros(( len(data[folder_name][:,0]), len(folder_names) ))
for ii,key in enumerate(data):
    for_mean[:,ii] = np.interp(master_x, data[key][:,0], data[key][:,1])

for key in data:
    plot( data[key][:,0], data[key][:,1] )

cla()
plot(master_x, np.mean(for_mean, axis=1), '-k')
xlabel('energy [eV]')
ylabel('XAS [arb. units]')
legend(['benzene C K-edge'])

data['mean'] = np.zeros((len(master_x),2))
data['mean'][:,0] = master_x
data['mean'][:,1] = np.mean(for_mean, axis=1)

np.savetxt('apath_HMF02_broad_av.dat', data['mean'])


