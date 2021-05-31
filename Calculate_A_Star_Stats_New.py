import sys
import Search
import random
import time
import timeit
import csv
import pandas as pd


def calculate_stats():
    ucs_graph_data = pd.read_csv("csv_files/ucs.csv",
                                 names=["graph_size", "cost", "nodes_expanded", "wall_time", "cpu_time"])

    random_edge_graph_data = pd.read_csv("csv_files/random_edges.csv",
                                         names=["graph_size", "cost", "nodes_expanded", "wall_time", "cpu_time"])

    cheapest_edge_graph_data = pd.read_csv("csv_files/cheapest_edges.csv",
                                           names=["graph_size", "cost", "nodes_expanded", "wall_time", "cpu_time"])

    mst_graph_data = pd.read_csv("csv_files/mst.csv",
                                 names=["graph_size", "cost", "nodes_expanded", "wall_time", "cpu_time"])

    ucs_tag = ["ucs"] * len(ucs_graph_data.index)
    random_edge_tag = ["random_edge"] * len(random_edge_graph_data.index)
    cheapest_edge_tag = ["cheapest_edge"] * len(cheapest_edge_graph_data.index)
    mst_tag = ["mst"] * len(mst_graph_data.index)

    ucs_graph_data["heuristic"] = ucs_tag
    random_edge_graph_data["heuristic"] = random_edge_tag
    cheapest_edge_graph_data["heuristic"] = cheapest_edge_tag
    mst_graph_data["heuristic"] = mst_tag

    frames = [ucs_graph_data, random_edge_graph_data, cheapest_edge_graph_data, mst_graph_data]
    graph_data = pd.concat(frames)

    grouped_by_heur = graph_data.groupby(["heuristic", "graph_size"])
    graph_data_min_values = grouped_by_heur.min().reset_index()

    graph_data_min_values.columns = ["heuristic", "graph_size", "min_cost", "min_nodes_expanded", "min_wall_time",
                                     "min_cpu_time"]
    graph_data_min_values = graph_data_min_values.reset_index(drop=True)

    graph_data_max_values = grouped_by_heur.max().reset_index()
    graph_data_max_values.columns = ["heuristic", "graph_size", "max_cost", "max_nodes_expanded", "max_wall_time",
                                     "max_cpu_time"]
    graph_data_max_values = graph_data_max_values.drop(columns=["heuristic", "graph_size"]).reset_index(drop=True)

    graph_stats = pd.concat([graph_data_min_values, graph_data_max_values], axis=1)

    graph_data_avg_values = grouped_by_heur.mean().reset_index()
    graph_data_avg_values.columns = ["heuristic", "graph_size", "avg_cost", "avg_nodes_expanded", "avg_wall_time",
                                     "avg_cpu_time"]
    graph_data_avg_values = graph_data_avg_values.drop(columns=["heuristic", "graph_size"]).reset_index(drop=True)

    graph_stats = pd.concat([graph_data_min_values, graph_data_max_values, graph_data_avg_values], axis=1)
    print(graph_stats)

    grouped_stats = [pd.DataFrame(y) for x, y in graph_stats.groupby('heuristic', as_index=False)]
    #print(grouped_stats[0].columns)

    """
    fo_new = open("stats_files/Random_edges_Stats.txt", "w+")
    fo_new.write(str("size5 cost min:  %f" % (size5_cost_min) + "\n"))
    fo_new.write(str("size5 cost max:  %f" % (size5_cost_max) + "\n"))
    fo_new.write(str("size5 cost avg:  %f" % (size5_cost_avg) + "\n"))
    fo_new.write(str("size5 nodes expanded min:  %f" % (size5_expanded_min) + "\n"))
    fo_new.write(str("size5 nodes expanded max:  %f" % (size5_expanded_max) + "\n"))
    fo_new.write(str("size5 nodes expanded avg:  %f" % (size5_expanded_avg) + "\n"))
    fo_new.write(str("size5 wall time min:  %f" % (size5_walltime_min) + "\n"))
    fo_new.write(str("size5 wall time max:  %f" % (size5_walltime_max) + "\n"))
    fo_new.write(str("size5 wall time avg:  %f" % (size5_walltime_avg) + "\n"))
    fo_new.write(str("size5 cpu time min:  %f" % (size5_cputime_min) + "\n"))
    fo_new.write(str("size5 cpu time max:  %f" % (size5_cputime_max) + "\n"))
    fo_new.write(str("size5 cpu time avg:  %f" % (size5_cputime_avg) + "\n"))
    
    fo_new.write(str("size6 cost min:  %f" % (size6_cost_min) + "\n"))
    fo_new.write(str("size6 cost max:  %f" % (size6_cost_max) + "\n"))
    fo_new.write(str("size6 cost avg:  %f" % (size6_cost_avg) + "\n"))
    fo_new.write(str("size6 nodes expanded min:  %f" % (size6_expanded_min) + "\n"))
    fo_new.write(str("size6 nodes expanded max:  %f" % (size6_expanded_max) + "\n"))
    fo_new.write(str("size6 nodes expanded avg:  %f" % (size6_expanded_avg) + "\n"))
    fo_new.write(str("size6 wall time min:  %f" % (size6_walltime_min) + "\n"))
    fo_new.write(str("size6 wall time max:  %f" % (size6_walltime_max) + "\n"))
    fo_new.write(str("size6 wall time avg:  %f" % (size6_walltime_avg) + "\n"))
    fo_new.write(str("size6 cpu time min:  %f" % (size6_cputime_min) + "\n"))
    fo_new.write(str("size6 cpu time max:  %f" % (size6_cputime_max) + "\n"))
    fo_new.write(str("size6 cpu time avg:  %f" % (size6_cputime_avg) + "\n"))
    
    fo_new.write(str("size7 cost min:  %f" % (size7_cost_min) + "\n"))
    fo_new.write(str("size7 cost max:  %f" % (size7_cost_max) + "\n"))
    fo_new.write(str("size7 cost avg:  %f" % (size7_cost_avg) + "\n"))
    fo_new.write(str("size7 nodes expanded min:  %f" % (size7_expanded_min) + "\n"))
    fo_new.write(str("size7 nodes expanded max:  %f" % (size7_expanded_max) + "\n"))
    fo_new.write(str("size7 nodes expanded avg:  %f" % (size7_expanded_avg) + "\n"))
    fo_new.write(str("size7 wall time min:  %f" % (size7_walltime_min) + "\n"))
    fo_new.write(str("size7 wall time max:  %f" % (size7_walltime_max) + "\n"))
    fo_new.write(str("size7 wall time avg:  %f" % (size7_walltime_avg) + "\n"))
    fo_new.write(str("size7 cpu time min:  %f" % (size7_cputime_min) + "\n"))
    fo_new.write(str("size7 cpu time max:  %f" % (size7_cputime_max) + "\n"))
    fo_new.write(str("size7 cpu time avg:  %f" % (size7_cputime_avg) + "\n"))
    
    fo_new.write(str("size8 cost min:  %f" % (size8_cost_min) + "\n"))
    fo_new.write(str("size8 cost max:  %f" % (size8_cost_max) + "\n"))
    fo_new.write(str("size8 cost avg:  %f" % (size8_cost_avg) + "\n"))
    fo_new.write(str("size8 nodes expanded min:  %f" % (size8_expanded_min) + "\n"))
    fo_new.write(str("size8 nodes expanded max:  %f" % (size8_expanded_max) + "\n"))
    fo_new.write(str("size8 nodes expanded avg:  %f" % (size8_expanded_avg) + "\n"))
    fo_new.write(str("size8 wall time min:  %f" % (size8_walltime_min) + "\n"))
    fo_new.write(str("size8 wall time max:  %f" % (size8_walltime_max) + "\n"))
    fo_new.write(str("size8 wall time avg:  %f" % (size8_walltime_avg) + "\n"))
    fo_new.write(str("size8 cpu time min:  %f" % (size8_cputime_min) + "\n"))
    fo_new.write(str("size8 cpu time max:  %f" % (size8_cputime_max) + "\n"))
    fo_new.write(str("size8 cpu time avg:  %f" % (size8_cputime_avg) + "\n"))
    
    fo_new.write(str("size9 cost min:  %f" % (size9_cost_min) + "\n"))
    fo_new.write(str("size9 cost max:  %f" % (size9_cost_max) + "\n"))
    fo_new.write(str("size9 cost avg:  %f" % (size9_cost_avg) + "\n"))
    fo_new.write(str("size9 nodes expanded min:  %f" % (size9_expanded_min) + "\n"))
    fo_new.write(str("size9 nodes expanded max:  %f" % (size9_expanded_max) + "\n"))
    fo_new.write(str("size9 nodes expanded avg:  %f" % (size9_expanded_avg) + "\n"))
    fo_new.write(str("size9 wall time min:  %f" % (size9_walltime_min) + "\n"))
    fo_new.write(str("size9 wall time max:  %f" % (size9_walltime_max) + "\n"))
    fo_new.write(str("size9 wall time avg:  %f" % (size9_walltime_avg) + "\n"))
    fo_new.write(str("size9 cpu time min:  %f" % (size9_cputime_min) + "\n"))
    fo_new.write(str("size9 cpu time max:  %f" % (size9_cputime_max) + "\n"))
    fo_new.write(str("size9 cpu time avg:  %f" % (size9_cputime_avg) + "\n"))
    """
if __name__ == "__main__":
    calculate_stats()