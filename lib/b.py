import argparse

def create_fragments(genome, k):
    output_path = rf"output\reads.fasta"

    try:
        with open(output_path, "w") as file:
            n = len(genome)
            for i in range(n - k + 1):
                file.write(f">{i + 1}\n")
                file.write(genome[i:i + k] + "\n")

    except IOError:
        print(f"Could not write to file: {output_path}")

def count_fragments(genome, k):
    n = len(genome)
    return n - k + 1

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--genome', help='Input file name', required=True)
    args = parser.parse_args()
    genome = args.genome

    if genome:
        fragment_size = 31
        create_fragments(genome, fragment_size)
        print(f"Number of fragments in the sequence: {count_fragments(genome, fragment_size)}")

