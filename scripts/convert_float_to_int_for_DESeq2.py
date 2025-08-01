#Changes floats to ints in table from Salmon for DESeq2
#To Run: python convert_float_to_int_for_DESeq2.py <tablefile> <outputTable>
#Created By: Alicia Rogers
#Last Modified: 5/30/2012

import sys

#Open files
inputTable = open(sys.argv[1], 'r')
outputTable = open(sys.argv[2], 'w')

#Read in the inputTable
for line in inputTable:
	#ID, start, stop, sample1, sample2, sample3, sample4, sample5, sample6, sample7, sample8 = line.split()
	#ID, start, stop, sample1, sample2, sample3, sample4 = line.split()
	#ID, start, stop, Name, Class, Family, sample1, sample2 = line.split()
	#ID, start, stop, sample1, sample2 = line.split()
	#ID, sample1, sample2 = line.split()
	#ID, sample1, sample2, sample3, sample4 = line.split()
	#ID, sample1, sample2, sample3, sample4, sample5, sample6, sample7, sample8 =line.split()
	#ID, sample1, sample2, sample3, sample4, sample5, sample6, sample7, sample8, sample9, sample10 = line.split()
	
	ID, sample1, sample2, sample3, sample4, sample5, sample6=line.split()
	
	#Print Header to output table
	if ID == "#":
		outputTable.write(line)
	elif ID != "Geneid":
		newS1 = int(round(float(sample1), 0))
		newS2 = int(round(float(sample2), 0))
		newS3 = int(round(float(sample3), 0))
		newS4 = int(round(float(sample4), 0))
		newS5 = int(round(float(sample5), 0))
		newS6 = int(round(float(sample6), 0))
		#newS7 = int(round(float(sample7), 0))
		#newS8 = int(round(float(sample8), 0))
        	#newS9 = int(round(float(sample9), 0))
		#newS10 = int(round(float(sample10), 0))
		

		outputTable.write(ID + '\t' + str(newS1) + '\t' + str(newS2) + '\t' + str(newS3) + '\t' + str(newS4) + '\t' + str(newS5) +'\t' + str(newS6) +'\n')
		#outputTable.write(ID + '\t' + str(newS1) + '\t' + str(newS2) + '\t' + str(newS3) + '\t' + str(newS4) + '\t' + str(newS5) +'\t' + str(newS6) +'\t' + str(newS7) +'\t' + str(newS8) + '\n')
		#outputTable.write(ID + '\t' + str(newS1) + '\t' + str(newS2) + '\t' + str(newS3) + '\t' + str(newS4) + '\t' + str(newS5) +'\t' + str(newS6) +'\t' + str(newS7) +'\t' + str(newS8) +'\t' + str(newS9) + '\t' + str(newS10) + '\n')
		#outputTable.write(ID + '\t' + start + '\t' + stop + '\t' + str(newS1) + '\t' + str(newS2) + '\t' + str(newS3) + '\t' + str(newS4) + '\t' + str(newS5) +'\t' + str(newS6) +'\t' + str(newS7) +'\t' + str(newS8) +'\n')
		#outputTable.write(ID + '\t' + start + '\t' + stop + '\t' + str(newS1) + '\t' + str(newS2) + '\t' + str(newS3) + '\t' + str(newS4) +'\n')
		#outputTable.write(ID + '\t' + start + '\t' + stop + '\t' + Name + '\t' + Class + '\t' + Family + '\t' + str(newS1) + '\t' + str(newS2) + '\n')
		#outputTable.write(ID + '\t' + start + '\t' + stop + '\t' + str(newS1) + '\t' + str(newS2) + '\n')
		#outputTable.write(ID + '\t' + str(newS1) + '\t' + str(newS2) + '\n')
		#outputTable.write(ID + '\t' + str(newS1) + '\t' + str(newS2) + '\t' + str(newS3) + '\t' + str(newS4) +'\n')
#Close files
inputTable.close()
outputTable.close()
