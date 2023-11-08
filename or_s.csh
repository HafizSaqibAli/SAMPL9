#!/bin/csh
set mols = "Toluene SAMPL9-1 SAMPL9-2 SAMPL9-3 SAMPL9-4 SAMPL9-5 SAMPL9-6 SAMPL9-7 SAMPL9-8 SAMPL9-9 SAMPL9-10 SAMPL9-11 SAMPL9-12 SAMPL9-13 SAMPL9-14 SAMPL9-15 SAMPL9-16"

set mols = "SAMPL9-1 SAMPL9-2 SAMPL9-3 SAMPL9-4 SAMPL9-5 SAMPL9-6 SAMPL9-7 SAMPL9-8 SAMPL9-9 SAMPL9-10 SAMPL9-11 SAMPL9-12 SAMPL9-13 SAMPL9-14 SAMPL9-15 SAMPL9-16"

foreach  mol ($mols)
	 cd $mol 
	  Scripts/solvent_wm_config.pl solvent f1/WMShells.txt Scripts/symmetry.dat
	  Scripts/solute_wm_config.pl solute f1/WMShells.txt Scripts/symmetry.dat
	  Scripts/bin/wm_config_sol.pl toluene f1/WMShells.txt Scripts/symmetry.dat
	  
	 #set solute = `tail -1 solute.sconfig | awk '{print $2}'`
	 

	 cd ..
end
