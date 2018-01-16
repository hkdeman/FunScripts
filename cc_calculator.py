from os import listdir
from os.path import isfile, join


mypath = "vcs/"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

for f in onlyfiles:
    node = 0
    functions_o_classes = 0
    fil = open(mypath+f).read().splitlines()
    inside_flow_braces = ""
    for i in range(len(fil)):
        line = fil[i]
        split_line = line.split(" ")
        if(len(split_line)>3):
            node+=1
            functions_o_classes +=1

        if "{" in line:
            node+=1
            anything_there = ""
            closing_or_opening_found = False
            j = i+1
            while(not closing_or_opening_found):
                if "{" not in line:
                    anything_there+=line
                    print(line)
                else:
                    closing_or_opening_found=True
                    break
                j+=1
                line = fil[j]
            if(anything_there!=""):
                node+=1
    node+=functions_o_classes
    print("number of nodes in "+f+":"+str(node))
