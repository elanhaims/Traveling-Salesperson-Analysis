import regli_assignment_ggen
for x in range(30):
    graph = regli_assignment_ggen.create_complete_symmetric_graphs(6)
    regli_assignment_ggen.create_final_output(graph, 6, x)

