#sum_isoforms_for_DESeq2.py
#To run use: python sum_isoforms_for_DESeq2.py <input quant.sf file> <output file>
#Created by:Alicia Rogers
#Last Modified: 07/24/18

import sys
import re

#read in file
inputFile = open(sys.argv[1], 'r')
output = open(sys.argv[2], 'w')

new_gene=0
tot_reads = 0.0
reset = 0
for line in inputFile:
	name, length, eff_length, TPM, reads = line.split()
	numreads=reads.strip('\n')
	if new_gene == 0:
		base_name, dot, *optional = name.split('.')
		new_gene=1
		new_dot = re.sub(r'[a-z]+', '', dot)
		tot_reads = float(numreads)
	
	elif new_gene != 0:
		g_name, g_dot, *optional = name.split('.')
		new_gdot = re.sub(r'[a-z]+', '', g_dot)
		if g_name == base_name:
			if new_dot == new_gdot:
				tot_reads += float(numreads)
				reset = 0
			else:
				output.write(base_name+"."+new_dot+'\t'+ str(tot_reads)+'\n')
				reset = 1
		else:		
			output.write(base_name+"."+new_dot+'\t'+ str(tot_reads)+'\n')
			reset = 1
			
	if reset == 1:
		#reset gene
		tot_reads=float(numreads)
		base_name=g_name
		new_dot=new_gdot
		reset = 0
			
#print last gene
output.write(base_name+"."+new_dot+'\t'+ str(tot_reads)+'\n')


#Close files
inputFile.close()
output.close()

