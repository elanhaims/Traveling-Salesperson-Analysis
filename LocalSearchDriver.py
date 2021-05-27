import os
import sys

#graph_size = int((sys.argv)[1])
i = 30
while i <=30:
    for x in range(18,31):
        os.system("python LocalSearch.py < graphs/infile%02d_%02d.txt" % (i, x))
    i += 5

