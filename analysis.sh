#!/bin/csh

set mols = "SAMPL9-1 SAMPL9-2 SAMPL9-3 SAMPL9-4 SAMPL9-5 SAMPL9-6 SAMPL9-7 SAMPL9-8 SAMPL9-9 SAMPL9-10 SAMPL9-11 SAMPL9-12 SAMPL9-13 SAMPL9-14 SAMPL9-15 SAMPL9-16"

echo "MoleculeName  Sconfig  Solvt_coor"
foreach mol ($mols)
  set Sconfig = `tail -n 1 $mol/solvent.sconfig | awk '{print $1}'`
  set Solvt_coor = `tail -n 1 $mol/solvent.sconfig | awk '{print $2}'`
  echo "$mol  $Sconfig  $Solvt_coor"
end

