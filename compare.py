#Sorry for not writing comments in russian.
#Program doesn't work in cmd shell if there is russian symbols in the code.
import argparse as argprs
parser = argprs.ArgumentParser()
parser.add_argument('inputarg', type=str)
parser.add_argument('scorearg', type=str)
args = parser.parse_args()


#Reading input.txt file
inputfile = open(args.inputarg).readlines()
scorefile = open(args.scorearg, 'w+')


#Comparing files
line = 0
for line in range(len(inputfile)):
    #Data
    filesize = 0.0
    plgcnt = 0.0
    word1 = ''
    word2 = ''
    text = ''
    j=0    
    while inputfile[line][j] != ' ':
        text+=inputfile[line][j]
        j+=1
    file1 = open(text).read()
    text = ''
    j+=1
    while j < len(inputfile[line]):
        if inputfile[line][j] == '\n':
            break
        else:
            text+=inputfile[line][j]
            j+=1
    file2 = open(text).read()
    text = ''
    #Comparing given files
    for j in range(len(file1)):
        word1 = word1+file1[j]
        if file1[j] == ' ':
            if file1[j-1] != ' ':
                filesize = filesize + 1
                for i in range(len(file2)):
                    word2 = word2+file2[i]
                    if file2[i] == ' ':
                        if word1 == word2:
                            plgcnt = plgcnt+1
                            break
                        word2 = ''
            word1 = ''     
    #Writing results
    print 'Plgt level: ', plgcnt/filesize*100, '%'
    scorefile.write(str(plgcnt/filesize)+'\n')
    
#Finishing
scorefile.close()
print('Compare completed. Results has been saved.')
