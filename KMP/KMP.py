import os

# function to read a fasta file and return the reads in a dictionary
def readFasta(name):
    # Check if the file specified by name exists
    if not (os.path.exists(name)):
        return

    # dictionary to store the reads
    reads = {}
    # string to store the sequence for a read
    sequence = ''

    # open the file and read each line
    with open(name) as file_one:
        for line in file_one:
            line = line.strip()
            # skip empty lines
            if not line:
                continue
            # If the line starts with ">", store the previous read (if any) and reset the sequence string
            if line.startswith(">"):
                if (len(sequence) != 0):
                    # store the previous read to the dictionary
                    reads.update({active_sequence_name: sequence})
                    # reset the sequence string
                    sequence = ''
                # Store the name of the current read
                s = line.split(" ")[0][1:]
                active_sequence_name = line.split(" ")[0][1:]
                # remove the suffix after '.' in the read name (if needed)
                """if(s.find('.')):
                    active_sequence_name = s[:-2]
                else:
                    active_sequence_name = line.split(" ")[0][1:]
                continue"""
            # concatenate the sequence lines for the current read
            sequence += line
        # store the last read to the dictionary
        reads.update({active_sequence_name: sequence})
    return reads
    
# function to implement the Knuth-Morris-Pratt (KMP) algorithm to find all the occurrences of a pattern in a text
def kmp(text, pattern):
    # length of the text
    n = len(text)
    # length of the pattern
    m = len(pattern)

    # Compute the failure function
    # list to store the failure function
    F = [0] * m
    # index to keep track of the current position in the pattern
    j = 0
    for i in range(1, m):
        while j > 0 and pattern[j] != pattern[i]:
            j = F[j - 1]
        if pattern[j] == pattern[i]:
            j += 1
        F[i] = j

    # Search for matches in the input string
    # index to keep track of the current position in the pattern
    j = 0
    # list to store the positions of the matches
    positions = []
    for i in range(n):
        while j > 0 and pattern[j] != text[i]:
            j = F[j - 1]
        if pattern[j] == text[i]:
            j += 1
        if j == m:
            # append the position of the match
            positions.append(i - j + 1)
            j = F[j - 1]

    return positions


# dictionary to store the genes and their corresponding sequences
#genes = readFasta("iwgsc_refseqv2.1_annotation_200916_HC_cds.fasta")
genes = {"1":"ATCTT", "2":"CTTB", "3":"ATCTT", "4":"ATCTB"} 

# dictionary to store the matches between genes
matchTable = {}

# loop through each gene to find matches with other genes
for i in genes.keys():

    # variable to store the number of matches for a gene
    numMaches = 0

    # list to store the matches for a gene
    matches = []

    # loop through other genes to find matches with the current gene
    for j in genes.keys():

        # skip the current gene if it is checking with itself
        if i == j:
            continue

        # call the kmp function to find matches between two genes
        k = kmp(genes[i], genes[j])

        # if there are matches, update the number of matches and the matches list
        if k != []:
            numMaches += len(k)
            matches.append(j)

    # if the number of matches is greater than 0, add the gene and its matches to the matchTable
    if numMaches > 0:
        matchTable.update({i: matches})

# print the final matchTable
print(matchTable)
#KMP: {'1': ['3'], '3': ['1']}