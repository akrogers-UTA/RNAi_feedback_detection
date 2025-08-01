#Removes genes not expressed in any samples from a table prior to DESeq2
#To run use: python remove_genes_not_expressed_in_any_samples.py <input integer table file> <output file>
#Created by:Alicia Rogers
#Last Modified: 07/24/18

import sys

#Open files
inputTable = open(sys.argv[1], 'r')
outputTable = open(sys.argv[2], 'w')

#Read in the inputTable
for line in inputTable:
	line.strip('\n')

	#ID, sample1, sample2 = line.split()
	#ID, sample1, sample2, sample3, sample4 = line.split()
	#ID, sample1, sample2, sample3, sample4, sample5, sample6, sample7, sample8 =line.split()
	#ID, sample1, sample2, sample3, sample4, sample5, sample6, sample7, sample8, sample9, sample10 = line.split()
	
	ID, sample1, sample2, sample3, sample4, sample5, sample6=line.split()
	
	#Print Header to output table
	if ID == "#":
		outputTable.write(line)
	else:
		#if int(sample1) != 0 or  int(sample2) != 0 or int(sample3) != 0 or int(sample4) != 0 or int(sample5) != 0 or int(sample6) != 0 or int(sample7) != 0 or int(sample8) != 0:
		if int(sample1) != 0 or  int(sample2) != 0 or int(sample3) != 0 or int(sample4) != 0 or int(sample5) != 0 or  int(sample6) != 0:
		#if int(sample1) != 0 or  int(sample2) != 0 or int(sample3) != 0 or int(sample4) != 0:
			outputTable.write(line)
#close files
inputTable.close()
outputTable.close()
