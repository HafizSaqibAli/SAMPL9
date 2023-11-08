#!/bin/csh
set mols = "Toluene SAMPL9-1 SAMPL9-2 SAMPL9-3 SAMPL9-4 SAMPL9-5 SAMPL9-6 SAMPL9-7 SAMPL9-8 SAMPL9-9 SAMPL9-10 SAMPL9-11 SAMPL9-12 SAMPL9-13 SAMPL9-14 SAMPL9-15 SAMPL9-16"

set mols = "SAMPL9-1 SAMPL9-2 SAMPL9-3 SAMPL9-4 SAMPL9-5 SAMPL9-6 SAMPL9-7 SAMPL9-8 SAMPL9-9 SAMPL9-10 SAMPL9-11 SAMPL9-12 SAMPL9-13 SAMPL9-14 SAMPL9-15 SAMPL9-16"

foreach  mol ($mols)

	#mv $mol/md.crd $mol/trajectory.crd
	#mv $mol/md.frc $mol/forces.frc
	#mv $mol/mol_solv.prmtop $mol/molecules.top
	tail -n 1 $mol/solvent.sconfig | awk 'END{print $2}'
end
