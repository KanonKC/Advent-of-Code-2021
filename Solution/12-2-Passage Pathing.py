# --- Part Two ---
# After reviewing the available paths, you realize you might have time to visit a single small cave twice. Specifically, big caves can be visited any number of times, a single small cave can be visited at most twice, and the remaining small caves can be visited at most once. However, the caves named start and end can only be visited exactly once each: once you leave the start cave, you may not return to it, and once you reach the end cave, the path must end immediately.

# Now, the 36 possible paths through the first example above are:

# start,A,b,A,b,A,c,A,end
# start,A,b,A,b,A,end
# start,A,b,A,b,end
# start,A,b,A,c,A,b,A,end
# start,A,b,A,c,A,b,end
# start,A,b,A,c,A,c,A,end
# start,A,b,A,c,A,end
# start,A,b,A,end
# start,A,b,d,b,A,c,A,end
# start,A,b,d,b,A,end
# start,A,b,d,b,end
# start,A,b,end
# start,A,c,A,b,A,b,A,end
# start,A,c,A,b,A,b,end
# start,A,c,A,b,A,c,A,end
# start,A,c,A,b,A,end
# start,A,c,A,b,d,b,A,end
# start,A,c,A,b,d,b,end
# start,A,c,A,b,end
# start,A,c,A,c,A,b,A,end
# start,A,c,A,c,A,b,end
# start,A,c,A,c,A,end
# start,A,c,A,end
# start,A,end
# start,b,A,b,A,c,A,end
# start,b,A,b,A,end
# start,b,A,b,end
# start,b,A,c,A,b,A,end
# start,b,A,c,A,b,end
# start,b,A,c,A,c,A,end
# start,b,A,c,A,end
# start,b,A,end
# start,b,d,b,A,c,A,end
# start,b,d,b,A,end
# start,b,d,b,end
# start,b,end
# The slightly larger example above now has 103 paths through it, and the even larger example now has 3509 paths through it.

# Given these new rules, how many paths through this cave system are there?

Counter = 0

def alreadyTwice(journey):
    for i in journey:
        if i.upper() != i and len([j for j in journey if j == i]) == 2:
            return True
    return False

def initTraversal(cave):
    traversal(cave,'start',[])

def traversal(cave,point,journey):
    for i in cave[point]:
        if (i in journey and i.upper() != i and alreadyTwice(journey)) or i == 'start':
            continue
        if i == 'end':
            global Counter
            Counter += 1
            continue
        journey.append(i)
        traversal(cave,i,journey)
        journey.pop(len(journey)-1)

cave_map = {}

while True:
    x = input().split('-')
    if x == ['']:
        break
    if x[0] in cave_map:
        cave_map[x[0]].append(x[1])
    else:
        cave_map[x[0]] = [x[1]]
    if x[1] in cave_map:
        cave_map[x[1]].append(x[0])
    else:
        cave_map[x[1]] = [x[0]]

initTraversal(cave_map)
print(Counter)