# --- Part Two ---
# Unfortunately, considering only horizontal and vertical lines doesn't give you the full picture; you need to also consider diagonal lines.

# Because of the limits of the hydrothermal vent mapping system, the lines in your list will only ever be horizontal, vertical, or a diagonal line at exactly 45 degrees. In other words:

# An entry like 1,1 -> 3,3 covers points 1,1, 2,2, and 3,3.
# An entry like 9,7 -> 7,9 covers points 9,7, 8,8, and 7,9.
# Considering all lines from the above example would now produce the following diagram:

# 1.1....11.
# .111...2..
# ..2.1.111.
# ...1.2.2..
# .112313211
# ...1.2....
# ..1...1...
# .1.....1..
# 1.......1.
# 222111....
# You still need to determine the number of points where at least two lines overlap. In the above example, this is still anywhere in the diagram with a 2 or larger - now a total of 12 points.

# Consider all of the lines. At how many points do at least two lines overlap?

p1 = []
p2 = []

while True:
    x = input().split()
    if len(x)==0:
        break
    p1.append([int(i) for i in x[0].split(',')])
    p2.append([int(i) for i in x[2].split(',')])

max_x = max(max([i[0] for i in p1]),max([i[0] for i in p2]))
max_y = max(max([i[1] for i in p1]),max([i[1] for i in p2]))

point = 0
path = [[0 for j in range(max_y+1)] for i in range(max_x+1)]

for i in range(len(p1)):
    # Horizontally Travel
    if p1[i][0] == p2[i][0]:
        start = min([p1[i][1],p2[i][1]])
        end = max([p1[i][1],p2[i][1]])+1
        for y in range(start,end):
            path[y][p1[i][0]] += 1
    
    # Vertically Travel
    elif p1[i][1] == p2[i][1]:
        start = min([p1[i][0],p2[i][0]])
        end = max([p1[i][0],p2[i][0]])+1
        for x in range(start,end):
            path[p1[i][1]][x] += 1

    # Diagonal \
    elif (p1[i][0]-p2[i][0])/(p1[i][1]-p2[i][1]) > 0:
        if p1[i][0] < p2[i][0]:
            start = p1[i]
        else:
            start = p2[i]
        distance = abs(p1[i][0]-p2[i][0])+1
        for d in range(distance):
            path[start[1]+d][start[0]+d] += 1
    
    # Diagonal /
    else:
        if p1[i][1] < p2[i][1]:
            start = [p1[i][1],p1[i][0]]
        else:
            start = [p2[i][1],p2[i][0]]
        distance = abs(p1[i][0] - p2[i][0])+1
        for d in range(distance):
            path[start[0]+d][start[1]-d] += 1

for i in path:
    for j in i:
        if j > 1:
            point += 1

print(point)