# Define a function to extract gene coordinates from a GFF3 file and return a dictionary containing the start and end coordinates of each gene
def getGeneCorinates():
    gene_cord = {}
    with open("iwgsc_refseqv2.1_annotation_200916_HC.gff3", "r") as fruits_file:
        tsv_reader = csv.reader(fruits_file, delimiter="\t")
        next(tsv_reader) # skip the header

            # Extract the required columns from the row
            (seqname, source, feature, start, end, score, strand, frame, attribute) = row

            # If the feature is mRNA and the gene is primer (ID ends in .1), store the gene coordinates in the dictionary
            if attribute[3:24][-2:] == ".1" and feature == "mRNA":
               gene_cord[attribute[3:24]] = (start, end)

    return gene_cord

# Define a function to read a file containing ortholog groups and return a dictionary where each key is a group ID and the corresponding value is a list of gene IDs in that group
def sepResults(fname):
    with open(fname, 'r') as f1:
        res = csv.reader(f1, delimiter="\t")
        pairs = {} # dictionary to store the gene pairs in each group
        seenBefore = [] # list to keep track of genes that have already been seen

        # Loop through each row of the file
        for row in res:
            if row[2] in pairs.keys():
                # If the gene pair is already in a group, add the second gene ID to the existing list of pairs
                pairs[row[2]].append(row[3])
                seenBefore.append(row[3])

            elif row[2] not in pairs.keys() and row[2] not in seenBefore:
                # If the gene pair is not in any group, create a new group and add the gene pair to it
                pairs[row[2]] = [row[3]]
                seenBefore.append(row[2])
                seenBefore.append(row[3])

        return pairs

# Extract gene coordinates from the GFF3 file
geneCord = getGeneCorinates()

# Separate gene pairs into ortholog groups and store the result in a dictionary
orthologGroups = sepResults("iwgcsProt1A-iwgcsProt1A1.txt")

# Create a new dictionary to store the gene coordinates for each group
orthologGroupsCoordinates= {}

# Loop through each ortholog group and create a list of gene coordinates for that group
for i in orthologGroups.keys():
    list = []
    list.append(geneCord[i]) # add the first gene ID to the list
    for j in orthologGroups[i]:
        list.append(geneCord[j]) # add the remaining gene IDs to the list
    orthologGroupsCoordinates[i] = list # store the list in the dictionary with the group ID as the key

# Print the final dictionary containing the gene coordinates for each ortholog group
print(orthologGroupsCoordinates)
print(orthologGroups)