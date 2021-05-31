import sys
import Search
import random
import time
import timeit
import csv

line = sys.stdin.readlines()

lines = []

for x in range(0, len(line)):
    lines.append(list(map(float, line[x].split(","))))

size5 = []
size6 = []
size7 = []
size8 = []
size9 = []
size10 = []
for x in range(len(lines)):
    if lines[x][0] == 5:
        size5.append(lines[x])
    elif lines[x][0] == 6:
        size6.append(lines[x])
    elif lines[x][0] == 7:
        size7.append(lines[x])
    elif lines[x][0] == 8:
        size8.append(lines[x])
    elif lines[x][0] == 9:
        size9.append(lines[x])
    elif lines[x][0] == 10:
        size10.append(lines[x])

size5_costs = []
size6_costs = []
size7_costs = []
size8_costs = []
size9_costs = []
size10_costs = []

size5_expanded = []
size6_expanded = []
size7_expanded = []
size8_expanded = []
size9_expanded = []
size10_expanded = []

size5_wall_time = []
size6_wall_time = []
size7_wall_time = []
size8_wall_time = []
size9_wall_time = []
size10_wall_time = []

size5_cpu_time = []
size6_cpu_time = []
size7_cpu_time = []
size8_cpu_time = []
size9_cpu_time = []
size10_cpu_time = []

for x in range(30):
    size5_costs.append(size5[x][1])
    size5_expanded.append(size5[x][2])
    size5_wall_time.append(size5[x][3])
    size5_cpu_time.append(size5[x][4])

    size6_costs.append(size6[x][1])
    size6_expanded.append(size6[x][2])
    size6_wall_time.append(size6[x][3])
    size6_cpu_time.append(size6[x][4])

    size7_costs.append(size7[x][1])
    size7_expanded.append(size7[x][2])
    size7_wall_time.append(size7[x][3])
    size7_cpu_time.append(size7[x][4])

    size8_costs.append(size8[x][1])
    size8_expanded.append(size8[x][2])
    size8_wall_time.append(size8[x][3])
    size8_cpu_time.append(size8[x][4])

    size9_costs.append(size9[x][1])
    size9_expanded.append(size9[x][2])
    size9_wall_time.append(size9[x][3])
    size9_cpu_time.append(size9[x][4])

    size10_costs.append(size10[x][1])
    size10_expanded.append(size10[x][2])
    size10_wall_time.append(size10[x][3])
    size10_cpu_time.append(size10[x][4])

size5_cost_min = size5_costs[0]
size5_cost_max = size5_costs[0]
size5_cost_avg = 0
size5_expanded_min = size5_expanded[0]
size5_expanded_max = size5_expanded[0]
size5_expanded_avg = 0
size5_walltime_min = size5_wall_time[0]
size5_walltime_max = size5_wall_time[0]
size5_walltime_avg = 0
size5_cputime_min = size5_cpu_time[0]
size5_cputime_max = size5_cpu_time[0]
size5_cputime_avg = 0

size6_cost_min = size6_costs[0]
size6_cost_max = size6_costs[0]
size6_cost_avg = 0
size6_expanded_min = size6_expanded[0]
size6_expanded_max = size6_expanded[0]
size6_expanded_avg = 0
size6_walltime_min = size6_wall_time[0]
size6_walltime_max = size6_wall_time[0]
size6_walltime_avg = 0
size6_cputime_min = size6_cpu_time[0]
size6_cputime_max = size6_cpu_time[0]
size6_cputime_avg = 0

size7_cost_min = size7_costs[0]
size7_cost_max = size7_costs[0]
size7_cost_avg = 0
size7_expanded_min = size7_expanded[0]
size7_expanded_max = size7_expanded[0]
size7_expanded_avg = 0
size7_walltime_min = size7_wall_time[0]
size7_walltime_max = size7_wall_time[0]
size7_walltime_avg = 0
size7_cputime_min = size7_cpu_time[0]
size7_cputime_max = size7_cpu_time[0]
size7_cputime_avg = 0

size8_cost_min = size8_costs[0]
size8_cost_max = size8_costs[0]
size8_cost_avg = 0
size8_expanded_min = size8_expanded[0]
size8_expanded_max = size8_expanded[0]
size8_expanded_avg = 0
size8_walltime_min = size8_wall_time[0]
size8_walltime_max = size8_wall_time[0]
size8_walltime_avg = 0
size8_cputime_min = size8_cpu_time[0]
size8_cputime_max = size8_cpu_time[0]
size8_cputime_avg = 0

size9_cost_min = size9_costs[0]
size9_cost_max = size9_costs[0]
size9_cost_avg = 0
size9_expanded_min = size9_expanded[0]
size9_expanded_max = size9_expanded[0]
size9_expanded_avg = 0
size9_walltime_min = size9_wall_time[0]
size9_walltime_max = size9_wall_time[0]
size9_walltime_avg = 0
size9_cputime_min = size9_cpu_time[0]
size9_cputime_max = size9_cpu_time[0]
size9_cputime_avg = 0

