import os

"""
This function reads a FASTA file and returns a dictionary where the keys are the
sequence names and the values are the sequences themselves.

:param file_path: the path to the input FASTA file
:return: a dictionary containing the sequences in the FASTA file
"""
def readFastaProt(file_path):
    
    # Check if the file specified by file_path exists
    if not os.path.exists(file_path):
        return
    
    # Initialize the reads dictionary and sequence string
    reads = {}
    sequence = ''
    
    with open(file_path) as file:
        # Loop over each line in the file
        for line in file:
            line = line.strip()
            if not line:
                continue
            
            # If the line starts with ">", store the previous read (if any) and reset the sequence string
            if line.startswith(">"):
                if len(sequence) != 0:
                    reads.update({active_sequence_name: sequence})
                    sequence = ''
                
                # Store the name of the current read
                active_sequence_name = line[1:]
                continue
            
            # Append the current line to the current sequence
            sequence += line
        
        # Store the last read to the dictionary
        reads.update({active_sequence_name: sequence})
    
    return reads

"""
This function takes a chromosome identifier as input and writes the protein sequences
corresponding to that chromosome to a new FASTA file.

:param chr: the chromosome identifier to filter on
"""
def sepProtFastaFile(chr):
   
    # Construct the output file name
    output_file_name = f"iwgcsProt{chr}_prime_only.fa"
    
    # Open the output file for writing
    with open(output_file_name, 'w') as output_file:
        # Read the input FASTA file into a dictionary
        sequence_dict = readFastaProt("iwgsc_refseqv2.1_annotation_200916_HC_pep.fasta")
        
        # Loop over each sequence in the dictionary
        for sequence_name, sequence in sequence_dict.items():
            # Check if the sequence name matches the chromosome identifier and ends with ".1"
            if sequence_name[7:9] == chr and sequence_name[-2:] == ".1":
                # Write the sequence to the output file in FASTA format
                output_file.write(">" + sequence_name + "\n")
                output_file.write(sequence + "\n")

		
#sepProFastaFile("1A")
