# class Test:
#     def __init__(self, size):
#         self.size = size

# class Tst(Test):
    
#     def __init__(self, size):
#         super().__init__(self)
#         #self.shape = shape


# tst = Tst(size = 'Circle')

# print(tst.size)

# def sm():
#     a = 10
#     b = 20

#     print('Sum: ', a+b)
# sm()


arr = [1,2,3,4,5]
#print(list(range(len(arr)-1, -1, -1)))
tmp = arr[0]
# for i in range(len(arr)-1, -1, -1):
#     #print(arr[i])
#     arr[i] = arr[i-1]
#     #arr[i], arr[i-1] = arr[i-1], arr[i-2]

# for i in range(1)
# print(arr)


arr=[1,2,3,4,5]




for k in range(2):
    tmp = arr[0]
    for i in range(len(arr)-1):
        arr[i] = arr[i+1]
    arr[-1] = tmp