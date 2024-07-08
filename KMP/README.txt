This repository contains a Python script that implements the Knuth-Morris-Pratt (KMP) algorithm to find all occurrences of a pattern in a given text. The script reads in a FASTA file containing gene sequences and then searches for matches between the genes using the KMP algorithm. The results are stored in a dictionary (matchTable), which displays the gene IDs and their corresponding matches.

Prerequisites
Python 3.x
PyCharm or any other Python IDE

Running the Script
1. Create a new PyCharm project or open an existing project in your preferred Python IDE.
2. Add the Python script to your project.
3. (Optional) Update the input FASTA file path in the readFasta() function call or use the provided test dictionary genes.
4. Run the script in your IDE.

Understanding the Code
The script contains two main functions:

1. readFasta(name): This function reads a FASTA file and returns the reads in a dictionary. It checks if the input file exists, opens it, and reads each line to extract the gene IDs and sequences. The sequences are concatenated and stored in a dictionary with the gene IDs as keys.

2. kmp(text, pattern): This function implements the Knuth-Morris-Pratt algorithm to find all occurrences of a pattern in a given text. It calculates the failure function and searches for matches in the input string. The positions of the matches are stored in a list and returned by the function.

The main part of the script loops through each gene in the input data and calls the kmp() function to find matches between genes. The matches are stored in a dictionary (matchTable), which is printed at the end of the script execution.

Output
The script outputs a dictionary (matchTable) with gene IDs as keys and lists of matching gene IDs as values. This provides a clear overview of the matches found between the genes in the input data.