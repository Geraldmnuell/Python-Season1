"""
Pengenalan String
"""

data = "ini adalah string"
print(data)
print(type(data))

# 1. Cara membuat string
'''
    1. Menggunakan single quote '...'
    2. Menggunakan double qu ote "..."
'''

data = 'ini menggunakan single quote'
print(data)
data = "Menggunakan double quote"
print(data)
print("ini adalah hari jum'at")

# 2. Menggunakan tanda \
# membuat tanda ' menjadi string
print('mari shalat jum\'at')
print('g\'day, isn\'t it?')

# backlash
print("C:\\user\\Gerald") # menambahkan backlash

# Tab
print("ucup\totong") # menambahkan \t, dan semakin jauh

# backspace
print("ucup \botong") # menambahkan \b, jadi dekatan

# newline
print('baris pertama.\nbaris kedua.') # LF -> Line Feed -> unix, macos, linux
print('baris pertama.\rbaris kedua.') # CR -> carriage return -> commodore, acorn, lisp
print('baris pertama.\r\nbaris kedua.') # CRLF -> LIne Feed Carriage Return -> dipakai oleh windows

# 3 String literal atau raw
# hati hati
print('C:\nnew folder') # akan salah pathnya

# menggunakan raw string
print(r'C:\new folder') # tambahkan r

# multiline literal string
print(""" 
nama : gerald
umur : 18 tahun      
""")

# multiline literal string dan RAW
print("""
Nama : Gerald Imanuel Manongga
NIM : 250211060004
Link akun github : https//github.com
""")