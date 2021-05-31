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
size10 = []
size15 = []
size20 = []
size25 = []
size30 = []
for x in range(len(lines)):
    if lines[x][0] == 5:
        size5.append(lines[x])
    elif lines[x][0] == 10:
        size10.append(lines[x])
    elif lines[x][0] == 15:
        size15.append(lines[x])
    elif lines[x][0] == 20:
        size20.append(lines[x])
    elif lines[x][0] == 25:
        size25.append(lines[x])
    elif lines[x][0] == 30:
        size30.append(lines[x])

size5_costs = []
size10_costs = []
size15_costs = []
size20_costs = []
size25_costs = []
size30_costs = []

size5_wall_time = []
size10_wall_time = []
size15_wall_time = []
size20_wall_time = []
size25_wall_time = []
size30_wall_time = []

size5_cpu_time = []
size10_cpu_time = []
size15_cpu_time = []
size20_cpu_time = []
size25_cpu_time = []
size30_cpu_time = []

for x in range(30):
    size5_costs.append(size5[x][1])
    size5_wall_time.append(size5[x][2])
    size5_cpu_time.append(size5[x][3])

    size10_costs.append(size10[x][1])
    size10_wall_time.append(size10[x][2])
    size10_cpu_time.append(size10[x][3])

    size15_costs.append(size15[x][1])
    size15_wall_time.append(size15[x][2])
    size15_cpu_time.append(size15[x][3])

    size20_costs.append(size20[x][1])
    size20_wall_time.append(size20[x][2])
    size20_cpu_time.append(size20[x][3])

    size25_costs.append(size25[x][1])
    size25_wall_time.append(size25[x][2])
    size25_cpu_time.append(size25[x][3])

    size30_costs.append(size30[x][1])
    size30_wall_time.append(size30[x][2])
    size30_cpu_time.append(size30[x][3])

size5_cost_min = size5_costs[0]
size5_cost_max = size5_costs[0]
size5_cost_avg = 0
size5_walltime_min = size5_wall_time[0]
size5_walltime_max = size5_wall_time[0]
size5_walltime_avg = 0
size5_cputime_min = size5_cpu_time[0]
size5_cputime_max = size5_cpu_time[0]
size5_cputime_avg = 0

size10_cost_min = size10_costs[0]
size10_cost_max = size10_costs[0]
size10_cost_avg = 0
size10_walltime_min = size10_wall_time[0]
size10_walltime_max = size10_wall_time[0]
size10_walltime_avg = 0
size10_cputime_min = size10_cpu_time[0]
size10_cputime_max = size10_cpu_time[0]
size10_cputime_avg = 0

size15_cost_min = size15_costs[0]
size15_cost_max = size15_costs[0]
size15_cost_avg = 0
size15_walltime_min = size15_wall_time[0]
size15_walltime_max = size15_wall_time[0]
size15_walltime_avg = 0
size15_cputime_min = size15_cpu_time[0]
size15_cputime_max = size15_cpu_time[0]
size15_cputime_avg = 0

size20_cost_min = size20_costs[0]
size20_cost_max = size20_costs[0]
size20_cost_avg = 0
size20_walltime_min = size20_wall_time[0]
size20_walltime_max = size20_wall_time[0]
size20_walltime_avg = 0
size20_cputime_min = size20_cpu_time[0]
size20_cputime_max = size20_cpu_time[0]
size20_cputime_avg = 0

size25_cost_min = size25_costs[0]
size25_cost_max = size25_costs[0]
size25_cost_avg = 0
size25_walltime_min = size25_wall_time[0]
size25_walltime_max = size25_wall_time[0]
size25_walltime_avg = 0
size25_cputime_min = size25_cpu_time[0]
size25_cputime_max = size25_cpu_time[0]
size25_cputime_avg = 0

size30_cost_min = size30_costs[0]
size30_cost_max = size30_costs[0]
size30_cost_avg = 0
size30_walltime_min = size30_wall_time[0]
size30_walltime_max = size30_wall_time[0]
size30_walltime_avg = 0
size30_cputime_min = size30_cpu_time[0]
size30_cputime_max = size30_cpu_time[0]
size30_cputime_avg = 0

