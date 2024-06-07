import subprocess

def run_script_a_and_return_genome(input_file):
    process = subprocess.run(['python', 'lib/a.py', '-i', input_file], capture_output=True, text=True)
    output_lines = process.stdout.strip().split('\n')
    print(output_lines[0], output_lines[1], sep='\n')
    genome = output_lines[2]
    return genome

def run_scripts_in_sequence_with_genome(scripts, genome):
    for script in scripts:
        process = subprocess.run(['python', script, '-i', genome], capture_output=True, text=True)
        print(process.stdout)

if __name__ == "__main__":
    input_file = 'genoma.fasta'
    scripts = ['lib/b.py', 'lib/c.py', 'lib/d.py']
    genome = run_script_a_and_return_genome(input_file)
    run_scripts_in_sequence_with_genome(scripts, genome)