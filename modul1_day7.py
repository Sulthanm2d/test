import math

# PYTHON FUNCTION

# Function adalah sebuah blok kode yang terorganisir dan memiliki nama
# function bisa menerima input dan menghasilkan output
# function bisa digunakan berulang kali

# ---------------------------------------------------------
# Built-in Function
# fungsi bawaan yang ada di python

# print()
print("Halo")

# len
kalimat = "Saya seorang murid Purwadhika"
panjang_kalimat = len(kalimat)
print(panjang_kalimat)

# type
print(type(kalimat))

# ----------------------------------------------------------
# Regular Function
# syntax

# def namaFunction(parameter1, parameter2):
#       kalkulasi = parameter1 + parameter2
#       return kalkulasi

# Membuat fungsi pertambahan
def tambah(angka1, angka2):
    hasil = angka1 + angka2
    return hasil

print(tambah(5, 7))

# membuat pengecekan genap ganjil
def cekGenapGanjil(angka):
    if angka%2 == 0:
        return "Genap"
    else:
        return "Ganjil"

print(cekGenapGanjil(12498712))

# ------------------------------------------------------
# 1. Function tanpa input (tanpa parameter) dan tanpa output (tanpa return)
# cara memanggil namaFunction()

# salam
def salam():
    print("Selamat datang di Purwadhika!")
    print("Ayo kita belajar!")

salam()

# latihan
# buatlah fungsi mainMenu()
# output:
# Main Menu
# 1. Tampilkan semua buah
# 2. Menambahkan buah
# 3. Menghapus buah
# 4. Membeli buah
# 5. Exit

def mainMenu():
    print('''
    Main Menu
    1. Tampilkan semua buah
    2. Menambahkan buah
    3. Menghapus buah
    4. Membeli buah
    5. Exit
''')
    
mainMenu()

# ------------------------------------------------------
# 2. Function dengan input (dengan parameter) dan tanpa output (tanpa return)
# cara memanggil namaFunction(argument)

# membuat fungsi perkenalan
# Halo, nama Saya {nama}. Saya dari kelas {program}.
def perkenalan(nama, program):
    print(f"Halo, nama Saya {nama}. Saya dari kelas {program}.")

# pengisian argument harus urut sesuai dengan urutan parameter
perkenalan("Sulthan", "JCDS")
perkenalan("JCDS", "Sulthan")

# jika ingin tidak urut, harus ditulis nama parameternya
perkenalan(program="JCDS", nama="Sulthan")

# latihan
# Buatlah sebuah function bernama oscar
# dengan parameter: nama_aktor, judul_film, dan tahun
# outputnya: Pemenang actor terbaik di tahun {tahun} adalah {aktor} pada film berjudul {judul_film}
# Pemenang actor terbaik di tahun 2016 adalah leonardo di caprio pada film berjudul revennant

def oscar(nama_aktor, judul_film, tahun):
    print(f"Pemenang actor terbaik di tahun {tahun} adalah {nama_aktor} pada film berjudul {judul_film}")

oscar("Leonardo di Caprio", "The Revennant", 2016)

# ------------------------------------------------------
# 3. Function dengan input (dengan parameter) dan dengan output (dengan return)
# cara memanggil print(namaFunction(argument))

# membuat fungsi pangkat
def pangkat(angka):
    return angka**2

def pangkatV2(angka):
    hasil = angka**2
    return hasil

# print(pangkat(7))

# latian
# buat sebuah fungsi luasLingkaran
# dengan diameter sebagai inputnya

def luasLingkaran(diameter):
    luas = math.pi * (diameter/2)**2
    return luas

print(luasLingkaran(27))

# ------------------------------------------------------
# Default Parameter
# Jika ada parameter yang tidak diisi, 
# maka parameter akan diisi dengan argument default

def perkenalan(nama, program):
    print(f"Halo, nama Saya {nama}. Saya dari kelas {program}.")

