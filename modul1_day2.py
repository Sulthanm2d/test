# # MODUL 1 Day 1
# print("Hello World!")

# # Variable
# # Untuk menyimpan nilai dan bisa dipanggil ulang lebih mudah

# # string
# nama = 'Sulthan'
# print(nama)

# print(type(nama))

# nama2 = "Garda"
# print(nama2)

# print(type(nama2))

# pesan = '''UNDANGAN RAPAT

# Selamat pagi, silakan hadiri rapat pada:
# Hari: Rabu, 22 Januari 2025
# Tempat: Purwadhika Bandung

# Terima kasih
# '''
# print(pesan)

# print("Hallo nama Saya", nama + "!")
# print("Hallo nama Saya" + " " + nama + "!")

# print("Hallo nama Saya" + " " + nama2)
# print(nama + " " + nama2)
# print(nama, nama2)


# # numerik

# # integer (int)
# umur1 = 25
# print(umur1)
# print(type(umur1))

# umur2 = "25"
# print(umur2)
# print(type(umur2))

# # float
# berat = 55.5
# print(berat)
# print(type(berat))

# # boolean
# # isinya hanya True atau False

# isDigit = False
# print(isDigit)
# print(type(isDigit))

# Collection Data Type

# # list
# list_buah = ["apel", "jeruk", "anggur"]
# print(list_buah)
# print(type(list_buah))
# print(list_buah[1])

# # tuple
# tuple_buah = ("apel", "jeruk", "anggur")
# print(tuple_buah)
# print(type(tuple_buah))
# print(tuple_buah[-1])

# # dictionary
# # key : value

# dictionary1 = {"nama": ["Sulthan", "Umar"], "umur": 26}
# print(dictionary1)
# print(type(dictionary1))
# print(dictionary1["nama"][1])


# # latihan
# dictionary_latihan = {"nama": ["Adi", "Budi", "Dani"], "program": ["JCDS", "JCWD", "JCDM"]}

# # soal:
# # buat sebuah output yang menghasilkan Halo Budi, Selamat datang di program JCDS!
# print("Halo", dictionary_latihan["nama"][1] + ", Selamat datang di program", dictionary_latihan["program"][0] + "!")

# print(f"Halo {dictionary_latihan["nama"][1]}, Selamat datang di program {dictionary_latihan["program"][0]}!")

# # Casting
# angka1 = 123
# angka2 = "456"

# print(type(angka1))
# print(angka2)
# print(type(angka2))

# angka2 = int(angka2)
# print(type(angka2))

# angka3 = "23.9"
# print(type(float(angka3)))

# print(type(angka3))

# angka3 = float(angka3)
# print(type(angka3))

# angka4 = int(angka3)
# print(angka3)
# print(angka4)

# string_angka4 = str(angka4)
# print(string_angka4)
# print(type(string_angka4))

# print(float(angka4))

# angka5 = "23.5"
# print(int(float(angka5))) # tidak bisa langsung diubah ke integer karena "23.5" merupakan string dan tidak bisa diubah ke int

# # math
# import math
# pi = math.pi
# print(pi)

# #ceil
# print(math.ceil(pi))

# #floor
# print(math.floor(pi))

# #fabs
# x = -35
# print(x)
# print(math.fabs(x))

# #pow
# a = 2
# b = 3
# print(math.pow(b, a))
# print(a**b)

# #sqrt (akar)
# a = 9
# print(math.sqrt(a))

# # latihan
# # 1. Tentukan panjang sisi miring segitiga
# # a^2 + b^2 = c^2
# a = 5
# b = 12

# c = math.sqrt(a**2 + b**2)
# print(c)


# # 2. Tentukan luas lingkaran
# # luas = pi * r^2
# d = 14

# luas = math.pi * (d/2)**2

# print(luas)


# # Escape character

# print("Selamat datang di 'Purwadhika'")

# print("Selamat datang di \"Purwadhika\"")

# print("Selamat datang di \n\"Purwadhika\"")

# print("Selamat datang di \t\"Purwadhika\"")

# print("Selamat datang di \b\"Purwadhika\"")

# print("Selamat \\ datang di \"Purwadhika\"")


# # built-in function
# kalimat = "Selamat datang di Purwadhika"

# print(kalimat)

# # len --> untuk mengukur panjang string
# print(len(kalimat))

# # index --> mencari index pertama dari kata yang dicari
# print(kalimat.index("Purwadhika"))
# print(kalimat.index("a"))

# # split --> memsisahkan kalimat ketika bertemu seperator yang ditentukan, default seperator adalah spasi
# print(kalimat.split(sep=" "))

# # lower --> mengubah kalimat menjadi huruf kecil semua
# print(kalimat.lower())

# # upper --> mengubah kalimat menjadi huruf kapital semua
# print(kalimat.upper())

# # capitalize --> mengubah huruf awal pada kalimat menjadi kapital
# print(kalimat.capitalize())

# # title --> mengubah huruf awal pada tiap kata menjadi kapital
# print(kalimat.title())

# # [start : stop : step]
kalimat = "Selamat datang di Purwadhika"
# print(kalimat[:7]) # Selamat
# print(kalimat[::2]) # Slmtdtn iPrahk
# print(kalimat[-10:]) # Purwadhika
# print(kalimat[6::-1]) # tamaleS

kata = "purwadhika"

check = kata in kalimat.lower()
print(check)
print(kalimat)

# check = "purwadhika" not in kalimat
# print(check)

# # user input
# username = input("Masukkan username Anda: ")

# print("Halo", username)
# print(type(username))

# umur = int(input("Masukkan umur Anda: "))

# print("Umur Anda", umur)
# print(type(umur))

# latihan
# buatlah input user "Masukkan nama Anda: "
# buatlah input user "Masukkan program Anda: "
# Outputnya: Halo {NAMA}, selamat datang di program {Program} "Purwadhika"!

# nama = input("Masukkan nama Anda: ")
# program = input("Masukkan program Anda: ")

# print(f"Halo {nama.upper()}, selamat datang di program {program.capitalize()} \"Purwadhika\"!")