for x in range(0,30):
    size5_cost_avg += size5_costs[x]
    size5_walltime_avg += size5_wall_time[x]
    size5_cputime_avg += size5_cpu_time[x]

    size10_cost_avg += size10_costs[x]
    size10_walltime_avg += size10_wall_time[x]
    size10_cputime_avg += size10_cpu_time[x]

    size15_cost_avg += size15_costs[x]
    size15_walltime_avg += size15_wall_time[x]
    size15_cputime_avg += size15_cpu_time[x]

    size20_cost_avg += size20_costs[x]
    size20_walltime_avg += size20_wall_time[x]
    size20_cputime_avg += size20_cpu_time[x]

    size25_cost_avg += size25_costs[x]
    size25_walltime_avg += size25_wall_time[x]
    size25_cputime_avg += size25_cpu_time[x]

    size30_cost_avg += size30_costs[x]
    size30_walltime_avg += size30_wall_time[x]
    size30_cputime_avg += size30_cpu_time[x]

    if size5_costs[x] < size5_cost_min:
        size5_cost_min = size5_costs[x]
    if size5_costs[x] > size5_cost_max:
        size5_cost_max = size5_costs[x]
    if size5_wall_time[x] < size5_walltime_min:
        size5_walltime_min = size5_wall_time[x]
    if size5_wall_time[x] > size5_walltime_max:
        size5_walltime_max = size5_wall_time[x]
    if size5_cpu_time[x] < size5_cputime_min:
        size5_cputime_min = size5_cpu_time[x]
    if size5_cpu_time[x] > size5_cputime_max:
        size5_cputime_max = size5_cpu_time[x]

    if size10_costs[x] < size10_cost_min:
        size10_cost_min = size10_costs[x]
    if size10_costs[x] > size10_cost_max:
        size10_cost_max = size10_costs[x]
    if size10_wall_time[x] < size10_walltime_min:
        size10_walltime_min = size10_wall_time[x]
    if size10_wall_time[x] > size10_walltime_max:
        size10_walltime_max = size10_wall_time[x]
    if size10_cpu_time[x] < size10_cputime_min:
        size10_cputime_min = size10_cpu_time[x]
    if size10_cpu_time[x] > size10_cputime_max:
        size10_cputime_max = size10_cpu_time[x]

    if size15_costs[x] < size15_cost_min:
        size15_cost_min = size15_costs[x]
    if size15_costs[x] > size15_cost_max:
        size15_cost_max = size15_costs[x]
    if size15_wall_time[x] < size15_walltime_min:
        size15_walltime_min = size15_wall_time[x]
    if size15_wall_time[x] > size15_walltime_max:
        size15_walltime_max = size15_wall_time[x]
    if size15_cpu_time[x] < size15_cputime_min:
        size15_cputime_min = size15_cpu_time[x]
    if size15_cpu_time[x] > size15_cputime_max:
        size15_cputime_max = size15_cpu_time[x]

    if size20_costs[x] < size20_cost_min:
        size20_cost_min = size20_costs[x]
    if size20_costs[x] > size20_cost_max:
        size20_cost_max = size20_costs[x]
    if size20_wall_time[x] < size20_walltime_min:
        size20_walltime_min = size20_wall_time[x]
    if size20_wall_time[x] > size20_walltime_max:
        size20_walltime_max = size20_wall_time[x]
    if size20_cpu_time[x] < size20_cputime_min:
        size20_cputime_min = size20_cpu_time[x]
    if size20_cpu_time[x] > size20_cputime_max:
        size20_cputime_max = size20_cpu_time[x]

    if size25_costs[x] < size25_cost_min:
        size25_cost_min = size25_costs[x]
    if size25_costs[x] > size25_cost_max:
        size25_cost_max = size25_costs[x]
    if size25_wall_time[x] < size25_walltime_min:
        size25_walltime_min = size25_wall_time[x]
    if size25_wall_time[x] > size25_walltime_max:
        size25_walltime_max = size25_wall_time[x]
    if size25_cpu_time[x] < size25_cputime_min:
        size25_cputime_min = size25_cpu_time[x]
    if size25_cpu_time[x] > size25_cputime_max:
        size25_cputime_max = size25_cpu_time[x]

    if size30_costs[x] < size30_cost_min:
        size30_cost_min = size30_costs[x]
    if size30_costs[x] > size30_cost_max:
        size30_cost_max = size30_costs[x]
    if size30_wall_time[x] < size30_walltime_min:
        size30_walltime_min = size30_wall_time[x]
    if size30_wall_time[x] > size30_walltime_max:
        size30_walltime_max = size30_wall_time[x]
    if size30_cpu_time[x] < size30_cputime_min:
        size30_cputime_min = size30_cpu_time[x]
    if size30_cpu_time[x] > size30_cputime_max:
        size30_cputime_max = size30_cpu_time[x]

size5_cost_avg = size5_cost_avg / 30
size5_walltime_avg = size5_walltime_avg / 30
size5_cputime_avg = size5_cputime_avg / 30

size10_cost_avg = size10_cost_avg / 30
size10_walltime_avg = size10_walltime_avg / 30
size10_cputime_avg = size10_cputime_avg / 30

size15_cost_avg = size15_cost_avg / 30
size15_walltime_avg = size15_walltime_avg / 30
size15_cputime_avg = size15_cputime_avg / 30

size20_cost_avg = size20_cost_avg / 30
size20_walltime_avg = size20_walltime_avg / 30
size20_cputime_avg = size20_cputime_avg / 30

size25_cost_avg = size25_cost_avg / 30
size25_walltime_avg = size25_walltime_avg / 30
size25_cputime_avg = size25_cputime_avg / 30

size30_cost_avg = size30_cost_avg / 30
size30_walltime_avg = size30_walltime_avg / 30
size30_cputime_avg = size30_cputime_avg / 30


