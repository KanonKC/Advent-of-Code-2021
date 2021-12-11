# --- Part Two ---
# It seems like the individual flashes aren't bright enough to navigate. However, you might have a better option: the flashes seem to be synchronizing!

# In the example above, the first time all octopuses flash simultaneously is step 195:

# After step 193:
# 5877777777
# 8877777777
# 7777777777
# 7777777777
# 7777777777
# 7777777777
# 7777777777
# 7777777777
# 7777777777
# 7777777777

# After step 194:
# 6988888888
# 9988888888
# 8888888888
# 8888888888
# 8888888888
# 8888888888
# 8888888888
# 8888888888
# 8888888888
# 8888888888

# After step 195:
# 0000000000
# 0000000000
# 0000000000
# 0000000000
# 0000000000
# 0000000000
# 0000000000
# 0000000000
# 0000000000
# 0000000000
# If you can calculate the exact moments when the octopuses will all flash simultaneously, you should be able to navigate through the cavern. What is the first step during which all octopuses flash?

Counter = 0

def glowing(octopus):
    visit = [[0 for j in i] for i in octopus]
    for i in range(len(octopus)):
        for j in range(len(octopus[0])):
            if not visit[i][j]:
                octopus[i][j] += 1
                flashing(octopus,i,j,visit)

def flashing(octopus,i,j,visit):
    if octopus[i][j] == 10:
        visit[i][j] = 1
        global Counter
        Counter += 1
        octopus[i][j] = 0
        for a in range(3):
            for b in range(3):
                if a == 1 and b == 1:
                    continue
                try:
                    i_shift = i-1+a
                    j_shift = j-1+b
                    if i_shift >= 0 and j_shift >= 0 and not visit[i_shift][j_shift]:
                        octopus[i_shift][j_shift] += 1
                        flashing(octopus,i_shift,j_shift,visit)
                except:
                    pass

def isGlowingAll(octopus):
    if sum([sum(i) for i in octopus]) == 0:
        return True
    return False

def printOct(octopus):
    for i in octopus:
        for j in i:
            print(j,end=" ")
        print()
    print()

octopus = []
while True:
    x = input()
    if x == '':
        break
    octopus.append([int(i) for i in x])

i = 0
while not isGlowingAll(octopus):
    glowing(octopus)
    i += 1
print(i)