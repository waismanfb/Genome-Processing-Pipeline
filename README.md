# Genome Processing
## Studying a virus's genome
The capsid is a protein structure that surrounds a virus's genetic material. The main function of the capsid is to protect and encapsulate the viral genetic material during transmission and infection. 

This pipeline consists of five modules, each located in the `lib` folder. Each module solves a specific problem related to the processing and analysis of the viral genome.

## Modules
### Module A: Genome Reader
- Reads the genome file present in the `genome.fasta` file.
- Prints the size of the sequence.
- Calculates and prints the GC content of the genome.

### Module B: Sequence Fragmenter
- Splits the sequence into fragments of size k = 31 using a sliding window technique.
- Saves the fragments in a multi-FASTA file named `reads.fasta` inside a folder named `output`.
- Calculates and prints the number of sequences stored in the `reads.fasta` file.
> **Information:** Each sequence is identified by a number and has a header line starting with ">"

### Module C: Coding Region Identifier
- Identifies all coding regions (CDS) in the genome.
- Saves each CDS in a FASTA format file. The files are saved in the `cds` folder.
> **Information:** A coding region starts with a methionine (ATG) and ends with a stop codon (TAA, TAG or TGA). 

### Module D: Spike Protein Identifier
- Identifies the gene that encodes the SPIKE protein.
- Saves the SPIKE protein in a file named `spike.fasta` inside of the `output` folder.
> **Information:** The SPIKE protein contains a region of significant importance characterized by a specific sequence of five amino acids: a glycine (G), followed by two positively charged polar amino acids (R, K, or H), a negatively charged polar amino acid (D or E), and another glycine (G).

# Pipeline Execution

This pipeline processes genome data. Here's how to run it:

1. Open your terminal.
2. Navigate to the directory where the `genome_processing.py` file is located. 
3. Once you're in the correct directory, you can run the pipeline by typing:
```python genome_processing.py -i genoma.fasta```

# Pipeline Struct 
The pipeline structure involves the following steps:

1. Initially, the pipeline executes module A to retrieve the genome. This process necessitates providing the input file using the -i or --input argument.
2. Subsequently, for the execution of modules B, C, and D, the pipeline mandates the presence of the genome information, which is acquired during the execution of module A. This genome information needs to be provided using the -i or --genome argument.