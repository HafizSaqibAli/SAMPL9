#!/usr/bin/env python3

import rdkit
from rdkit import Chem
from rdkit.Chem import AllChem
import autode
from dimorphite_dl import DimorphiteDL
import os
import argparse

def get_args():
    # Get arguments for ligand files preparation
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", action='store', help='smiles.txt file(s) of ligand for preparation', nargs='+')
    
    return parser.parse_args()

def get_protonation_state(smiles):
    """
    returns the smiles string of the most probable protonation state at pH specified
    :param smiles: SMILES of molecule to protonate
    :return: SMILES of protonation state
    """
    dimorphite_dl = DimorphiteDL(
        min_ph=7.4,
        max_ph=7.4,
        max_variants=128,
        label_states=False,
        pka_precision=1.0
    )

    protonation_states = dimorphite_dl.protonate(smiles)

    return protonation_states[0]

def optimise_smiles_geometry_and_print_xyz(smiles, name):
    """
    Uses autode and XTB to optimise the geometry of the molecule specified by the smiles string and prints xyz file
    :param smiles: smiles string of molecule to optimise
    :param name: name of molecule
    :return: None
    """
    mol = autode.Molecule(smiles=smiles, name=name)
    mol.optimise(method=autode.methods.XTB())

    return None

if __name__ == '__main__':
    
    args = get_args()
    #print(args.filenames)
    
    #filename = open(args.filenames, 'r')
    #lines = filename.readlines()
    #print(lines)
    
    for file in args.filenames:
        lines = open (file, 'r')
        lines = lines.readlines()
        for line in lines:
            words = line.split()
            name = words[1]
            smiles = words[2]
            mol = Chem.MolFromSmiles(smiles)
            mol = Chem.AddHs(mol)
            protonation_states = get_protonation_state(Chem.MolToSmiles(mol))
            #print(protonation_states)
            optimise_smiles_geometry_and_print_xyz(protonation_states, name)
