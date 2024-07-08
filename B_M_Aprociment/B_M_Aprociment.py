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
                    """
                continue
            # concatenate the sequence lines for the current read
            sequence += line
        # store the last read to the dictionary
        reads.update({active_sequence_name: sequence})
    return reads
    
# function to implement a modified version of the Boyer-Moore algorithm that allows for 20% mismatches
def boyer_moore_20_mismatch(text, pattern):
    # length of the text
    n = len(text)
    # length of the pattern
    m = len(pattern)
    # maximum number of mismatches allowed (20% of the pattern length)
    max_mismatch = m // 5
    # list to store the positions of the matches
    positions = []

    # loop through the text to find matches with the pattern
    for i in range(n - m + 1):
        # variable to keep track of the current position in the pattern
        j = 0
        # variable to keep track of the number of mismatches
        mismatch = 0
        # check for exact matches
        while j < m and text[i + j] == pattern[j]:
            j += 1
        # if all characters match, add the position to the list of positions
        if j == m:
            positions.append(i)
        else:
            # check for mismatches
            for k in range(j, m):
                if text[i + k] != pattern[k]:
                    mismatch += 1
                # break if the number of mismatches exceeds max_mismatch
                if mismatch > max_mismatch:
                    break
            # if the number of mismatches does not exceed max_mismatch, add the position to the list of positions
            if mismatch <= max_mismatch:
                positions.append(i)
    return positions


# dictionary to store the genes and their corresponding sequences
#genes = readFasta("iwgcsProt1A_prime_only.fa")
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
        k = boyer_moore_20_mismatch(genes[i], genes[j])

        # if there are matches, update the number of matches and the matches list
        if k != []:
            numMaches += len(k)
            matches.append(j)

    # if the number of matches is greater than 0, add the gene and its matches to the matchTable
    if numMaches > 0:
        matchTable.update({i: matches})

# print the final matchTable
print(matchTable) 
#BOYER-MORE: {'1': ['3', '4'], '3': ['1', '4'], '4': ['1', '3']}