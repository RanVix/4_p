def strcounter(s):
    for sym in set(s):
        count = 0
        for subsym in s:
            if sym == subsym:
                count+=1
        print(sym, count)
strcounter("abcnra")