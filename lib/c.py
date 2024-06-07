import argparse

START_CODON = 'ATG'
STOP_CODONS = ["TAA", "TAG", "TGA"]

def find_coding_sequences(seq):
    coding_sequences = []
    i = 0

    while i < len(seq):
        if seq[i:i+3] == START_CODON:
            for j in range(i, len(seq), 3):
                if seq[j:j+3] in STOP_CODONS and len(seq[i:j+3]) % 3 == 0:
                    coding_sequences.append(seq[i:j+3])  
                    i = j + 3
                    break
            else:
                i += 3
        else:
            i += 3

    return coding_sequences


def save_coding_sequences(coding_sequences):
    output_dir="cds"

    for i, sequence in enumerate(coding_sequences):
        with open(f"{output_dir}/cds_{i + 1}.fasta", "w") as file:
            file.write(f">Coding_sequence_{i + 1}\n")
            file.write(sequence)
            
    print(f"All {len(coding_sequences)} sequences were successfully saved to the /{output_dir} folder.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--genome', help='Input file name', required=True)
    args = parser.parse_args()
    genome = args.genome

    if genome:
        coding_sequences = find_coding_sequences(genome)
        save_coding_sequences(coding_sequences)



