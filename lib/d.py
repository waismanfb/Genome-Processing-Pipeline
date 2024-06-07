import argparse
import os
import re
from Bio import SeqIO

CODON_TO_AMINO_ACID = {
    'TTT': 'F', 'TTC': 'F', 'TTA': 'L', 'TTG': 'L',
    'TCT': 'S', 'TCC': 'S', 'TCA': 'S', 'TCG': 'S',
    'TAT': 'Y', 'TAC': 'Y', 'TAA': '*', 'TAG': '*',
    'TGT': 'C', 'TGC': 'C', 'TGA': '*', 'TGG': 'W',
    'CTT': 'L', 'CTC': 'L', 'CTA': 'L', 'CTG': 'L',
    'CCT': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    'CAT': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'CGT': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
    'ATT': 'I', 'ATC': 'I', 'ATA': 'I', 'ATG': 'M',
    'ACT': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
    'AAT': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
    'AGT': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
    'GTT': 'V', 'GTC': 'V', 'GTA': 'V', 'GTG': 'V',
    'GCT': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
    'GAT': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
    'GGT': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
}

def translate_codon(codon):
    return CODON_TO_AMINO_ACID[codon]

def translate_sequence_to_amino_acids(sequence_file_path):
    with open(sequence_file_path, "r") as sequence_file:
        sequence = SeqIO.read(sequence_file, "fasta").seq
        return ''.join(translate_codon(sequence[i:i+3]) for i in range(0, len(sequence), 3))
    
def find_spike_protein_in_cds_files():
    for cds_file in os.listdir('cds'):
        amino_acid_sequence = translate_sequence_to_amino_acids(f"cds\{cds_file}")
        spike_protein_pattern = re.compile('G[RKH][RKH][DE]G')
        if re.search(spike_protein_pattern, amino_acid_sequence):
            print(f"Spike protein was found in {cds_file}")
            return amino_acid_sequence

def save_spike_protein_sequence(spike_protein_sequence):
    with open("output/spike.fasta", "w") as output_file:
        output_file.write(f">Spike protein\n{spike_protein_sequence}\n")
    print("Spike protein sequence was saved successfully to output/spike.fasta")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--genome', help='Input file name', required=True)
    args = parser.parse_args()
    genome = args.genome

    spike_protein_sequence = find_spike_protein_in_cds_files()
    save_spike_protein_sequence(spike_protein_sequence)


        


