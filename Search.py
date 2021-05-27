import sys
import copy
import numpy
import math
from collections import deque

from utils import *

""" CITATIONS
    All of the classes and functions in this file were taken and altered from the AIMA python repository except 
    for the class PrimGraph and all of the functions inside it which were taken from  
    https://www.geeksforgeeks.org/prims-minimum-spanning-tree-mst-greedy-algo-5/
    The functions random_edges(), cheapest_edges(), and prim_mst_heuristic() were not taken from anywhere and were all
    written by me and the people I collaborated with on the project
    """

class Problem:
    """The abstract class for a formal problem. You should subclass
    this and implement the methods actions and result, and possibly
    __init__, goal_test, and path_cost. Then you will create instances
    of your subclass and solve them with the various search functions."""

    def __init__(self, initial, goal=None):
        """The constructor specifies the initial state, and possibly a goal
        state, if there is a unique goal. Your subclass's constructor can add
        other arguments."""
        self.initial = initial
        self.goal = goal

    def actions(self, state):
        """Return the actions that can be executed in the given
        state. The result would typically be a list, but if there are
        many actions, consider yielding them one at a time in an
        iterator, rather than building them all at once."""
        raise NotImplementedError

    def result(self, state, action):
        """Return the state that results from executing the given
        action in the given state. The action must be one of
        self.actions(state)."""
        raise NotImplementedError

    def goal_test(self, state):
        """Return True if the state is a goal. The default method compares the
        state to self.goal or checks for state in self.goal if it is a
        list, as specified in the constructor. Override this method if
        checking against a single self.goal is not enough."""
        if(len(state) == self.goal + 1) and state[len(state) -1] == state[0]:
            return True
        else:
            return False


    def path_cost(self, c, state1, action, state2):
        """Return the cost of a solution path that arrives at state2 from
        state1 via action, assuming cost c to get up to state1. If the problem
        is such that the path doesn't matter, this function will only look at
        state2. If the path does matter, it will consider c and maybe state1
        and action. The default method costs 1 for every step in the path."""
        return c + 1

    def value(self, state):
        """For optimization problems, each state has a value. Hill Climbing
        and related algorithms try to maximize this value."""
        raise NotImplementedError


# ______________________________________________________________________________


class Node:
    """A node in a search tree. Contains a pointer to the parent (the node
    that this is a successor of) and to the actual state for this node. Note
    that if a state is arrived at by two paths, then there are two nodes with
    the same state. Also includes the action that got us to this state, and
    the total path_cost (also known as g) to reach the node. Other functions
    may add an f and h value; see best_first_graph_search and astar_search for
    an explanation of how the f and h values are handled. You will not need to
    subclass this class."""

    def __init__(self, state, parent=None, action=None, path_cost=0):
        """Create a search tree Node, derived from a parent by an action."""
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1

    def __repr__(self):
        return "<Node {}>".format(self.state)

    def __lt__(self, node):
        return self.state < node.state

    def expand(self, problem):
        """List the nodes reachable in one step from this node."""
        return [self.child_node(problem, action)
                for action in problem.actions(self.state)]

    def child_node(self, problem, action):
        """[Figure 3.10]"""
        next_state = problem.result(self.state, action)
        next_node = Node(next_state, self, action, problem.path_cost(self.path_cost, self.state, action, next_state))
        return next_node

    def solution(self):
        """Return the sequence of actions to go from the root to this node."""
        return [node.action for node in self.path()[1:]]

    def path(self):
        """Return a list of nodes forming the path from the root to this node."""
        node, path_back = self, []
        while node:
            path_back.append(node)
            node = node.parent
        return list(reversed(path_back))



    # We want for a queue of nodes in breadth_first_graph_search or
    # astar_search to have no duplicated states, so we treat nodes
    # with the same state as equal. [Problem: this may not be what you
    # want in other contexts.]

    def __eq__(self, other):
        return isinstance(other, Node) and self.state == other.state

    def __hash__(self):
        # We use the hash value of the state
        # stored in the node instead of the node
        # object itself to quickly search a node
        # with the same state in a Hash Table
        return hash(self.state)


