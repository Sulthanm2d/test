# Collection Datatype
# 1. List
# 2. Tuple
# 3. Dictionary
# 4. Set

# =======================================
# 1. LIST
# ditandai dengan [ ]
# Gunanya untuk menampung banyak data
# Bisa menampung lebih dari 1 tipe data
# Bisa menyimpan data yang duplikat (nilainya bisa sama)
# Mutable --> Bisa diubah isinya
# Isi dari list berurutan, sehingga bisa dilakukan indexing

# list kosong
list_kosong = []
print(list_kosong)

# Cara membuat list
list_buah = ["apel", "anggur", "jeruk", "semangka"]
print(list_buah)
print(type(list_buah))

list_angka = [1, 2, 3, 4, 5]
print(list_angka)
print(type(list_angka))

# membuat list dengan range
list_angka2 = list(range(1,6))
print(list_angka2)
print(type(list_angka2))

# list comprehension -> membuat list dengan for loop
list_angka3 = [i for i in range(1,6)] # [1, 2, 3, 4, 5]
print(list_angka3)
print(type(list_angka3))

list_angka_genap = [angka for angka in range(2, 11, 2)]
print(list_angka_genap)

list_angka_genap = [angka for angka in range(1, 11) if angka%2 == 0]
print(list_angka_genap)

# ganjil, genap, ganjil, genap
list_ganjil_genap = ["ganjil" if angka%2 != 0 else "genap" for angka in range(1, 11)]
print(list_ganjil_genap)

list_genap_ganjil = []
for angka in range(1, 11):
    if angka%2 != 0:
        list_genap_ganjil.append("ganjil")
    else:
        list_genap_ganjil.append("genap")
print(list_genap_ganjil)

# contoh
# [1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz]

list_fizz_buzz_kosong = []
for i in range(1, 11):
    if i%3 == 0:
        list_fizz_buzz_kosong.append("Fizz")
    elif i%5 == 0:
        list_fizz_buzz_kosong.append("Buzz")
    else:
        list_fizz_buzz_kosong.append(i)
print(list_fizz_buzz_kosong)

list_fizz_buzz = ["Fizz" if i%3 == 0 else "Buzz" if i%5 == 0 else i for i in range(1, 11)]
print(list_fizz_buzz)

# list bisa menyimpan berbagai macam tipe (tidak harus 1 jenis)
list_contoh = ["Budi", 25, "Data Scientist", 3.5, True, None]
print(list_contoh)
print(type(list_contoh))
print(type(list_contoh[-2]))

# indexing and slicing [start : stop : step]
print(list_contoh[2]) # Data Scientist
print(list_contoh[2:5]) # Data Scientist, 3.5, True
print(list_contoh[2:-1]) # Data Scientist, 3.5, True
print(list_contoh[1:5:2]) # 25, 3.5
print(list_contoh[2].split()[1])# Scientist
print(list_contoh[2][5:])# Scientist
# print(list_contoh[1][-1])# 5 --> ERROR karena int tidak bisa displit

# Mengubah ini value (mutable)
list_contoh[2] = "Data Analyst"
print(list_contoh)

# list di dalam list
list_contoh[-1] = [10, 20, 30]
print(list_contoh)

# cek panjang list
print(len(list_contoh))

# mencari data
print("data scientist" in list_contoh) # False --> karena sudah diganti ke data analyst
print("data analyst" in list_contoh) # False --> karena case sensitif
# print("data analyst" in list_contoh.lower()) # Error --> karena fungsi lower hanya bisa digunakan di string, list bukan merupakan string
print("Data Analyst" in list_contoh) # True
print(10 in list_contoh) # False --> 10 ada di dalam inner list

# .index() untuk mencari tahu, item yang dicari ada di index ke berapa
print(list_contoh.index("Data Analyst")) # 2
# print(list_contoh.index(10)) # error, .index() hanya bisa mencari item yang ada di dalam list


# latihan
list_contoh = ['Budi', 25, 'Data Analyst', 3.5, True, [10, 20, 30], 25]

print(list_contoh.index(25)) # 1

# output:
# 25 berada pada index ke 1
# 25 berada pada index ke 6

