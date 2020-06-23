print(id(1))
a = 1
print((a is 2))
print((a is 1))
a = 2
print((a is 2))
print((a is 1))

a, b, c, d = map(int, input().split())
print (a >= 90 and b > 80 and c > 85 and d >= 80)