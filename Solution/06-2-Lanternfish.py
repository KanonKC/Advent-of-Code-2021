# --- Part Two ---
# Suppose the lanternfish live forever and have unlimited food and space. Would they take over the entire ocean?

# After 256 days in the example above, there would be a total of 26984457539 lanternfish!

# How many lanternfish would there be after 256 days?

fish = [int(i) for i in input().split(',')]
counter = [0,0,0,0,0,0,0,0,0]

for i in fish:
    counter[i] += 1

for f in range(256):
    for i in range(len(counter)-1):
        if i == 0:
            baby = counter[0]
            counter[0] = 0
        counter[i] = counter[i+1]
        counter[i+1] = 0
    counter[6] += baby
    counter[8] += baby
print(sum(counter))
