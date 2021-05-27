import os
import sys

graph_size = int((sys.argv)[1])

for x in range(1,31):
    os.system("python MST.py < graphs/infile%02d_%02d.txt" % (graph_size, x))

