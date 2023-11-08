# Energy-entropy multiscale cell correlation method to predict toluene–water log P in the SAMPL9 challenge
The energy-entropy multiscale cell correlation (EE-MCC) method is used to calculate toluene–water log P 
values of 16 drug molecules in the SAMPL9 physical properties challenge. EE-MCC calculates the free energy, 
energy and entropy from molecular dynamics (MD) simulations of the water and toluene solutions. Specifically, 
MCC evaluates entropy by partitioning the system into cells of correlated atoms at multiple length scales and 
further partitioning the local coordinates into energy wells, yielding vibrational and topographical terms 
from the energy-well sizes and probabilities. The log P values calculated by EE- MCC using three 200 ns MD 
simulations have a mean average error of 0.82 and standard error of the mean of 0.97 versus experiment, which 
is comparable with the best methods entered in SAMPL9. The main contribution to logP is from energy. Less polar 
drugs have more favourable energies of transfer. The entropy of transfer consists of increased solute vibrational 
and conformational terms in toluene due to weaker interactions, fewer solute positions in the larger-molecule 
solvent, reduced water vibrational entropy, negligible change in toluene vibrational entropy, and gains in solvent 
orientational entropy. The solvent entropy contributions here may be slightly underestimated because software limitations 
and statistical fluctuations meant that only the first shell could be included while averaged over the whole solution. 
Nonetheless, such issues will be addressed in future software to offer a general method to calculate entropy directly 
from MD simulation and to provide molecular understanding or guide system design.


https://doi.org/10.1039/D3CP03076H

