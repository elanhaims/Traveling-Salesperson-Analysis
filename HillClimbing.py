import sys
import Search
import random

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

distances = {}
all_cities = []

for city in graph_dict.keys():
    all_cities.append(city)

tsp = Search.TSP_problem(all_cities, graph_dict)
print(Search.hill_climbing(tsp))