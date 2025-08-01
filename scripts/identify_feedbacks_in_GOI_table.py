
import sys

#####################################################################################################################
#TO RUN:                                                                                                            #
# python identify_feedbacks_in_GOI_table.py <GOI list> <mRNA_DESeq_Results> <small RNA_DESeq_Results> <output file> #                                                                             
#####################################################################################################################

#READ IN A LIST OF GENES OF INTEREST
GOI_file = open(sys.argv[1], 'r')
GOI = []

for line in GOI_file:
	gene, id, chrm, start, end = line.split()
	
	item = [gene, id, chrm, start, end]
	GOI.append(item)

GOI_file.close()
print(str(len(GOI)) + " GENES OF INTEREST")

#READ IN MRNA-SEQ DESEQ RESULTS
mRNA_file = open(sys.argv[2], 'r')
mRNA = []

for line in mRNA_file:
	if "log2FoldChange" not in line:
		line=line.strip('\n')
		line=line.replace('"', '')
		id, bMean, l2FC, lfcSE, stat, pV, pJ = line.split(" ")
	
		item = [id, l2FC, pV, pJ]
		mRNA.append(item)

mRNA_file.close()

#READ IN smallRNA-SEQ DESEQ RESULTS
smallRNA_file = open(sys.argv[3], 'r')
smallRNA = []

for line in smallRNA_file:
	if "log2FoldChange" not in line:
		line=line.strip('\n')
		line=line.replace('"', '')
		id, bMean, l2FC, lfcSE, stat, pV, pJ = line.split(" ")
	
		item = [id, l2FC, pV, pJ]
		smallRNA.append(item)

smallRNA_file.close()

#OPEN OUTPUT FILE 		
output = open(sys.argv[4], 'w')
output.write("GENE" + '\t' + "ID" + '\t' + "CHR" + '\t' + "START" + '\t' + "END" + '\t' + "mRNA_l2FC" + '\t' + "mRNA_pV" + '\t' + "mRNA_pJ" + '\t' + "smallRNA_l2FC" + '\t' + "smallRNA_pV" + '\t' + "smallRNA_pJ" + '\n')

count = 0 

#FOR EACH GOI, PRINT mRNA and SMALL RNA DATA INTO OUTPUT FILE
for x in GOI:
	mRNA_found = 0
	smallRNA_found = 0

	for y in mRNA:
		if y[0] == x[1]:
			mRNA_l2FC = y[1]
			mRNA_pV = y[2]
			mRNA_pJ = y[3]
			mRNA_found = 1
	
	for z in smallRNA:
		if z[0] == x[1]:
			smallRNA_l2FC = z[1]
			smallRNA_pV = z[2]
			smallRNA_pJ = z[3]
			smallRNA_found = 1

	if mRNA_found == 1 and smallRNA_found == 1:
		count += 1
		output.write(x[0] + '\t' + x[1] + '\t' + x[2] + '\t' + x[3] + '\t' + x[4] + '\t' + mRNA_l2FC + '\t' + mRNA_pV + '\t' + mRNA_pJ + '\t' + smallRNA_l2FC + '\t' + smallRNA_pV + '\t' + smallRNA_pJ + '\n')
	elif mRNA_found == 1 and smallRNA_found == 0:
		output.write(x[0] + '\t' + x[1] + '\t' + x[2] + '\t' + x[3] + '\t' + x[4] + '\t' + mRNA_l2FC + '\t' + mRNA_pV + '\t' + mRNA_pJ + '\t' + "not_found" + '\t' + "not_found" + '\t' + "not_found" + '\n')
		count += 1
	elif mRNA_found == 0 and smallRNA_found == 1:
		output.write(x[0] + '\t' + x[1] + '\t' + x[2] + '\t' + x[3] + '\t' + x[4] + '\t' + "not_found" + '\t' + "not_found" + '\t' + "not_found" + '\t' + smallRNA_l2FC + '\t' + smallRNA_pV + '\t' + smallRNA_pJ + '\n')
		count += 1

print("TOTAL NUMBER OF GENES OF INTEREST PROCESSED: " + str(count))


output.close()
