from case_config import *

i = 1
# TODO: Change the number of Total Timespells
while i <= 32:
    edgelistname = "{}Edgelist".format(case) + str(i) + ".edgelist"
    newedgelist = "{}EdgelistOut".format(case) + str(i) + ".edgelist"
    lines_seen = set()  # holds lines already seen
    outfile = open(newedgelist, "w")
    infile = open(edgelistname, "r")
    for line in infile:
        # print (line)
        if line not in lines_seen:  # not a duplicate
            outfile.write(line)
            lines_seen.add(line)
    outfile.close()
    i+=1
