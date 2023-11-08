# Load Modules

import MDAnalysis as mda
from MDAnalysis.analysis.base import AnalysisFromFunction
from MDAnalysis.coordinates.memory import MemoryReader
from CodeEntropy.FunctionCollection import EntropyFunctions as EF
from CodeEntropy.ClassCollection import DataContainer as DC
from CodeEntropy.IO import MDAUniverseHelper as MDAHelper
from CodeEntropy.ClassCollection.PoseidonClass import Poseidon

#Load your data into a MDAnalysis Universe

topo_file = "molecules.top"
traj_file = "trajectory.crd"

force_file = "forces.frc"

main = mda.Universe(topo_file, traj_file, atom_style='id type x y z', dt=100, format="MDCRD")
force = mda.Universe(topo_file, force_file, atom_style='id type x y z', dt=100, format="MDCRD")


select_atom = main.select_atoms('all')
select_atom_force = force.select_atoms('all')

coordinates = AnalysisFromFunction(lambda ag: ag.positions.copy(), select_atom).run().results['timeseries']
forces = AnalysisFromFunction(lambda ag: ag.positions.copy(), select_atom_force).run().results['timeseries']

dimensions = AnalysisFromFunction(lambda ag: ag.dimensions.copy(), select_atom).run().results['timeseries']

u2 = mda.Merge(select_atom)

u2.load_new(coordinates, format=MemoryReader, forces=forces, dimensions=dimensions)

#Set Parameters for entropy calculations at ML and UA
selection_string = "all"
axis_list = ["C1", "C2", "C3"]  #DC: the atom name is not C1' but C1 etc.
outfile = None
moutFile = None
nmdFile = None
csv_out = None
tScale = 1.0
fScale = 1.0
temper = 300.0 #K
verbose = 3
thread = 4

# %%
#transVibration and rovibrational entropy at Whole-molecule Level

wm_entropyFF, wm_entropyTT = EF.compute_entropy_whole_molecule_level(
    arg_hostDataContainer = dataContainer,
    arg_outFile = outfile,
    arg_selector = selection_string,
    arg_moutFile = moutFile,
    arg_nmdFile = nmdFile,
    arg_fScale = fScale,
    arg_tScale = tScale,
    arg_temper = temper,
    arg_verbose = verbose
)

#transVibration and rovibrational entropy at United-Atom Level

UA_entropyFF, UA_entropyTT, res_df = EF.compute_entropy_UA_level( #DC: you might not want to use multiprocess as it is just a demo and it is not very stable
    arg_hostDataContainer = dataContainer,
    arg_outFile = outfile,
    arg_axis_list = axis_list, #DC: you forgot to pass the axis list into the function
    arg_selector = selection_string,
    arg_moutFile = moutFile,
    arg_nmdFile = nmdFile,
    arg_fScale = fScale,
    arg_tScale = tScale,
    arg_temper = temper,
    arg_verbose = verbose,
    arg_csv_out= csv_out,
)


total = wm_entropyFF + wm_entropyTT + UA_entropyFF + UA_entropyTT +result_topo_BB
#print(f"Total Entropy = {total} J/mol/K")

with open ('S_Vib.csv', 'w') as f:
    print(f'wm_entropyFF, wm_entropyTT, UA_entropyFF, UA_entropyTT, total', file=f)
    f.write(f' {wm_entropyFF}, {wm_entropyTT}, {UA_entropyFF}, {UA_entropyTT}, {total}')

# Load data into POSEIDON
poseidon_object = Poseidon(container=u2, start=0, end=2000, step=1)

# Calculate Whole Molecule level

result_wm = poseidon_object.run_analysis(level_list = ['moleculeLevel'], verbose=False, forceUnits="Kcal") # this is because the forces value supplied in this trajectory is in Kcal
#print(result_wm)
with open ('S_Vib_solv.txt', 'w') as f:
    #print(f'result_wm', file=f)
    f.write(f'{result_wm}')
