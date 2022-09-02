from rdkit import Chem
from rdkit.Chem.rdMolTransforms import ComputeCentroid
from vina import Vina
from rdkit.Chem import rdFMCS
from rdkit.Chem import AllChem
import streamlit as st

st.title("Molecular Docking Simulation Web Application - Virtual Screening Drug Desing")

v = Vina(sf_name='vina')

receptor = st.file_uploader("Choose a pdbqt receptor: ")
ligand_sdf = st.file_uploader("Choose a sdf ligand: ")
ligand_pdb = st.file_uploader("Choose a pdbqt ligand: ")

rec = str('/home/ABTLUS/mario.neto/Desktop/receptores/'+receptor.name)
ligandsdf = str('/home/ABTLUS/mario.neto/Desktop/ligantes/'+ligand_sdf.name)
ligandpdb = str('/home/ABTLUS/mario.neto/Desktop/ligantes/'+ligand_pdb.name)

lig = Chem.MolFromMolFile(f'{ligandsdf}',sanitize=False)

for conf in lig.GetConformers():
    centroid = Chem.rdMolTransforms.ComputeCentroid(conf)
    x = centroid[0]
    y = centroid[1]
    z = centroid[2]

v.set_receptor(f'{rec}')
v.set_ligand_from_file(f'{ligandpdb}')
print("x: %.3f",x)
print("y: %.3f",y)
print("z: %.3f",z)

v.compute_vina_maps(center=[x, y, z], box_size=[40, 40, 40])
 
energy_minimized = v.optimize()
print('Score after minimization : %.3f (kcal/mol)' % energy_minimized[0])
v.write_pose('1iep_ligand_minimized.pdbqt', overwrite=True)

v.dock(exhaustiveness=32, n_poses=30)
v.write_poses('1iep_ligand_vina_out.pdbqt', n_poses=30, overwrite=True)
