"""
KEEP LEARN FOR UPGRADE YOUR SKILL!!!!
"""

print('\n', 10*"=", "PRACTICE #1", 10*'=', '\n')

print(7 + 9)   # BAGIAN PERTAMA
print (7 + 9)

print(11*13) # BAGIAN KEDUA
print(2*(11*13)) # BAGIAN KETIGA

a = "hallo" # BAGIAN KEEMPAT
b = "brooo"

print(a, b) # BAGIAN LIMA

length = 45 # BAGIAN ENAM
width = 76
area = length * width
print(area)

pi = 3.14  # BAGIAN TUJUH
radius = 8.9
area = pi * (radius**2)
print(area)

operasi = 1 + 1 
if operasi == 3:
    print(bool(operasi))
else:
    print("hasil salah")

print('\n', 10*"=", "PRACTICE #2", 10*'=', '\n')

# nomor 1
s = 14
area = s * s
cost = area * 7

print(area)
print(cost)

# nomor 2
a = -50
b = 40

total = a + b
product = a * b

print(total, product)

# nomor 3
a = -10
b = -3
print(a * b)

print('\n', 10*'=', "PRACTICE #3", 10*'=', '\n')
x = 10
x += 5
x *= 2
print(x)

height1 = 15
height2 = 13
print(height1 != height2)

a = 5
b = 3
c = 2
d = 5
result1 = a + b
result2 = c * d
print(result1 < result2)

age = 20
voting_age = 18
print(age > voting_age)

a = 15
b = 15.0
print(a == b)

word = "tenet "
print(word * 100)

print(25 * 69)

greeting = "hello"
len_string = len(greeting)
print(len_string)

name = "Go" * 2 + "gle"
print(name)

print(len("Hello World!"))

print('\n', 10*'=', "PRACTICE #4", 10*'=', '\n')

num = int(input("Insert the number = "))
print(num)

a = int(input())
b = int(input())
sum = a + b
diff = a - b
print(sum)
print(diff)

sentence = "Air Water Earth Fire"
words = sentence.split()

reverse = " ".join(words[::-1])
print(reverse)

print('\n', 10*'=', "PRACTICE #5", 10*'=', '\n')

a = 25
b = 20

if a > b:
    print("Coding is fun")

score = int(input("Insert score : "))

if score == 100:
    print("Perfect Score")
elif score >= 80 and score <= 100:
    print("Almost perfect score")
elif score < 80:
    print("Nice Try!")


num = 12
if num % 3 == 0:
    print("Divisible by 3")
elif num % 4 == 0:
    print("Divisible by 4")
    
is_logged_in = True

if is_logged_in:
    print("Welcome!")
else:
    print("Please log in.")

angka = [1, 2, 3, 4, 5, 6]

for angka in range(5):
    print(angka)

a = 5
b = 2
hasil = 5 // 2
print(hasil)