fo_new = open("stats_files/Genetic_Stats.txt", "w+")
fo_new.write(str("size5 cost min:  %f" % (size5_cost_min) + "\n"))
fo_new.write(str("size5 cost max:  %f" % (size5_cost_max) + "\n"))
fo_new.write(str("size5 cost avg:  %f" % (size5_cost_avg) + "\n"))
fo_new.write(str("size5 wall time min:  %f" % (size5_walltime_min) + "\n"))
fo_new.write(str("size5 wall time max:  %f" % (size5_walltime_max) + "\n"))
fo_new.write(str("size5 wall time avg:  %f" % (size5_walltime_avg) + "\n"))
fo_new.write(str("size5 cpu time min:  %f" % (size5_cputime_min) + "\n"))
fo_new.write(str("size5 cpu time max:  %f" % (size5_cputime_max) + "\n"))
fo_new.write(str("size5 cpu time avg:  %f" % (size5_cputime_avg) + "\n"))

fo_new.write(str("size10 cost min:  %f" % (size10_cost_min) + "\n"))
fo_new.write(str("size10 cost max:  %f" % (size10_cost_max) + "\n"))
fo_new.write(str("size10 cost avg:  %f" % (size10_cost_avg) + "\n"))
fo_new.write(str("size10 wall time min:  %f" % (size10_walltime_min) + "\n"))
fo_new.write(str("size10 wall time max:  %f" % (size10_walltime_max) + "\n"))
fo_new.write(str("size10 wall time avg:  %f" % (size10_walltime_avg) + "\n"))
fo_new.write(str("size10 cpu time min:  %f" % (size10_cputime_min) + "\n"))
fo_new.write(str("size10 cpu time max:  %f" % (size10_cputime_max) + "\n"))
fo_new.write(str("size10 cpu time avg:  %f" % (size10_cputime_avg) + "\n"))


fo_new.write(str("size15 cost min:  %f" % (size15_cost_min) + "\n"))
fo_new.write(str("size15 cost max:  %f" % (size15_cost_max) + "\n"))
fo_new.write(str("size15 cost avg:  %f" % (size15_cost_avg) + "\n"))
fo_new.write(str("size15 wall time min:  %f" % (size15_walltime_min) + "\n"))
fo_new.write(str("size15 wall time max:  %f" % (size15_walltime_max) + "\n"))
fo_new.write(str("size15 wall time avg:  %f" % (size15_walltime_avg) + "\n"))
fo_new.write(str("size15 cpu time min:  %f" % (size15_cputime_min) + "\n"))
fo_new.write(str("size15 cpu time max:  %f" % (size15_cputime_max) + "\n"))
fo_new.write(str("size15 cpu time avg:  %f" % (size15_cputime_avg) + "\n"))

fo_new.write(str("size20 cost min:  %f" % (size20_cost_min) + "\n"))
fo_new.write(str("size20 cost max:  %f" % (size20_cost_max) + "\n"))
fo_new.write(str("size20 cost avg:  %f" % (size20_cost_avg) + "\n"))
fo_new.write(str("size20 wall time min:  %f" % (size20_walltime_min) + "\n"))
fo_new.write(str("size20 wall time max:  %f" % (size20_walltime_max) + "\n"))
fo_new.write(str("size20 wall time avg:  %f" % (size20_walltime_avg) + "\n"))
fo_new.write(str("size20 cpu time min:  %f" % (size20_cputime_min) + "\n"))
fo_new.write(str("size20 cpu time max:  %f" % (size20_cputime_max) + "\n"))
fo_new.write(str("size20 cpu time avg:  %f" % (size20_cputime_avg) + "\n"))

fo_new.write(str("size25 cost min:  %f" % (size25_cost_min) + "\n"))
fo_new.write(str("size25 cost max:  %f" % (size25_cost_max) + "\n"))
fo_new.write(str("size25 cost avg:  %f" % (size25_cost_avg) + "\n"))
fo_new.write(str("size25 wall time min:  %f" % (size25_walltime_min) + "\n"))
fo_new.write(str("size25 wall time max:  %f" % (size25_walltime_max) + "\n"))
fo_new.write(str("size25 wall time avg:  %f" % (size25_walltime_avg) + "\n"))
fo_new.write(str("size25 cpu time min:  %f" % (size25_cputime_min) + "\n"))
fo_new.write(str("size25 cpu time max:  %f" % (size25_cputime_max) + "\n"))
fo_new.write(str("size25 cpu time avg:  %f" % (size25_cputime_avg) + "\n"))

fo_new.write(str("size30 cost min:  %f" % (size30_cost_min) + "\n"))
fo_new.write(str("size30 cost max:  %f" % (size30_cost_max) + "\n"))
fo_new.write(str("size30 cost avg:  %f" % (size30_cost_avg) + "\n"))
fo_new.write(str("size30 wall time min:  %f" % (size30_walltime_min) + "\n"))
fo_new.write(str("size30 wall time max:  %f" % (size30_walltime_max) + "\n"))
fo_new.write(str("size30 wall time avg:  %f" % (size30_walltime_avg) + "\n"))
fo_new.write(str("size30 cpu time min:  %f" % (size30_cputime_min) + "\n"))
fo_new.write(str("size30 cpu time max:  %f" % (size30_cputime_max) + "\n"))
fo_new.write(str("size30 cpu time avg:  %f" % (size30_cputime_avg) + "\n"))

