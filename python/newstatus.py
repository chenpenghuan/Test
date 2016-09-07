with open('status2.txt','w') as f2:
    with open('status.txt','r') as f:
        for line in f:
            line=line.split()
            if int(line[-1])==1:
                f2.write(line[0]+"\t"+line[1]+"\n")