class Graph:
    """A graph connects nodes (vertices) by edges (links). Each edge can also
    have a length associated with it. The constructor call is something like:
        g = Graph({'A': {'B': 1, 'C': 2})
    this makes a graph with 3 nodes, A, B, and C, with an edge of length 1 from
    A to B,  and an edge of length 2 from A to C. You can also do:
        g = Graph({'A': {'B': 1, 'C': 2}, directed=False)
    This makes an undirected graph, so inverse links are also added. The graph
    stays undirected; if you add more links with g.connect('B', 'C', 3), then
    inverse link is also added. You can use g.nodes() to get a list of nodes,
    g.get('A') to get a dict of links out of A, and g.get('A', 'B') to get the
    length of the link from A to B. 'Lengths' can actually be any object at
    all, and nodes can be any hashable object."""

    def __init__(self, graph_dict=None, directed=True):
        self.graph_dict = graph_dict or {}
        self.directed = directed
        if not directed:
            self.make_undirected()

    def make_undirected(self):
        """Make a digraph into an undirected graph by adding symmetric edges."""
        for a in list(self.graph_dict.keys()):
            for (b, dist) in self.graph_dict[a].items():
                self.connect1(b, a, dist)

    def connect(self, A, B, distance=1):
        """Add a link from A and B of given distance, and also add the inverse
        link if the graph is undirected."""
        self.connect1(A, B, distance)
        if not self.directed:
            self.connect1(B, A, distance)

    def connect1(self, A, B, distance):
        """Add a link from A to B of given distance, in one direction only."""
        self.graph_dict.setdefault(A, {})[B] = distance

    def get(self, a, b=None):
        """Return a link distance or a dict of {node: distance} entries.
        .get(a,b) returns the distance or None;
        .get(a) returns a dict of {node: distance} entries, possibly {}."""
        links = self.graph_dict.setdefault(a, {})
        if b is None:
            return links
        else:
            return links.get(b)

    def nodes(self):
        """Return a list of nodes in the graph."""
        s1 = set([k for k in self.graph_dict.keys()])
        s2 = set([k2 for v in self.graph_dict.values() for k2, v2 in v.items()])
        nodes = s1.union(s2)
        return list(nodes)


def UndirectedGraph(graph_dict=None):
    """Build a Graph where every edge (including future ones) goes both ways."""
    return Graph(graph_dict=graph_dict, directed=False)


#This class and the functions inside it were taken from https://www.geeksforgeeks.org/prims-minimum-spanning-tree-mst-greedy-algo-5/
class PrimGraph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    # A utility function to print the constructed MST stored in parent[]
    def printMST(self, parent):
        print
        "Edge \tWeight"
        for i in range(1, self.V):
            print
            parent[i], "-", i, "\t", self.graph[i][parent[i]]

    def add_cost(self,parent):
        cost = 0
        for i in range(1, self.V):
            cost = cost + self.graph[i][parent[i]]
        return cost

    # A utility function to find the vertex with
    # minimum distance value, from the set of vertices
    # not yet included in shortest path tree
    def minKey(self, key, mstSet):

        # Initilaize min value
        min = math.inf

        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v

        return min_index

    # Function to construct and print MST for a graph
    # represented using adjacency matrix representation
    def primMST(self):

        # Key values used to pick minimum weight edge in cut
        key = [math.inf] * self.V
        parent = [None] * self.V  # Array to store constructed MST
        # Make key 0 so that this vertex is picked as first vertex
        key[0] = 0
        mstSet = [False] * self.V

        parent[0] = -1  # First node is always the root of

        for cout in range(self.V):

            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # u is always equal to src in first iteration
            u = self.minKey(key, mstSet)

            # Put the minimum distance vertex in
            # the shortest path tree
            mstSet[u] = True

            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shotest path tree
            for v in range(self.V):

                # graph[u][v] is non zero only for adjacent vertices of m
                # mstSet[v] is false for vertices not yet included in MST
                # Update the key only if graph[u][v] is smaller than key[v]
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        return self.add_cost(parent)


