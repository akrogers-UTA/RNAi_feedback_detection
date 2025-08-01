#combine_into_table.py
#To run use: python combine_into_table.py <config file> <output file>
#Last Modified: 07/24/18

import sys
import string


def run():

    if len(sys.argv) < 2:
        print('usage: python %s <list of files filename> outputfilename [-union] [-NaN symbol] [-binary] [-skipheader] [-splitby space | string] [-npIDR] [-cufflinks FAILfiledID] [-capitalize]' % sys.argv[0])
        print('	format of list of files file: label <tab> filename <tab> <label fields> <value field>' )
        print('	separate label fields with a coma: 1,2,4...' )
        print('	only use the -skipheader option if ALL input files have a header')
        sys.exit(1)
    
    files = sys.argv[1]
    outfilename = sys.argv[2]

    doCapitalize = False
    if '-capitalize' in sys.argv:
        doCapitalize = True

    splitBy='\t'
    if '-splitby' in sys.argv:
        splitBy=sys.argv[sys.argv.index('-splitby')+1]
        if splitBy == 'space':
            splitBy=' '

    doCufflinks=False
    if '-cufflinks' in sys.argv:
        doCufflinks=True
        FAILFieldID = int(sys.argv[sys.argv.index('-cufflinks')+1])
        print('will add OK/FAIL status tag to scores from field ', FAILFieldID)

    skipHeader=False
    if '-skipheader' in sys.argv:
        skipHeader=True

    doUnion=False
    if '-union' in sys.argv:
        doUnion=True

    doBinary=False
    if '-binary' in sys.argv:
        doUnion=True
        doBinary=True

    doZeros=False
    if '-NaN' in sys.argv:
        doZeros=True
        NaNReplace = sys.argv[sys.argv.index('-NaN')+1]

    donpIDR=False
    if '-npIDR' in sys.argv:
        donpIDR=True

    LabelToFileDict={}
    linelist=open(files)
    for line in linelist:
        fields=line.strip().split('\t')
        label=fields[0]
        LabelToFileDict[label]={}
        file=fields[1]
        fieldfields = fields[2].split(',')
        labelFields=[]
        for fieldID in fieldfields:
            labelFields.append(int(fieldID))
        ValueField=int(fields[3])
        LabelToFileDict[label]['file']=file
        LabelToFileDict[label]['labelFields']=labelFields
        LabelToFileDict[label]['ValueField']=ValueField

    #LabelKeys=LabelToFileDict.keys()
    #LabelKeys.sort()
    LabelKeys = sorted(LabelToFileDict.keys())
    DataDict={}
    for label in LabelKeys:
        file=LabelToFileDict[label]['file']
        linelist=open(file)
        ValueField=LabelToFileDict[label]['ValueField']
        labelFields=LabelToFileDict[label]['labelFields']
        print( label, file, ValueField, labelFields)
        i=0
        for line in linelist:
            if line.strip() == '':
                continue
            i+=1
            if i==1 and skipHeader:
                continue
            if line[0]=='#':
                continue
            fields=line.strip().split(splitBy)
            try:
                value=fields[ValueField]
            except:
                print('exiting', ValueField, fields)
                sys.exit(1)
            if donpIDR:
                value=fields[ValueField].split('npIDR "')[1].split('";')[0]
            DataID=[]
            for fieldID in labelFields:
                if doCapitalize:
                    DataID.append(fields[fieldID].capitalize())
                else:
                    DataID.append(fields[fieldID])
            DataID=tuple(DataID)
            if DataID in DataDict:
                pass
            else:
                DataDict[DataID]={}
            if doCufflinks:
                FAIL = fields[FAILFieldID]
                value = str(value) + ',' + FAIL
            DataDict[DataID][label]=value

    outfile = open(outfilename, 'w')

    outline='#'
    for fieldID in labelFields:
        outline=outline+'\t'

    for label in LabelKeys:
        outline=outline+label+'\t'

    outfile.write(outline.strip()+'\n')
        
    #DataKeys=DataDict.keys()
    #DataKeys.sort()
    DataKeys=sorted(DataDict.keys())
    badDict={}
    for DataID in DataKeys:
        Good=True
        DataIDList=list(DataID)
        outline=''
        for F in DataIDList:
            outline=outline+F+'\t'
        for label in LabelKeys:
            if doUnion:
                if doBinary:
                    if label in  DataDict[DataID]:
                        outline=outline+'1\t'
                    else:
                        outline=outline+'0\t'
                else:
                    if label in DataDict[DataID]:
                        outline=outline+DataDict[DataID][label]+'\t'
                    elif doZeros:
                        outline=outline + NaNReplace + '\t'
                    else:
                        outline=outline+'NaN\t'
            else:
                if label in DataDict[DataID]:
                    outline=outline+DataDict[DataID][label]+'\t'
                else:
                    if DataID in badDict:
                        pass
                    else:
                        print( DataID, 'not found in all datasets, skipping')
                        badDict[DataID]=''
                    Good=False
                    continue
        if doUnion:
            outfile.write(outline.strip()+'\n')
        else:
            if Good:
                outfile.write(outline.strip()+'\n')
 
    print('Problematic:', len(badDict.keys()))
   
    outfile.close()
            
run()

