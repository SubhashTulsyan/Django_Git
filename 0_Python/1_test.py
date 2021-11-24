def countingValleys(steps, path):
    vcnt = 0
    res = 0
    for i in range(steps):
        if path[i] == 'U':
            res = res + 1
        if path[i] == 'D':
            res = res - 1
        if res == 0:
            vcnt = vcnt + 1
    return vcnt
        
t = countingValleys(8, 'UDDDUDUU')
print(t)
