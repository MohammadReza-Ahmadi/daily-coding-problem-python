def crossword_puzzle(crossword: [], words: str):
    wa = words.split(';')  # word array = wa
    wu = [0] * len(wa)  # word_used = wu
    w = wa[0]  # word = w
    for r in range(len(crossword)):
        for c in range(len(crossword[r])):
            print(crossword[r][c])
            if crossword[r][c] == '+':
                continue

            print('W')


# word index = wi
# d = direction -> 0=horizontal, 1=vertical
def crossword_recur(cw: [], r, c, w, wi, d):
    cw[r][c]
