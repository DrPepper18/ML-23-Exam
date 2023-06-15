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
for line in range(len(inputfile)):
    #Data
    filesize = plgcnt = 0.0 
    task = inputfile[line].split()
    file1 = open(task[0]).read().split()
    file2 = open(task[1]).read().split()
    filesize = len(file1)
    #Comparing given files
    for j in range(len(file1)):
        for i in range(len(file2)):
            if file1[j] == file2[i]:
                plgcnt+=1
                break
    #Writing results
    print('Plgt level: ', str(plgcnt/filesize*100)[:5], '%')
    scorefile.write(str(plgcnt/filesize)[:5]+'\n')
#Finishing
scorefile.close()
print('Compare completed. Results has been saved. Press [Enter] to quit.')
input()
