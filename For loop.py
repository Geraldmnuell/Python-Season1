fruits = ["apple", "banana", "orange"]
for item in fruits:
    print(item)

print(20*'=')

numbers = [1, 6, 4, 3, 2, 5]
for item in numbers:
    print(item)

print(20*'=')

string = 'bolloon'
count_o = 0
for i in string:
    if i == 'o':
        count_o = count_o + 1
print(count_o)

print(20*'=')

for i in range(55, 100, 3):
    print(i)

print(20*'=')

for i in range(30, 4, -1):
    print(i)

print(20*'=')

num = int(input("Insert Number : "))
for i in range(1, num+1):
    print(i)

print(20*'=')

for i in range(10):
    print(i**2)

print(20*'=')

n = int(input("Insert number 2 : "))
for i in range(1, 11):
    print(n, "x", i, "=", i*n)

print(20*'=')

n = 6
i = 1
factorial = 1

while i <= n:
    factorial = i * factorial
    i = i + 1
print(factorial)

print(20*'=')

for i in range(2, 10, 3):
    print(i)

print(20*'=')

sum = 0
n = 5
for i in range(1, n + 1):
    sum = sum + i
print(sum)

print(20*'=')

num = 2358
count = 0
while num != 0:
    num = num // 10
    count = count + 1
print(count)

print(20*'=')

N, M = map(int, input().split())
result = 1
for i in range(M):
    result = N * result
print(result)

print(20*'=')

n = int(input())
a = 0
b = 1

print(a, b, end=" ")

for i in range(n-2):
    c = a + b
    print(c, end=" ")
    a = b
    b = c