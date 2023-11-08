#!/bin/csh
set mols = "Toluene SAMPL9-1 SAMPL9-2 SAMPL9-3 SAMPL9-4 SAMPL9-5 SAMPL9-6 SAMPL9-7 SAMPL9-8 SAMPL9-9 SAMPL9-10 SAMPL9-11 SAMPL9-12 SAMPL9-13 SAMPL9-14 SAMPL9-15 SAMPL9-16"

set mols = "Toluene SAMPL9-1 SAMPL9-2 SAMPL9-3 SAMPL9-4 SAMPL9-5 SAMPL9-6 SAMPL9-7 SAMPL9-8 SAMPL9-9 SAMPL9-10 SAMPL9-11 SAMPL9-12 SAMPL9-13 SAMPL9-14 SAMPL9-15 SAMPL9-16"

foreach  mol ($mols)
	 cd $mol
	   python Scripts/Code_Entropy.py 
	   python Scripts/remove_dih_duplicates.py S_Config.txt
	   python Scripts/Svib_M.py
	   python Scripts/Strans_UA.py
	   python Scripts/Srot_UA.py
	   cat Svib_M.txt Srot_UA.txt Strans_UA.txt | awk '$1!="END"' > Entropy_total_JonsCode.txt
	cd ..
end
