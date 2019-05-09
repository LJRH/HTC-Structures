#!/bin/bash

export OMP_NUM_THREADS=12

PATH=$PATH:/users/sahle/ERKALE/erkale/bin
export PATH

export ERKALE_LIBRARY=/users/sahle/ERKALE/build/erkale/basis

# perform initial GGA calculation
if [ ! -d scf ]; then
 mkdir scf
fi

cd scf
erkale_omp ../run.gga
cd ..

# perform half core hole calculation
if [ ! -d xrs ]; then
 mkdir xrs
fi

cd xrs
erkale_xrs_omp ../run.xrs
cd ..

# do full core hole calculation for delta KS correction
if [ ! -d xch ]; then
 mkdir xch
fi

cd xch
erkale_xrs_omp ../run.xch
cd ..