size10_cost_min = size10_costs[0]
size10_cost_max = size10_costs[0]
size10_cost_avg = 0
size10_expanded_min = size10_expanded[0]
size10_expanded_max = size10_expanded[0]
size10_expanded_avg = 0
size10_walltime_min = size10_wall_time[0]
size10_walltime_max = size10_wall_time[0]
size10_walltime_avg = 0
size10_cputime_min = size10_cpu_time[0]
size10_cputime_max = size10_cpu_time[0]
size10_cputime_avg = 0

for x in range(0,30):
    size5_cost_avg += size5_costs[x]
    size5_expanded_avg += size5_expanded[x]
    size5_walltime_avg += size5_wall_time[x]
    size5_cputime_avg += size5_cpu_time[x]

    size6_cost_avg += size6_costs[x]
    size6_expanded_avg += size6_expanded[x]
    size6_walltime_avg += size6_wall_time[x]
    size6_cputime_avg += size6_cpu_time[x]

    size7_cost_avg += size7_costs[x]
    size7_expanded_avg += size7_expanded[x]
    size7_walltime_avg += size7_wall_time[x]
    size7_cputime_avg += size7_cpu_time[x]

    size8_cost_avg += size8_costs[x]
    size8_expanded_avg += size8_expanded[x]
    size8_walltime_avg += size8_wall_time[x]
    size8_cputime_avg += size8_cpu_time[x]

    size9_cost_avg += size9_costs[x]
    size9_expanded_avg += size9_expanded[x]
    size9_walltime_avg += size9_wall_time[x]
    size9_cputime_avg += size9_cpu_time[x]

    size10_cost_avg += size10_costs[x]
    size10_expanded_avg += size10_expanded[x]
    size10_walltime_avg += size10_wall_time[x]
    size10_cputime_avg += size10_cpu_time[x]

    if size5_costs[x] < size5_cost_min:
        size5_cost_min = size5_costs[x]
    if size5_costs[x] > size5_cost_max:
        size5_cost_max = size5_costs[x]
    if size5_expanded[x] < size5_expanded_min:
        size5_expanded_min = size5_expanded[x]
    if size5_expanded[x] > size5_expanded_max:
        size5_expanded_max = size5_expanded[x]
    if size5_wall_time[x] < size5_walltime_min:
        size5_walltime_min = size5_wall_time[x]
    if size5_wall_time[x] > size5_walltime_max:
        size5_walltime_max = size5_wall_time[x]
    if size5_cpu_time[x] < size5_cputime_min:
        size5_cputime_min = size5_cpu_time[x]
    if size5_cpu_time[x] > size5_cputime_max:
        size5_cputime_max = size5_cpu_time[x]

    if size6_costs[x] < size6_cost_min:
        size6_cost_min = size6_costs[x]
    if size6_costs[x] > size6_cost_max:
        size6_cost_max = size6_costs[x]
    if size6_expanded[x] < size6_expanded_min:
        size6_expanded_min = size6_expanded[x]
    if size6_expanded[x] > size6_expanded_max:
        size6_expanded_max = size6_expanded[x]
    if size6_wall_time[x] < size6_walltime_min:
        size6_walltime_min = size6_wall_time[x]
    if size6_wall_time[x] > size6_walltime_max:
        size6_walltime_max = size6_wall_time[x]
    if size6_cpu_time[x] < size6_cputime_min:
        size6_cputime_min = size6_cpu_time[x]
    if size6_cpu_time[x] > size6_cputime_max:
        size6_cputime_max = size6_cpu_time[x]

    if size7_costs[x] < size7_cost_min:
        size7_cost_min = size7_costs[x]
    if size7_costs[x] > size7_cost_max:
        size7_cost_max = size7_costs[x]
    if size7_expanded[x] < size7_expanded_min:
        size7_expanded_min = size7_expanded[x]
    if size7_expanded[x] > size7_expanded_max:
        size7_expanded_max = size7_expanded[x]
    if size7_wall_time[x] < size7_walltime_min:
        size7_walltime_min = size7_wall_time[x]
    if size7_wall_time[x] > size7_walltime_max:
        size7_walltime_max = size7_wall_time[x]
    if size7_cpu_time[x] < size7_cputime_min:
        size7_cputime_min = size7_cpu_time[x]
    if size7_cpu_time[x] > size7_cputime_max:
        size7_cputime_max = size7_cpu_time[x]

    if size8_costs[x] < size8_cost_min:
        size8_cost_min = size8_costs[x]
    if size8_costs[x] > size8_cost_max:
        size8_cost_max = size8_costs[x]
    if size8_expanded[x] < size8_expanded_min:
        size8_expanded_min = size8_expanded[x]
    if size8_expanded[x] > size8_expanded_max:
        size8_expanded_max = size8_expanded[x]
    if size8_wall_time[x] < size8_walltime_min:
        size8_walltime_min = size8_wall_time[x]
    if size8_wall_time[x] > size8_walltime_max:
        size8_walltime_max = size8_wall_time[x]
    if size8_cpu_time[x] < size8_cputime_min:
        size8_cputime_min = size8_cpu_time[x]
    if size8_cpu_time[x] > size8_cputime_max:
        size8_cputime_max = size8_cpu_time[x]

    if size9_costs[x] < size9_cost_min:
        size9_cost_min = size9_costs[x]
    if size9_costs[x] > size9_cost_max:
        size9_cost_max = size9_costs[x]
    if size9_expanded[x] < size9_expanded_min:
        size9_expanded_min = size9_expanded[x]
    if size9_expanded[x] > size9_expanded_max:
        size9_expanded_max = size9_expanded[x]
    if size9_wall_time[x] < size9_walltime_min:
        size9_walltime_min = size9_wall_time[x]
    if size9_wall_time[x] > size9_walltime_max:
        size9_walltime_max = size9_wall_time[x]
    if size9_cpu_time[x] < size9_cputime_min:
        size9_cputime_min = size9_cpu_time[x]
    if size9_cpu_time[x] > size9_cputime_max:
        size9_cputime_max = size9_cpu_time[x]

    if size10_costs[x] < size10_cost_min:
        size10_cost_min = size10_costs[x]
    if size10_costs[x] > size10_cost_max:
        size10_cost_max = size10_costs[x]
    if size10_expanded[x] < size10_expanded_min:
        size10_expanded_min = size10_expanded[x]
    if size10_expanded[x] > size10_expanded_max:
        size10_expanded_max = size10_expanded[x]
    if size10_wall_time[x] < size10_walltime_min:
        size10_walltime_min = size10_wall_time[x]
    if size10_wall_time[x] > size10_walltime_max:
        size10_walltime_max = size10_wall_time[x]
    if size10_cpu_time[x] < size10_cputime_min:
        size10_cputime_min = size10_cpu_time[x]
    if size10_cpu_time[x] > size10_cputime_max:
        size10_cputime_max = size10_cpu_time[x]