class GraphProblem(Problem):
    """The problem of searching a graph from one node to another."""

    def __init__(self, initial, goal, graph, adjmatrix, nodes_expanded):
        super().__init__(initial, goal)
        self.graph = graph
        self.adjmatrix = adjmatrix
        self.expanded_nodes = nodes_expanded

    def nodes_expanded(self):
        return self.expanded_nodes

    def actions(self, A):
        """The actions at a graph node are just its neighbors."""
        final_list = []
        templist = list(self.graph.get(A[len(A) - 1]).keys())
        if len(A) == self.goal:
            b = list(A)
            b.append(self.initial)
            final_list.append(b)
        else:
            for i in templist:
                if i not in A:
                    b = list(A)
                    b.append(i)
                    final_list.append(b)
        return final_list

    def result(self, state, action):
        """The result of going to a neighbor is just that neighbor."""
        return action

    def path_cost(self, cost_so_far, A, action, B):
        length = len(B)
        return cost_so_far + self.graph.get(B[length-2], B[length-1])

    def find_min_edge(self):
        """Find minimum value of edges."""
        m = np.inf
        for d in self.graph.graph_dict.values():
            local_min = min(d.values())
            m = min(m, local_min)

        return m

    def h(self, node):
        """h function is straight-line distance from a node's state to goal."""
        locs = getattr(self.graph, 'locations', None)
        if locs:
            if type(node) is str:
                return int(distance(locs[node], locs[self.goal]))

            return int(distance(locs[node.state], locs[self.goal]))
        else:
            return np.inf

    def random_edges(self, A):
            cost = 0
            length = len(A.state)
            ints = []

            if length == self.goal:
                return self.graph.get(A.state[length-1], self.initial)

            if length != 1:
                for character in A.state:
                    ints.append(ord(character) - 65)

            for i in range(self.goal):
                if i not in ints:
                    index = random.randrange(0, self.goal)
                    while index not in ints and index != i:
                        index = random.randrange(0, self.goal)
                    cost = cost + self.adjmatrix[i][index]
            return cost


    def cheapest_edges(self, A):
        cost = 0
        length = len(A.state)
        ints = []
        if length != 1:
            for character in A.state:
                ints.append(ord(character) - 65)

        for i in range(self.goal):
            if i not in ints:
                templist = list(self.adjmatrix[i])
                templist.sort()
                cost = cost + templist[1]
        return cost

    def prim_mst_heuristic(self, A):
        cost = 0
        g = PrimGraph(self.goal - len(A.state))
        ints = []
        for character in A.state:
            ints.append(ord(character) - 65)

        adjmatrix = []
        if len(A.state) == self.goal:
            return self.graph.get(A.state[len(A.state) - 1], self.initial)
        if len(A.state) > self.goal:
            return 0

        for x in range(self.goal):
            templist = []
            if x not in ints:
                for y in range(self.goal):
                    if y not in ints:
                        templist.append(self.adjmatrix[x][y])
            if x not in ints:
                adjmatrix.append(templist)

        g.graph = adjmatrix
        cost = g.primMST()
        return cost


class TSP_problem(Problem):

    """ subclass of Problem to define various functions """
    def __init__(self, initial, dist):
        self.initial = initial
        self.distances = dist

    def two_opt(self, state):
        """ Neighbour generating function for Traveling Salesman Problem """
        neighbour_state = state[:]
        left = random.randint(0, len(neighbour_state) - 1)
        right = random.randint(0, len(neighbour_state) - 1)
        if left > right:
            left, right = right, left
        neighbour_state[left: right + 1] = reversed(neighbour_state[left: right + 1])
        return neighbour_state

    def actions(self, state):
        """ action that can be excuted in given state """
        return [self.two_opt]

    def result(self, state, action):
        """  result after applying the given action on the given state """
        return action(state)

    def path_cost(self, c, state1, action, state2):
        """ total distance for the Traveling Salesman to be covered if in state2  """
        cost = 0
        for i in range(len(state2) - 1):
            cost += self.distances[state2[i]][state2[i + 1]]
        cost += self.distances[state2[0]][state2[-1]]
        return cost

    def value(self, state):
        """ value of path cost given negative for the given state """
        return -1 * self.path_cost(None, None, None, state)



