Project Overview
This project contains a Python script for processing and manipulating FASTA files containing protein sequences. The script provides functions for reading and parsing FASTA files, filtering protein sequences based on a specified chromosome identifier, and writing the filtered protein sequences to a new FASTA file.

Files
The project contains the following files:

fasta_processing.py: This is the main Python script containing the readFastaProt() and sepProtFastaFile() functions, which handle reading, parsing, filtering, and writing FASTA files.
iwgsc_refseqv2.1_annotation_200916_HC_pep.fasta: This is the input FASTA file containing protein sequences. It is essential that this file is present in the project directory for the script to function correctly.

Usage
1. To run the code using PyCharm, follow these steps:

2. Create a new PyCharm project.

3. Add the fasta_processing.py and iwgsc_refseqv2.1_annotation_200916_HC_pep.fasta files to the project directory. Ensure that the input FASTA file is present in the project directory, as the script relies on it to function correctly.

4. In PyCharm, right-click on the fasta_processing.py file in the project directory and select 'Run'.

5. The script will read the input FASTA file, filter the protein sequences based on the specified chromosome identifier, and write the filtered sequences to a new FASTA file in the project directory.

Dependencies
The project requires Python 3.6 or higher.

Note
Remember that the input FASTA file (iwgsc_refseqv2.1_annotation_200916_HC_pep.fasta) is crucial for the script's proper functioning. Make sure it is located in the same directory as the fasta_processing.py script before running the code. If your input file has a different name, adjust the file name accordingly in the sepProtFastaFile() function.