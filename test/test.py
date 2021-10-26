n = 7
m = 21
pat = '.|.'
for i in range(int(n/2)):
    ini = int((m-3*(2*i+1))/2)
    for j in range(ini):
        print('-', end='')
    for k in range(2*i+1):
        print(pat, end='')
    for w in range(ini):
        print('-', end='')
    print()

        

