# a = 10
# b = 20
# if a < b:
#     print("a is smaller")
# else:
#     print("a is greater")

# <--For loop-->
# for i in range(2,10):
#     print(i)

# <-- Shallow Copy-->
# a = [10, 20, 30, 40]
# b=a
# print (id(a))
# print (id(b))

# <-- Deep Copy-->
# a = [10, 20, 30, 40]
# b=a.copy()
# print (id(a))
# print (id(b))

a = [10, 20, 30]
b = [40, 50, 60]
a.append(b)
# print(a)
# print(a[3])
# print(a[3][1])

c = [70, 80, 90]
b.append(c)
c[1] = 0
print(a)

# print(a[3][3][1])



# print(a[3][3][1])

