Overview
This repository contains a Python script designed to extract gene coordinates from a GFF3 file and organize them into ortholog groups. The code processes the input files and outputs a dictionary containing gene coordinates for each ortholog group, which can be used for further analysis and investigation of the relationships between genes and their ortholog groups.

Files
gene_coordinates.py: The main Python script that contains the functions getGeneCoordinates() and sepResults() for extracting gene coordinates from a GFF3 file and organizing them into ortholog groups.

Running the Code

To run the code, follow these steps:
Install PyCharm or any other Python IDE of your choice.
Create a new PyCharm project.
Copy the gene_coordinates.py file into the project directory.
Add the necessary input files (iwgsc_refseqv2.1_annotation_200916_HC.gff3 and iwgcsProt1A-iwgcsProt1A1_inv.txt) to the project directory.
Open the gene_coordinates.py file in PyCharm.
Ensure that the correct file paths are used when calling the getGeneCoordinates() and sepResults() functions.
Run the script by clicking the 'Run' button or by pressing Shift + F10.

Notes
Please note that the current implementation uses hardcoded indices to extract gene IDs from the GFF3 file. If you wish to use the code with a different GFF3 file, you may need to adjust these indices according to the new file's formatting.

Dependencies
Python 3.6 or later
csv library (built-in with Python)