perkenalan("Sulthan","JCDS")
perkenalan(program="JCDS",nama="Sulthan")
# perkenalan("Sulthan") # ERROR karena missing 1 argument

def perkenalan(nama="Unknown", program="Unknown"):
    print(f"Halo, nama Saya {nama}. Saya dari kelas {program}.")

perkenalan("Sulthan","JCDS")
perkenalan(program="JCDS",nama="Sulthan")
perkenalan("Sulthan") # Tidak error karena program secara default berisi "Unknown"
perkenalan()

# kalimat = "Purwadhika"
# kalimat.split()

# def range(start, stop, step=1):

# fungsi tambah
# inputnya kadang bisa 2 kadang bisa 3 angka

def tambah(angka1, angka2, angka3=0):
    return angka1 + angka2 + angka3

print(tambah(5,7))

# fungsi biodata
def bio(nama, umur=0):
    print(f"Halo nama Saya {nama}, umur saya {umur} tahun")

bio("Sulthan", "lima")

x = 5
x = "Aku"
print(x)

# ------------------------------------------------------
# local variable
# variable yang didefinisikan di dalam fungsi
# hanya berlaku ketika di dalam fungsi
# ketika dipanggil di luar fungsi, variable tidak berlaku

def tambah(angka1, angka2, angka3=0):
    hasil =  angka1 + angka2 + angka3
    return hasil

tambah(1,2,3)
# print(hasil) # error, karena hasil masih belum pernah didefinisikan. hasil pada function bersifat local variable

# ------------------------------------------------------
# global variable
# variable yang didefinisikan di luar fungsi
# nilainya bisa digunakan sepanjang program berjalan
# bersifat global, bisa diakses di luar maupun di dalam fungsi

x = 100 # --> global variable

def kali(angka):
    hasil = angka * x
    return hasil

print(kali(5))


# ------------------------------------------------------
# Prioritas local variable daripada global variable
x = 100 # --> global variable

def kali(angka):
    x = 10
    hasil = angka * x
    return hasil

print(kali(5))
print(x)

# ------------------------------------------------------
# ERROR karena x di local variable belum didefinisikan

# x = 100 # --> global variable

# def kali(angka):
#     x += 10
#     hasil = angka * x
#     return hasil

# print(kali(5))
# print(x)

# ------------------------------------------------------
# Solusi 1, define x local

x = 100 # --> global variable

def kali(angka):
    x = 0
    x += 10
    hasil = angka * x
    return hasil

print(kali(5))
print(x)

# solusi 2, jadikan x sebagai global
x = 100 # --> global variable

def kali(angka):
    global x
    x += 10
    hasil = angka * x
    return hasil

print(kali(5))
print(x)

# ---------------------------------
def KaBaTaKu(angka1, angka2):
    kali = angka1*angka2
    bagi = angka1/angka2
    tambah = angka1 + angka2
    kurang = angka1 - angka2
    return kali, bagi, tambah, kurang

a, b, c, d = KaBaTaKu(10, 2)
print(a)
print(b)
print(c)
print(d)

# ---------------------------------
# Callback Function
# memanggil fungsi lain sebagai argumen

def tambah(angka1, angka2):
    return angka1 + angka2

def kurang(angka1, angka2):
    return angka1 - angka2

def kali(angka1, angka2):
    return angka1 * angka2

def bagi(angka1, angka2):
    return angka1 / angka2

def kalkulator(operator, angka1, angka2):
    hasil = operator(angka1, angka2)
    return hasil

print(kalkulator(kurang, 7, 2))

# ---------------------------------
# Calling Other Function
# fungsi yang digunakan dari fungsi lain

def kuadrat(angka):
    return angka**2

# fungsi luas lingkaran
def luasLingkaran(diameter):
    hasil = math.pi * kuadrat(diameter/2)
    return hasil

print(luasLingkaran(14))

# ---------------------------------
# Recursive Function
# Memanggil fungsi ini sendiri

