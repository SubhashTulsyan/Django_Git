from functools import reduce
# def print_rangoli(size):
#     alpha = 'abcdefijklmnopqrstuvwxyz'
#     alpha_input = alpha[:size]
#     row = 2*size-1
#     col = 4*size-3
#     for i in range(int((row/2))):
#         for j in range(col):
#             print(j, end='')
#         print()

# if __name__ == '__main__':
#     n = int(input())
#     print_rangoli(n)


# dic = {
#     'name': 'Subhash',
# }
# #a = dic['name1']
# b = dic.get('name1')
# c = dic.get('name1', 'Not Found !!')

# #print(a)
# print(b)
# print(c)

# a = lambda x,y : x+y 
# print(a(5, 6))

# ab = (1,2,3,2,)
# print(a.count(2))
# print(a.index(1))
# for i in a:
#     print(i)
# i = 0
# while(a[i]< a[i]+1):
#     print(a[i])
#     i = i+1
# a = {
#     'name': 'Subhash',
#     'age': 27,
#     101: 'roll',
# }

# a[0] = 5
# print(a.setdefault('email', '@asd'))
# print(max(ab))

# dic = {}
# a = {i: i*2 for i in range(x) for x in range(5) if x==2}
# print(a)


# lst = [2,3,4,5,6,7,8]
# print([lst[i:i+int(len(lst)/2)+1] for i in range(int(len(lst)/2)+1)])
# lst = [2,3,4,5,6]
# [[j] for i in range(int(len(lst)/2)+1) for j in lst[i:i+int(len(lst)/2)+1]]



def deco_add(func):
    def inner():
        func()
        print('in deco')
    return inner

@deco_add #2
def add():
    print('add')
# 1
# z = add
# a = deco_add(z)
# a()
add()


l = [1,2,3,4]

r = map(lambda x: x+1, l)
s = filter(lambda x: x%2==0, l)
t = reduce(lambda x,y: x*y, l)
# for i in r:
#     print(i)
# for i in s:
#     print(i)

print(t)