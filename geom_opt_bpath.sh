#!/bin/bash
#$ -cwd -V
#$ -l h_rt=24:00:00
#$ -l h_vmem=12G
#$ -l node_type=24core-768G
#$ -pe smp 8
#$ -m be
module add orca
orca /nobackup/pmljrh/data/HTC-structures/bpath_HMF01/bpath_HMF01.inp > /nobackup/pmljrh/data/HTC-structures/bpath_HMF01/geom_opt01/bpath_HMF01.out
orca /nobackup/pmljrh/data/HTC-structures/bpath_HMF02/bpath_HMF02.inp > /nobackup/pmljrh/data/HTC-structures/bpath_HMF02/geom_opt01/bpath_HMF02.out
orca /nobackup/pmljrh/data/HTC-structures/bpath_HMF03/bpath_HMF03.inp > /nobackup/pmljrh/data/HTC-structures/bpath_HMF03/geom_opt01/bpath_HMF03.out
