# find max sum of grouped numbers and then find top 3 sums added together

with open("calories.txt", "r") as calories:
	lines = calories.readlines()

lines = [s.strip('\n') for s in lines] 
lines = [s.replace('\n', '') for s in lines]

from itertools import groupby
lines =  [list(g) for k, g in groupby(lines, key=bool) if k]

new_list = [[int(x) for x in lst] for lst in lines]

list_2 = [sum(l) for l in new_list]

list2 = sorted(list_2)

print(list2[-1])

print(list2[-1] + list2[-2] + list2[-3])
