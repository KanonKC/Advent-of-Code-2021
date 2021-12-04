# --- Part Two ---
# On the other hand, it might be wise to try a different strategy: let the giant squid win.

# You aren't sure how many bingo boards a giant squid could play at once, so rather than waste time counting its arms, the safe thing to do is to figure out which board will win last and choose that one. That way, no matter which boards it picks, it will win for sure.

# In the above example, the second board is the last to win, which happens after 13 is eventually called and its middle column is completely marked. If you were to keep playing until this point, the second board would have a sum of unmarked numbers equal to 148 for a final score of 148 * 13 = 1924.

# Figure out which board will win last. Once it wins, what would its final score be?

def isWin(bingo):
    # Horizontal
    for i in range(len(bingo)):
        if(sum(bingo[i])==-5):
            return True

    # Vertical
    for i in range(len(bingo)):
        verti = []
        for j in range(len(bingo[0])):
            verti.append(bingo[j][i])
        if(sum(verti)==-5):
            return True
    return False
        
def main():
    call = [int(i) for i in input().split(',')]
    y = input()
    static_bingo = []
    bingo = []
    while True:
        try:
            x = [[int(j) for j in input().split()] for i in range(5)]
            static_bingo.append(x)
            y = input()
        except:
            break

    for i in range(len(static_bingo)):
        m = []
        for j in range(len(static_bingo[0])):
            tm = []
            for k in range(len(static_bingo[0][0])):
                tm.append(static_bingo[i][j][k])
            m.append(tm)
        bingo.append(m)

    for c in call:
        pre_pop = []

        for i in range(len(bingo)):
            for j in range(len(bingo[0])):
                for k in range(len(bingo[0][0])):
                    if bingo[i][j][k] == c:
                        bingo[i][j][k] = -1
                        break
            if isWin(bingo[i]) and len(bingo)>1:
                pre_pop.append(i)

        pre_pop.sort(reverse=True)
        for i in pre_pop:
            bingo.pop(i)

        if len(bingo)==1 and isWin(bingo[0]):
            last_bingo = bingo[0]
            unmark = 0
            for i in last_bingo:
                for j in i:
                    if j != -1:
                        unmark += j
            print(unmark*c)
            return

main()