for i in range(len(list_contoh)):
    if list_contoh[i] == 25:
        print(f"25 berada pada index ke-{i}")

print(list(enumerate(list_contoh)))
for index, value in enumerate(list_contoh):
    if value == 25:
        print(f"25 berada pada index ke-{index}")

# ------------------------------------------------
list_huruf = ["a", "b", "c", "f"]
list_baru = list_huruf

print(list_huruf)
print(list_baru)

list_baru[-1] = "d"
print()
print(list_huruf)
print(list_baru)

list_baru_2 = list_huruf.copy()

print()
print(list_huruf)
print(list_baru_2)

list_baru_2[-1] = "e"
print()
print(list_huruf)
print(list_baru_2)


# --------------------------------------
# list concatenating --> untuk menggabungkan list

list_huruf = ["a", "b", "c", "d"]
list_angka = [1, 2, 3, 4]

# output = ["a", "b", "c", "d", 1, 2, 3, 4]

# +
list_gabungan = list_huruf + list_angka
print(list_gabungan)

# +
list_gabungan_2 = list_angka + list_huruf
print(list_gabungan_2)

# extend
print(list_huruf)
print(list_angka)
list_gabungan_extend = list_huruf.copy()
list_gabungan_extend.extend(list_angka)
print(list_huruf)
print(list_gabungan_extend)
print(len(list_gabungan_extend))

# append
print(list_huruf)
print(list_angka)
list_gabungan_append = list_huruf.copy()
list_gabungan_append.append(list_angka)
print(list_huruf)
print(list_gabungan_append)
print(len(list_gabungan_append))

# insert
print(list_huruf)
print(list_angka)
list_gabungan_insert = list_huruf.copy()
list_gabungan_insert.insert(2, list_angka)
print(list_huruf)
print(list_gabungan_insert)
print(len(list_gabungan_insert))

# --------------------------------------
# sorting --> defaultnya ascending (dari kecil ke besar)
list_acak = ["anggur", "a", "abc", "apel", "jeruk"]
print()
print(list_acak)
list_acak.sort()
print(list_acak)

# descending
list_acak = ["anggur", "a", "abc", "apel", "jeruk"]
print()
print(list_acak)
list_acak.sort(reverse=True)
print(list_acak)

list_angka_acak = [1,5,7,9,13,8,21,20,3,4]
print(list_angka_acak)
list_angka_acak.sort()
print(list_angka_acak)

# list_gabungan = [1, "b", 3, "a", "c", "d", 2, 4] # error (angka tidak bisa dibandingkan dengan huruf)
# print(list_gabungan)
# list_gabungan.sort()
# print(list_gabungan)

list_gabungan = ["1", "b", "3", "a", "c", "d", "2", "4", "A", "ABC", "C"]
print(list_gabungan)
list_gabungan.sort()
print(list_gabungan)

# ----------------------------
# memasukkan data ke list
list_buah = ["apel", "jeruk", "anggur"]
buah_baru = "mangga"

# append
print(list_buah)
list_buah.append(buah_baru)
print(list_buah)
list_buah.append("jambu")
print(list_buah)

# insert
list_buah.insert(3, 'melon')
print(list_buah)

# extend
# list_buah.extend('melon') # --> m, e, l, o, n
# print(list_buah)

list_buah.extend(['melon']) # --> melon
print(list_buah)

# -----------------------------------
# menghapus item di list
# pop() --> menghapus index terakhir
# remove() --> menghapus item berdarkan namanya
# del --> menghapus item berdasarkan index
# clear() --> menghapus semua item di list

list_buah = ['apel', 'jeruk', 'anggur', 'melon', 'mangga', 'jambu', 'melon']

# pop()
list_buah.pop()
print(list_buah)

list_buah.pop(1)
print(list_buah)

# remove()
list_buah.remove("melon")
print(list_buah)

# list_buah.remove("stroberi") # --> error karena stroberi tidak ada di dalam list
# print(list_buah)

# list_buah.remove("Apel") # --> error karena case sensitive
# print(list_buah)

# del
del list_buah[0]
print(list_buah)

# clear()
list_buah.clear()
print(list_buah)
