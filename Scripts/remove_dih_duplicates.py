#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser(description='Removes duplicate and zero dihedral entropy values from CodeEntropy output')
parser.add_argument('dihfile', help='input dihedral file')
args = parser.parse_args()

outfile = "dih_entropy.txt"
dihedral = {}

def read_dihedrals(file):
    global dihedral
    stot = 0
    with open(file, 'r') as f, open(outfile, 'w') as out:
        for line in f:
            if not line.startswith('Dihedral'):
                continue
            line = line.strip().split()
            atom2, atom3, entropy = line[2], line[3], float(line[6])
            if atom2 in dihedral and atom3 in dihedral[atom2]:
                out.write(" ".join(line) + " Duplicate\n")
                continue
            if atom3 in dihedral and atom2 in dihedral[atom3]:
                out.write(" ".join(line) + " Duplicate\n")
                continue
            if entropy <= 0:
                out.write(" ".join(line) + " zero entropy\n")
                continue
            out.write(" ".join(line) + "\n")
            dihedral.setdefault(atom2, {})[atom3] = 1
            dihedral.setdefault(atom3, {})[atom2] = 1
            stot += entropy
    print("{:.4f}".format(stot))

read_dihedrals(args.dihfile)
