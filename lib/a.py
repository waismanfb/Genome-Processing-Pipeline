import argparse

def read_genome(input_file):
    try:
        with open(input_file, "r") as file:
            genome = ''.join(line.strip() for line in file.readlines()[1:])
            return genome.upper()
        
    except FileNotFoundError:
        print(f"File not found: {input_file}")
        return None

def gc_content(genome):
    if not genome:
        return 0.0    
    
    gc_count = genome.count("G") + genome.count("C")
    return gc_count / len(genome)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', help='Input file name', required=True)
    args = parser.parse_args()

    genome = read_genome(args.input)
    print(f"Genome size: {len(genome)}")
    print(f"GC content: {gc_content(genome) * 100:.2f}%")
    print(genome)