def hill_climbing(problem):
    """From the initial node, keep choosing the neighbor with highest value,
    stopping when no neighbor is better. [Figure 4.2]"""

    def find_neighbors(state, number_of_neighbors=10):
        """ finds neighbors using two_opt method """

        neighbors = []

        for i in range(number_of_neighbors):
            new_state = problem.two_opt(state)
            neighbors.append(Node(new_state))
            state = new_state

        return neighbors

    # as this is a stochastic algorithm, we will set a cap on the number of iterations
    iterations = 100000

    current = Node(problem.initial)
    while iterations:
        neighbors = find_neighbors(current.state)
        if not neighbors:
            break
        neighbor = argmax_random_tie(neighbors,
                                     key=lambda node: problem.value(node.state))
        #print(problem.value(neighbor.state))
        #print(problem.value(current.state))
        if problem.value(neighbor.state) >= problem.value(current.state):
            current.state = neighbor.state
        iterations -= 1

    return current.state


def exp_schedule(k=20, lam=0.005, limit=10000):
    """One possible schedule function for simulated annealing"""
    return lambda t: (k * math.exp(-lam * t) if t < limit else 0)

def simulated_annealing(problem, schedule=exp_schedule()):
    """[Figure 4.5] CAUTION: This differs from the pseudocode as it
    returns a state instead of a Node."""
    current = Node(problem.initial)
    for t in range(sys.maxsize):
        T = schedule(t)
        if T == 0:
            return current.state
        neighbors = current.expand(problem)
        if not neighbors:
            return current.state
        next_choice = random.choice(neighbors)
        delta_e = problem.value(next_choice.state) - problem.value(current.state)
        if delta_e > 0 or probability(math.exp(delta_e / T)):
            current = next_choice


def best_first_graph_search(problem, f, display=False):
    """Search the nodes with the lowest f scores first.
    You specify the function f(node) that you want to minimize; for example,
    if f is a heuristic estimate to the goal, then we have greedy best
    first search; if f is node.depth then we have breadth-first search.
    There is a subtlety: the line "f = memoize(f, 'f')" means that the f
    values will be cached on the nodes as they are computed. So after doing
    a best first search you can examine the f values of the path returned."""
    f = memoize(f, 'f')
    node = Node(problem.initial)
    frontier = PriorityQueue('min', f)
    frontier.append(node)
    explored = set()
    while frontier:
        node = frontier.pop()
        problem.expanded_nodes = problem.expanded_nodes + 1
        if problem.goal_test(node.state):
            if display:
                print(len(explored), "paths have been expanded and", len(frontier), "paths remain in the frontier")
            return node
        explored.add(tuple(node.state))
        for child in node.expand(problem):
            if tuple(child.state) not in explored and child not in frontier:
                frontier.append(child)
            elif child in frontier:
                if f(child) < frontier[child]:
                    del frontier[child]
                    frontier.append(child)
    return None


def uniform_cost_search(problem, display=False):
    """[Figure 3.14]"""
    return best_first_graph_search(problem, lambda node: node.path_cost, display)

def astar_search(problem, h=None, display=False):
    """A* search is best-first graph search with f(n) = g(n)+h(n).
    You need to specify the h function when you call astar_search, or
    else in your Problem subclass."""
    h = memoize(h or problem.h, 'h')
    return best_first_graph_search(problem, lambda n: n.path_cost + h(n), display)

    """[Figure 4.8]"""
    for i in range(ngen):
        population = [mutate(recombine(*select(2, population, fitness_fn)), gene_pool, pmut)
                      for i in range(len(population))]

        fittest_individual = fitness_threshold(fitness_fn, f_thres, population)
        if fittest_individual:
            return fittest_individual

    return argmax(population, key=fitness_fn)


