#!/bin/bash 
#
#$ -S /bin/bash
#$ -cwd
#
#$ -pe smp 20
#$ -l nvidia_p100=1
#$ -l s_rt=100:00:00

INPUTLIST='min.in heat1.in heat2.in equil.in md.in 1_solv.inpcrd 1_solv.prmtop'

SCR=$TMPDIR
ORIG=`pwd`

module load amber20
export LD_LIBRARY_PATH=/usr/local/cuda-10.2/lib64:$LD_LIBRARY_PATH
export CUDA_VISIBLE_DEVICES=$SGE_GPU
export OMP_NUM_THREADS=$NSLOTS
export MKL_NUM_THREADS=$NSLOTS

cp $INPUTLIST $SCR
cd $SCR

pmemd.cuda -O -i min.in -o min.out -p 1_solv.prmtop -c 1_solv.inpcrd -r min.rst -x min.crd -ref min.rst
pmemd.cuda -O -i heat1.in -o heat1.out -p 1_solv.prmtop -c min.rst -r heat1.rst -x heat1.crd -ref min.rst
pmemd.cuda -O -i heat2.in -o heat2.out -p 1_solv.prmtop -c heat1.rst -r heat2.rst -x heat2.crd -ref heat1.rst
pmemd.cuda -O -i equil.in -o equil.out -p 1_solv.prmtop -c heat2.rst -r equil.rst -x equil.crd -ref heat2.rst
pmemd.cuda -O -i md.in -o md.out -p 1_solv.prmtop -c equil.rst -r md.rst -x md.crd -frc md.frc -ref equil.rst


cp -R * $ORIG
