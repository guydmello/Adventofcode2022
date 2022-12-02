with open("calories.txt", "r") as calories:
	lines = calories.readlines()
	# print(lines)

lines = [s.strip('\n') for s in lines] # remove the 8 from the string borders
lines = [s.replace('\n', '') for s in lines]

from itertools import groupby
lines =  [list(g) for k, g in groupby(lines, key=bool) if k]

new_list = [[int(x) for x in lst] for lst in lines]

list_2 = [sum(l) for l in new_list]

print(max(list_2))