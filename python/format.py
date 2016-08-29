filef = '/home/cph/status.txt'
filet = '/home/cph/status2.txt'
flag=0
with open(filet, 'w') as ft:
    with open(filef, 'r') as ff:
        for line in ff:
            line = line.split()
            if len(line) == 3 and len(line[0]) == 11:
                ft.write(line[0] + "\t" + line[1] + "\r\n")

