#!/bin/bash
#$ -cwd -V
#$ -l h_rt=24:00:00
#$ -l h_vmem=12G
#$ -l node_type=24core-768G
#$ -pe smp 8
#$ -m be
module add orca
orca /nobackup/pmljrh/data/HTC-structures/apath_HMF00/apath_HMF00.inp > /nobackup/pmljrh/data/HTC-structures/apath_HMF00/geom_opt01/apath_HMF00.out
orca /nobackup/pmljrh/data/HTC-structures/apath_HMF01/apath_HMF01.inp > /nobackup/pmljrh/data/HTC-structures/apath_HMF01/geom_opt01/apath_HMF01.out
orca /nobackup/pmljrh/data/HTC-structures/apath_HMF02/apath_HMF02.inp > /nobackup/pmljrh/data/HTC-structures/apath_HMF02/geom_opt01/apath_HMF02.out
orca /nobackup/pmljrh/data/HTC-structures/apath_HMF02_O/apath_HMF02_O.inp > /nobackup/pmljrh/data/HTC-structures/apath_HMF02_O/geom_opt01/apath_HMF02_O.out
orca /nobackup/pmljrh/data/HTC-structures/apath_HMF03/apath_HMF03.inp > /nobackup/pmljrh/data/HTC-structures/apath_HMF03/geom_opt01/apath_HMF03.out
