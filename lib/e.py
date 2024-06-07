import matplotlib.pyplot as plt
import numpy as np
from Bio.PDB import PDBParser

def calculate_distance(atom1, atom2):
    return np.sqrt(np.sum((atom1.coord - atom2.coord)**2))

def generate_distance_map(structure):
    atoms = [atom for atom in structure.get_atoms()] 
    num_atoms = len(atoms)
    distance_matrix = np.zeros((num_atoms, num_atoms))

    for i in range(num_atoms):
        for j in range(i + 1, num_atoms): 
            distance_matrix[i, j] = distance_matrix[j, i] = calculate_distance(atoms[i], atoms[j])

    return distance_matrix

def generate_contact_map(structure):
    residues = list(structure.get_residues())
    num_residues = len(residues)
    contact_matrix = np.zeros((num_residues, num_residues))

    for i, res1 in enumerate(residues):
        for j, res2 in enumerate(residues):
            if i != j:
                for atom1 in res1:
                    for atom2 in res2:
                        if calculate_distance(atom1, atom2) < 3.5: 
                            contact_matrix[i, j] = 1 
                            break
    return contact_matrix

def main(input_pdb_file, output_dir):

    parser = PDBParser()
    structure = parser.get_structure("protein", input_pdb_file)

    distance_map = generate_distance_map(structure)
    contact_map = generate_contact_map(structure)

    for map_data, map_name in [(distance_map, "distance_map"), (contact_map, "contact_map")]:
        plt.figure(figsize=(10, 8))
        plt.imshow(map_data, cmap='hot' if map_name == 'distance_map' else 'binary')
        plt.colorbar(label='Distance' if map_name == 'distance_map' else 'Contact')
        plt.title(f"{map_name.capitalize()} Heatmap")
        plt.savefig(f"{output_dir}/{map_name}.png")  # Example: Save as PNG
        plt.show()
  
if __name__ == "__main__":
    input_file = "ranks/rank_001_alphafold2_ptm_model_4_seed_000.pdb"
    output_dir = "output"
    main(input_file, output_dir)