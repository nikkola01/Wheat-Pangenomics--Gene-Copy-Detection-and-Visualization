#!/bin/bash

# Define an array of input file names
myArray=("iwgcsProt1Aprime" "iwgcsProt1Bprime" "iwgcsProt1Dprime" "iwgcsProt2Aprime" "iwgcsProt2Bprime" "iwgcsProt2Dprime" "iwgcsProt3Aprime" "iwgcsProt3Bprime" "iwgcsProt3Dprime" "iwgcsProt4Aprime" "iwgcsProt4Bprime" "iwgcsProt4Dprime" "iwgcsProt5Aprime" "iwgcsProt5Bprime" "iwgcsProt5Dprime" "iwgcsProt6Aprime" "iwgcsProt6Bprime" "iwgcsProt6Dprime" "iwgcsProt7Aprime" "iwgcsProt7Bprime" "iwgcsProt7Dprime")

# Loop over each input file name in the array
for i in ${myArray[@]}; do

    # Remove the "DB" directory, create a new one, and move the input file to the new directory
    rm -r DB/
    mkdir DB/
    mv ~/Documents/OMA.2.5.0/iwgcsProt/$i.fa ~/Documents/OMA.2.5.0/DB/

    # Create a copy of the input file with a new name
    cp ~/Documents/OMA.2.5.0/DB/$i.fa ~/Documents/OMA.2.5.0/DB/$i'1'.fa

    # Replace a line in the "parameters1.drw" file and save it as "parameters.drw"
    sed 's/OutgroupSpecies :=.*/OutgroupSpecies := ['$i'];/' parameters1.drw > parameters.drw

    # Run OMA with the "-c" option and log the start and end times to "time.txt"
    echo $i -c>> time.txt
    date>> time.txt
    ./bin/oma -c
    echo $i -c end>> time.txt
    date>> time.txt

    # Run OMA with the "-n 10 -s" options and log the start and end times to "time.txt"
    echo $i -s>> time.txt
    date>> time.txt
    ./bin/oma -n 10 -s
    echo $i -s end>> time.txt
    date>> time.txt

    # Run OMA with the "-n 10" option and log the start and end times to "time.txt"
    echo $i >> time.txt
    date>> time.txt
    ./bin/oma -n 10
    echo $i end>> time.txt
    date>> time.txt

    # Compress the output files into a ZIP archive and remove the "Output", "Cache", and "DB" directories
    zip -r $i.zip Output/ Cache/ DB/ parameters.drw
    rm -r Output/
    rm -r Cache/

done
