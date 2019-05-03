import numpy as np
from pylab import *
ion()

import sys
sys.path.append('/home/christoph/sources/XRStools/')
from XRStools import xrs_calctools, xrs_utilities, math_functions

import copy
import os

ex_atom = 'C'

path = '/home/christoph/atoms/HTC-Structures/apath_HMF00/'
fname = 'apath_HMF00.xyz'
# read xyz file
box = xrs_calctools.boxParser( path+fname )
all_ex_atoms = box.get_atoms_by_name( ex_atom )

base_name = fname[:-4]

# make xyz and xyz-xrs files
for ii,atom in enumerate(all_ex_atoms):
    # put excited atom first
    xyz_atoms = [atom]
    for at in box.xyzAtoms:
        if at is not atom:
            xyz_atoms.append(at)
    # make one folder per ex-atom
    os.system('mkdir '+base_name+'_%d'%ii)
    # write files
    fname1 = base_name+'_%d.xyz'%ii
    save_box = xrs_calctools.xyzBox(xyz_atoms)
    save_box.writeBox(base_name+'_%d/'%ii+fname1)
    # change carbon name to C-Xc
    fname2 = base_name+'_%d-xrs.xyz'%ii
    save_box.xyzAtoms[0].name = 'C-Xc'
    save_box.writeBox(base_name+'_%d/'%ii+fname2)
    # change carbon name back
    save_box.xyzAtoms[0].name = 'C'
    #
    # write all run files
    #
    # GGA run
    ggaf = open( base_name+'_%d'%ii+'/run.gga','w+')
    ggaf.write('# Coordinates are given in the file \n')
    ggaf.write('System ../'+fname1 + ' \n')
    ggaf.write('# Use GGA-PBE exchange and GGA-PBE correlation \n')
    ggaf.write('Method gga_x_rpbe-gga_c_pbe \n')
    ggaf.write('# Use the cc-pVDZ basis set \n')
    ggaf.write('Basis ../basis.gbs \n')
    ggaf.write('# Save the results in the checkpoint file \n')
    ggaf.write('SaveChk gga.chk \n')
    ggaf.write('# Use the core guess to initialize the calculation \n')
    ggaf.write('Guess Core \n')
    ggaf.write('# use direct \n')
    ggaf.write('Direct true \n')
    ggaf.write('# do not use Cholesky decomposition \n')
    ggaf.write('Cholesky false \n')
    ggaf.write('IntegralThresh 1.000e-8 \n')
    ggaf.close()
    # xrs run
    xrsf = open( base_name+'_%d'%ii+'/run.xrs', 'w+')
    xrsf.write('System ../%s \n'%fname2)
    xrsf.write('Method gga_x_rpbe-gga_c_pbe \n')
    xrsf.write('Basis ../basis.gbs \n')
    xrsf.write('# ... with the ground-state density given by \n')
    xrsf.write('LoadChk ../scf/gga.chk \n')
    xrsf.write('XRSAugment 1 \n')
    xrsf.write('XRSQval 0.01, 0.2, 0.4, 0.6, 0.8, 1.0 \n')
    xrsf.write('# use direct \n')
    xrsf.write('Direct true \n')
    xrsf.write('# do not use Cholesky decomposition \n')
    xrsf.write('Cholesky false \n')
    xrsf.write('IntegralThresh 1.000e-8 \n')
    xrsf.close()
    # xch run
    xchf = open( base_name+'_%d'%ii+'/run.xch', 'w+')
    xchf.write('System ../%s \n'%fname2)
    xchf.write('Method gga_x_rpbe-gga_c_pbe \n')
    xchf.write('Basis ../basis.gbs \n')
    xchf.write('# ... with the ground-state density given by \n')
    xchf.write('LoadChk ../scf/gga.chk \n')
    xchf.write('XRSAugment 1 \n')
    xchf.write('XRSMethod XCH \n')
    xchf.write('# use direct \n')
    xchf.write('Direct true \n')
    xchf.write('# do not use Cholesky decomposition \n')
    xchf.write('Cholesky false \n')
    xchf.write('IntegralThresh 1.000e-8 \n')
    xchf.close()

