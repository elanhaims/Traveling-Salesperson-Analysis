import sys
import Search
import random
import time
import timeit
import csv

line = sys.stdin.readlines()
numberOfVertices = int(line[0])

dict_numbers_to_letters = {}
for x in range(26):
    dict_numbers_to_letters[x] = chr(x + 65)
dict_numbers_to_letters[26] = 'AA'
dict_numbers_to_letters[27] = 'BB'
dict_numbers_to_letters[28] = 'CC'
dict_numbers_to_letters[29] = 'DD'



adjMatrix = []

for x in range(1, numberOfVertices + 1):
    adjMatrix.append(list(map(int, line[x].split(", "))))

graph_dict = {}

for i in range(len(adjMatrix)):
    tempDict = {}
    for j in range(len(adjMatrix[i])):
        if adjMatrix[i][j] != 0:
            tempDict[dict_numbers_to_letters[j]] = adjMatrix[i][j]
    graph_dict[dict_numbers_to_letters[i]] = tempDict


problem_graph = Search.UndirectedGraph(graph_dict)

mst_prob = Search.GraphProblem('A', numberOfVertices, problem_graph, adjMatrix, 0)



mst_heuristic = mst_prob.prim_mst_heuristic



def calc_cost(soln, graph):
    cost = 0
    for i in range(len(soln)-1):
        cost += graph.get(soln[i],soln[i+1])
    return cost

if __name__ == '__main__':
    size = numberOfVertices
    mst_filename = "mst.csv"

    fields = ['Size', 'Cost', 'Nodes Expanded', 'Real Time', 'CPU Time']

    mst_stats = []



    start_time = time.time()
    start_process_time = time.process_time()
    mst_solution = Search.astar_search(mst_prob, mst_heuristic).solution()[size - 1]
    mst_nodes_expanded = mst_prob.nodes_expanded()
    elapsed_process_time = time.process_time() - start_process_time
    elapsed_time = time.time() - start_time

    mst_stats.append([size, calc_cost(mst_solution, problem_graph), mst_nodes_expanded, elapsed_time, elapsed_process_time])



    with open(mst_filename, 'a') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(mst_stats)





