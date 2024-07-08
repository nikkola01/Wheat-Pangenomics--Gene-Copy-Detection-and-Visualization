Project Overview
This project contains a Python script for comparing and identifying similar sequences in a collection of genes. The script provides functions for reading FASTA files, implementing a modified version of the Boyer-Moore algorithm that allows for 20% mismatches, and identifying the matches between the genes.

Files
The project contains the following file:

sequence_comparison.py: This is the main Python script containing the readFasta(), boyer_moore_20_mismatch(), and the main code block, which handles reading gene sequences, finding matches between genes, and printing the final match table.
Usage
To run the code using PyCharm, follow these steps:

Create a new PyCharm project.

Add the sequence_comparison.py file to the project directory.

Ensure that the input FASTA file (e.g., iwgcsProt1A_prime_only.fa) is present in the project directory. The script relies on this file to read the gene sequences. If your input file has a different name, adjust the file name accordingly in the readFasta() function call in the sequence_comparison.py script.

In PyCharm, right-click on the sequence_comparison.py file in the project directory and select 'Run'.

The script will read the gene sequences from the input FASTA file, find matches between the genes using the modified Boyer-Moore algorithm, and print the final match table in the output console.

Dependencies
The project requires Python 3.6 or higher.