def countdown(counter):
    print(counter)
    counter -= 1

    if counter >= 0:
        countdown(counter)

countdown(5)

def faktorial(angka):
    hasil = angka
    angka -= 1
    if angka >= 1:
        hasil = hasil * faktorial(angka)
    return hasil

print()
print(faktorial(5))

# # ---------------------------

# def menu1():
#     print("Menampilkan daftar buah")

# def menu2():
#     print("Menambahkan buah")

# def menu3():
#     print("Menghapus buah")

# def menu4():
#     print("Membeli buah")

# def mainMenu():
#     print('''
# Selamat Datang di Toko Buah
          
# 1. Menampilkan daftar buah
# 2. Menambahkan buah
# 3. Menghapus buah
# 4. Membeli buah
#           ''')
#     menu = int(input("Masukkan menu yang anda pilih: "))
#     if menu == 1:
#         menu1()
#         mainMenu()
#     elif menu == 2:
#         menu2()
#         mainMenu()
#     elif menu == 3:
#         menu3()
#         mainMenu()
#     elif menu == 4:
#         menu4()
#         mainMenu()
#     elif menu == 5:
#         print("Terima kasih telah berbelanja")
#         return
#     else:
#         print("Input tidak valid!")
#         mainMenu()

    
# mainMenu()

# -------------------------------
# Lambda Function
# function kecil yang tidak memiliki nama
# bisa beberapa parameter tetapi hanya bisa 1 expression
# syntax --> lambda parameter : expression

def tambah(angka1, angka2):
    return angka1 + angka2

penjumlahan = lambda angka1, angka2 : angka1 + angka2
print(penjumlahan(2,3))


aritmatik = lambda angka1, angka2 : (angka1+angka2, angka1-angka2, angka1*angka2, angka1/angka2)
tambah, kurang, kali, bagi = aritmatik(10,2)
print(tambah)
print(kurang)
print(kali)
print(bagi)

# menampilkan huruf pertama dari kata yang diinput
def huruf_pertama(kata):
    return kata[0]

print(huruf_pertama("Saya"))

huruf_pertama_lambda = lambda huruf: huruf[0]
print(huruf_pertama_lambda("Saya"))

# Latihan
# buatlah fungsi pengecekan apakah angka yang diinput genap atau ganjil menggunakan lambda

def genap_ganjil(angka):
    if angka%2 == 0:
        return("Genap")
    else:
        return("Ganjil")
    
genap_ganjil_lambda = lambda angka: "Genap" if angka%2 == 0 else "Ganjil"

print(genap_ganjil_lambda(9))

# -------------------------------
# Map Function
# Function yang berguna untuk mengubah bentuk dari collection data types
# tidak mengurangi jumlah itemnya
# cara penulisannya --> map(function, collection_data)

list_angka = [1, 2, 3, 4, 5]

def kuadrat(angka):
    return angka**2

print(list_angka)
print(list(map(kuadrat, list_angka)))
print(list(map(lambda angka: angka**2, list_angka)))

# latihan
# ubah list angka tersebut menjadi string genap dan ganjil
print(list(map(lambda angka: "Genap" if angka%2 == 0 else "Ganjil", list_angka)))

# -------------------------------
# Filter Function
# Function yang berguna untuk menyaring atau menyeleksi dari collection data types
# mengurangi jumlah itemnya
# cara penulisannya --> filter(function, collection_data)

list_angka = [1,2,3,4,5,6,7,8,9,10]

def lebih5(angka):
    return angka>5

print(list_angka)
print(list(filter(lebih5, list_angka)))
print(list(filter(lambda angka: angka>5, list_angka)))

# tampilkan angka yang ganjil saja

print(list(filter(lambda angka: angka%2 !=0, list_angka)))

# tuple
tuple_angka = (1,2,3,4,5,6,7,8,9,10)
print(tuple(map(lambda angka: angka**2, tuple_angka)))
print(tuple(filter(lambda angka: angka%2 !=0, tuple_angka)))

tes