size5_cost_avg = size5_cost_avg / 30
size5_expanded_avg = size5_expanded_avg / 30
size5_walltime_avg = size5_walltime_avg / 30
size5_cputime_avg = size5_cputime_avg / 30

size6_cost_avg = size6_cost_avg / 30
size6_expanded_avg = size6_expanded_avg / 30
size6_walltime_avg = size6_walltime_avg / 30
size6_cputime_avg = size6_cputime_avg / 30

size7_cost_avg = size7_cost_avg / 30
size7_expanded_avg = size7_expanded_avg / 30
size7_walltime_avg = size7_walltime_avg / 30
size7_cputime_avg = size7_cputime_avg / 30

size8_cost_avg = size8_cost_avg / 30
size8_expanded_avg = size8_expanded_avg / 30
size8_walltime_avg = size8_walltime_avg / 30
size8_cputime_avg = size8_cputime_avg / 30

size9_cost_avg = size9_cost_avg / 30
size9_expanded_avg = size9_expanded_avg / 30
size9_walltime_avg = size9_walltime_avg / 30
size9_cputime_avg = size9_cputime_avg / 30

size10_cost_avg = size10_cost_avg / 30
size10_expanded_avg = size10_expanded_avg / 30
size10_walltime_avg = size10_walltime_avg / 30
size10_cputime_avg = size10_cputime_avg / 30

fo_new = open("stats_files/MST_Stats.txt", "w+")
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

fo_new.write(str("size10 cost min:  %f" % (size10_cost_min) + "\n"))
fo_new.write(str("size10 cost max:  %f" % (size10_cost_max) + "\n"))
fo_new.write(str("size10 cost avg:  %f" % (size10_cost_avg) + "\n"))
fo_new.write(str("size10 nodes expanded min:  %f" % (size10_expanded_min) + "\n"))
fo_new.write(str("size10 nodes expanded max:  %f" % (size10_expanded_max) + "\n"))
fo_new.write(str("size10 nodes expanded avg:  %f" % (size10_expanded_avg) + "\n"))
fo_new.write(str("size10 wall time min:  %f" % (size10_walltime_min) + "\n"))
fo_new.write(str("size10 wall time max:  %f" % (size10_walltime_max) + "\n"))
fo_new.write(str("size10 wall time avg:  %f" % (size10_walltime_avg) + "\n"))
fo_new.write(str("size10 cpu time min:  %f" % (size10_cputime_min) + "\n"))
fo_new.write(str("size10 cpu time max:  %f" % (size10_cputime_max) + "\n"))
fo_new.write(str("size10 cpu time avg:  %f" % (size10_cputime_avg) + "\n"))

