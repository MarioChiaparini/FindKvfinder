from rdkit import Chem
from rdkit.Chem.rdMolTransforms import ComputeCentroid
from vina import Vina
from rdkit.Chem import rdFMCS
from rdkit.Chem import AllChem

v = Vina(sf_name='vina')
lig = Chem.MolFromMolFile('/home/ABTLUS/mario.neto/Desktop/ligantes/ligante5kdir.sdf',sanitize=False)

for conf in lig.GetConformers():

    centroid = Chem.rdMolTransforms.ComputeCentroid(conf)
    x = centroid[0]
    y = centroid[1]
    z = centroid[2]

v.set_receptor('/home/ABTLUS/mario.neto/Desktop/receptores/5kdirout.pdbqt')
v.set_ligand_from_file('/home/ABTLUS/mario.neto/Desktop/ligantes/outligand.pdbqt')
print("x: %f",x)
print("y: %f",y)
print("z: %f",z)

v.compute_vina_maps(center=[x, y, z], box_size=[30, 30,30])
 
energy_minimized = v.optimize()
print('Score after minimization : %.3f (kcal/mol)' % energy_minimized[0])
v.write_pose('1iep_ligand_minimized.pdbqt', overwrite=True)

# Dock the ligand
v.dock(exhaustiveness=32, n_poses=30)
v.write_poses('1iep_ligand_vina_out.pdbqt', n_poses=30, overwrite=True)


