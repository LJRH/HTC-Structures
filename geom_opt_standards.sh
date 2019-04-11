#!/bin/bash
#$ -cwd -V
#$ -l h_rt=24:00:00
#$ -l h_vmem=12G
#$ -l node_type=24core-768G
#$ -pe smp 8
#$ -m be
module add orca
orca /nobackup/pmljrh/data/HTC-structures/5HMF/5HMF.inp > /nobackup/pmljrh/data/HTC-structures/5HMF/geom_opt01/5HMF.out
orca /nobackup/pmljrh/data/HTC-structures/DHA/DHA.inp > /nobackup/pmljrh/data/HTC-structures/DHA/geom_opt01/DHA.out
orca /nobackup/pmljrh/data/HTC-structures/formic_acid/formic_acid.inp > /nobackup/pmljrh/data/HTC-structures/formic_acid/geom_opt01/formic_acid.out
orca /nobackup/pmljrh/data/HTC-structures/levullinic_acid/levullinic_acid.inp > /nobackup/pmljrh/data/HTC-structures/levullinic_acid/geom_opt01/levullinic_acid.out