class GeneticAlgorithm:

    def __init__(self, numberOfVertices, adjmatrix, numbers_to_letters_dict):
        self.numberOfVertices = numberOfVertices
        self.adjmatrix = adjmatrix
        self.dict_numbers_to_letters = numbers_to_letters_dict

    def calc_cost(self, path):
        cost = 0
        for i in range(len(path) - 1):
            cost += self.adjmatrix[path[i]][path[i + 1]]
        return cost

    def fitness_fn(self, population):
        path_ints = []
        for x in range(len(population)):
            if population[x] == "AA":
                path_ints.append(26)
            elif population[x] == "BB":
                path_ints.append(27)
            elif population[x] == "CC":
                path_ints.append(28)
            elif population[x] == "DD":
                path_ints.append(29)
            elif population[x] == "EE":
                path_ints.append(30)
            else:
                path_ints.append(ord(population[x]) - 65)
        return 31000 - (self.calc_cost(path_ints))


    def init_population(self, pop_number, state_length):
        """Initializes population for genetic algorithm
        pop_number  :  Number of individuals in population
        gene_pool   :  List of possible values for individuals
        state_length:  The length of each individual"""
        g = state_length
        population = []
        original_lst = []

        for i in range(self.numberOfVertices):
            if i == 26:
                original_lst.append("AA")
            elif i == 27:
                original_lst.append("BB")
            elif i == 28:
                original_lst.append("CC")
            elif i == 29:
                original_lst.append("DD")
            elif i == 30:
                original_lst.append("EE")
            else:
                original_lst.append(chr(i + 65))

        for n in range(pop_number):
            random.shuffle(original_lst)
            population.append(original_lst.copy())


        return population

    def fitness_threshold(self, fitness_fn, f_thres, population):
        if not f_thres:
            return None

        fittest_individual = max(population, key=self.fitness_fn)
        if self.fitness_fn(fittest_individual) >= f_thres:
            return fittest_individual

        return None


    def select(self, r, population, fitness_fn):
        fitnesses = map(self.fitness_fn, population)
        sampler = weighted_sampler(population, fitnesses)
        return [sampler() for i in range(r)]


    def recombine(self, x, y):
        n = len(x)
        c = random.randrange(0, n)
        return x[:c] + y[c:]


    def recombine_uniform(self, x, y):
        n = len(x)
        result = [0] * n
        indexes = random.sample(range(n), n)
        for i in range(n):
            ix = indexes[i]
            result[ix] = x[ix] if i < n / 2 else y[ix]

        return ''.join(str(r) for r in result)

    def recombine_ordered(self, x, y):
        n = len(x)
        first = random.randrange(0, n-2)
        second = random.randrange(first, n)
        temp = []
        child = []
        best = x
        worst = y
        if(self.fitness_fn(y) > self.fitness_fn(x)):
            best = y
            worst = x
        lst = best[first:second]

        for i in lst:
            worst.remove(i)

        worst[second:second] = lst

        if self.fitness_fn(worst) < self.fitness_fn(best):
            return best
        else:
            return worst



    def mutate(self, x, gene_pool, pmut):
        if random.uniform(0, 1) >= pmut:
            return x

        n = len(x)
        g = len(gene_pool)
        c = random.randrange(0, n)
        r = random.randrange(c, n)

        first_gene = x[c]
        second_gene = x[r]
        templist = []
        for i in range(len(x)):
            if i == c:
                templist.append(second_gene)
            elif i == r:
                templist.append(first_gene)
            else:
                templist.append(x[i])
        return templist


    def genetic_algorithm(self, population, fitness_fn, gene_pool, f_thres=None, ngen=500, pmut=0.02):
        """[Figure 4.8]"""
        for i in range(ngen):
            population = [self.mutate(self.recombine_ordered(*self.select(2, population, fitness_fn)), gene_pool, pmut)
                          for i in range(len(population))]
            fittest_individual = self.fitness_threshold(fitness_fn, f_thres, population)
            if fittest_individual:
                return fittest_individual

        return max(population, key=self.fitness_fn)