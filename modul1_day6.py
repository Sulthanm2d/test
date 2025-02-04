# Collection Datatypes

# List
# Tuple
# Dictionary
# Set

# ========================================
# 2. Tuple
# Ditandai dengan ( )
# Mirip dengan list, bisa menyimpan berbagai macam tipe data di dalam 1 tuple
# Bisa menyimpan data yang duplikat
# Index tuple berurutan, sehingga bisa dilakukan indexing
# Tuple bersifat imutable --> tidak dapat diubah isi nilainya


# Bisa menyimpan berbagai macam data, bisa diplikat
tuple_contoh = ("Hello", 1, 1, 20, 3.5, True, None)
print(tuple_contoh)
print(type(tuple_contoh))

tuple_1 = ("Hallo")
print(tuple_1)
print(type(tuple_1))

tuple_1 = ("Hallo",)
print(tuple_1)
print(len(tuple_1))
print(type(tuple_1))

tuple_hello, tuple_world = "hello", "world"
print(tuple_hello)
print(type(tuple_hello))
print(tuple_world)
print(type(tuple_world))


tuple_hello = "hello", "world", 23
print(tuple_hello)
print(type(tuple_hello))


# ordered atau bisa diindexing
tuple_contoh = ("Hello", 1, 1, 20, 3.5, True, None)
print(tuple_contoh[3]) # 20
print(tuple_contoh[-2]) # True
print(tuple_contoh[3:-1]) # 20, 3.5, True

# immutable --> tidak dapat diubah isinya
# tuple_contoh[-1] = False # Error --> 'tuple' object does not support item assignment
# print(tuple_contoh)

list_contoh = list(tuple_contoh)
list_contoh[-1] = False
tuple_contoh = tuple(list_contoh)
print(tuple_contoh)

# mengecek panjang tuple
print(len(tuple_contoh))

# mengecek item
print(20 in tuple_contoh) # True --> karena 20 ada di dalam tuple

# looping in tuple
for i in tuple_contoh:
    print(i)

tuple_comprehension = tuple((i for i in range(1,11)))
for i in tuple_comprehension:
    print(i, end=" ")
print(tuple_comprehension)
print(type(tuple_comprehension))

list_comprehension = [i for i in range(1,11)]
print(list_comprehension)

tuple_comprehension = (i for i in range(1,11))

for i in tuple_comprehension:
    if i%2 == 0:
        print(i)

# -----------------------
# Tuple Concatenating
# menambahkan item ke dalam tuple
# bisa menggunakan +
# ubah ke dalam bentuk list

tuple_1 = (1, 2, 3, 4)
tuple_2 = (10, 20, 30, 40)

tuple_gabungan = tuple_1+tuple_2
print(tuple_gabungan)

angka = 100

# tuple_gabungan_2 = tuple_gabungan + angka # error karena tuple hanya bisa ditambahkan dengan tuple
# print(tuple_gabungan_2)

# angka = (100)
# tuple_gabungan_2 = tuple_gabungan + angka  # error karena tuple hanya bisa ditambahkan dengan tuple
# print(tuple_gabungan_2)

angka = (100,)
tuple_gabungan_2 = tuple_gabungan + angka  # error karena tuple hanya bisa ditambahkan dengan tuple
print(tuple_gabungan_2)

# menggunakan __add__
angka_baru = (500,)
tuple_gabungan_3 = tuple_gabungan_2.__add__(angka_baru)
print(tuple_gabungan_3)

# Tuple tidak bisa dihapus, harus diubah ke dalam bentuk list dulu

# Tuple di dalam tuple (nested tuple)
tuple_peserta = (("Andi", 20, "Bandung"),
                 ("Budi", 35, "Surabaya"),
                 ("Coki", 25, "Jakarta"))

print(tuple_peserta)
print(len(tuple_peserta))

print(tuple_peserta[1][-1]) # Surabaya
print(tuple_peserta[1][1:]) # 35, Surabaya

# --------------------------
# 3. Dictionary
# ditandai dengan {key: value}
# Bisa menampung berbagai macam jenis tipe data
# Bisa dilakukan indexing tetapi bukan berdasarkan urutan index, melainkan menggunakan key
# key merupakan sebuah kode unik, sehingga key tidak boleh duplikat
# bersifat mutable --> bisa diubah isinya
# biasanya dictionary digunakan ketika data memiliki pola [0, "apel", 20, 30000] --> {"index": 0, "nama_buah": "apel", "stok": 20, "harga": 30000}

# cara membuat dictionary
contoh_dict = {"nama": "apel", 
               "stok": 20, 
               "harga": 30000}
print(contoh_dict)
print(type(contoh_dict))
print(len(contoh_dict))

# contoh key number
# {1:1, 2:4, 3:9, 4:16, 5:25}
dict_num = {}
for i in range(1,6):
    dict_num[i] = i ** 2
print(dict_num)

# dictionary comprehension
dict_compre = {i : i**2 for i in range(1,6)}
print(dict_compre)

# latihan
# {1:"ganjil", 2:"genap", 3:"ganjil", 4:"genap", 5:"ganjil"}

dict_genap_ganjil = {}
for i in range(1,6):
    if i%2 == 0:
        dict_genap_ganjil[i] = "genap"
    else:
        dict_genap_ganjil[i] = "ganjil"
print(dict_genap_ganjil)

dict_genap_ganjil_2 = {i:"genap" if i%2==0 else "ganjil" for i in range(1,6)}
print(dict_genap_ganjil_2)

# --------------------------
dict_contoh = {
    "nama": "Andi",
    "asal": "Bandung",
    "umur": 24,
    "status": True,
    30: "Saya"
}

print(dict_contoh)
print(dict_contoh["asal"])# Bandung
print(dict_contoh["umur"])# 24
print()

# ---------------------
# looping
# secara default nilainya berupa key
for i in dict_contoh:
    print(i)

print()

# looping berdasarkan keys
for i in dict_contoh.keys():
    print(i)

print()

# looping berdasarkan values
for i in dict_contoh.values():
    print(i)

print()

# bisa mengambil value dan key
for i in dict_contoh.items():
    print(i)

print()

for key, value in dict_contoh.items():
    print(key)
    print(value)

# ---------------------------------------
# dictionary di dalam dictionary
dict_menu = {
    'appetizer':{
        'nama':'dimsum',
        'harga': 30000
    },
    'main_course':{
        'nama':'nasi goreng',
        'harga': 50000
    },
    'dessert':{
        'nama':'puding',
        'harga': 20000
    }
}
print(dict_menu)
print(len(dict_menu))

print(dict_menu["main_course"]["nama"]) # nasi goreng
print(dict_menu["appetizer"]["harga"]) # 30000

# mengubah nilai
dict_menu["appetizer"]["harga"] = 25000
print(dict_menu["appetizer"]["harga"])

# menambah value baru
dict_menu["minuman"] = "es teh"
print(dict_menu)

dict_menu["minuman"] = {'nama': 'es teh', 'harga': 5000}
print(dict_menu)

# latihan
dict_menu = {
    'appetizer':{
        'nama':'dimsum',
        'harga': 30000
    },
    'main_course':{
        'nama':'nasi goreng',
        'harga': 50000
    },
    'dessert':{
        'nama':'puding',
        'harga': 20000
    }
}

# output: 
# dimsum
# nasi goreng
# puding

# cara manual
print(dict_menu["appetizer"]["nama"])
print(dict_menu["main_course"]["nama"])
print(dict_menu["dessert"]["nama"])
print()

# cara looping
for i in dict_menu:
    print(dict_menu[i]["nama"])
print()

for i in dict_menu.keys():
    print(dict_menu[i]["nama"])
print()

for i in dict_menu.values():
    print(i["nama"])
print()

# # comprehension
# print([i["nama"] for i in dict_menu.values()])


#--------------------------------------
# 4. SET
# set ditandai dengan { }
# Dapat menyimpan banyak tipe data
# Tidak bisa menyimpan data yang duplikat -> bisa digunakan untuk mencari unik data
# tidak punya urutan indexing --> tidak bisa dilakukan index (data selalu acak)
# mutable --> bisa ditambahkan dan dihapus datanya

contoh_set = {1, 2, 3, 4, 5, 6, 1, 4, 2, 8, 9, 4, 7}
print(contoh_set)
print(len(contoh_set))

contoh_set2 = {"apel", "anggur", "jeruk", "apel", "pisang"}
print(contoh_set2)
print(len(contoh_set2))

set_compre = {i for i in range(1,11)}
print(set_compre)

# print(contoh_set[2]) # ERROR --> tidak bisa dilakukan indexing

# -----------------------------------
# menambahkan data baru ke dalam set
contoh_set2 = {"apel", "anggur", "jeruk", "apel", "pisang"}

# add --> untuk menambahkan 1 item
contoh_set2.add("melon")
print(contoh_set2)

# update --> untuk menambahkan lebih dari 1 item --> harus disimpan kedalam sebuah collection datatypes
contoh_set2.update(["pepaya", "semangka"])
print(contoh_set2)

# -----------------------------------
# menghapus data yang terdapat di dalam sebuah data set
# remove --> menghapus item berdasarkan namanya, error jika tidak ditemukan
# discard --> menghapus item berdasarkan namanya, tidak melakukan apapun jika tidak ditemukan
# pop --> menghapus 1 item secara acak
# clear --> menghapus seluruh isi set

contoh_set2.remove("apel")
print(contoh_set2)

# contoh_set2.remove("stroberi") # --> error karena tidak ada di set
# print(contoh_set2)
print()

contoh_set2.discard("pepaya")
print(contoh_set2)

contoh_set2.discard("stroberi") 
print(contoh_set2)

contoh_set2.pop()
print(contoh_set2)

contoh_set2.clear()
print(contoh_set2)

# --------------------- 
# menggabungkan set

set_ganjil = {1, 3, 5, 7, 9}
set_prima = {2, 3, 5, 7}

# union --> menggabungkan 2 set, data yang duplikat hanya diambil 1x
print(set_ganjil)
print(set_prima)
print(set_ganjil.union(set_prima))
print()

# intersection --> mengambil irisan dari set A dan set B
print(set_ganjil)
print(set_prima)
print(set_ganjil.intersection(set_prima))
print()

# difference --> mengambil set A yang tidak ada di set B
print(set_ganjil)
print(set_prima)
print(set_ganjil.difference(set_prima))
print()

# symmetric difference --> mengambil set A dan set B yang tidak beririsan
print(set_ganjil)
print(set_prima)
print(set_ganjil.symmetric_difference(set_prima))
print()

#------------------------
# isdisjoint --> mengecek apakah set A dan set B seluruhnya berbeda
# issubset --> mengecek apakah seluruh set A merupakan bagian dari set B
# issuperset --> mengecek apakah seluruh set B merupakan bagian dari set A

set_ganjil = {1, 3, 5, 7, 9}
set_prima = {2, 3, 5, 7}
set_100 = {100, 200, 300}
set_angka = {1, 5, 7}

# disjoint
print(set_ganjil)
print(set_100)
print(set_ganjil.isdisjoint(set_100))
print()

# issubset
print(set_ganjil)
print(set_angka)
print(set_ganjil.issubset(set_angka)) # False
print()

print(set_ganjil)
print(set_angka)
print(set_angka.issubset(set_ganjil)) # True
print()

print(set_prima)
print(set_angka)
print(set_angka.issubset(set_prima)) # False
print()

# issuperset
print(set_ganjil)
print(set_angka)
print(set_ganjil.issuperset(set_angka)) # True
print()

print(set_ganjil)
print(set_angka)
print(set_angka.issuperset(set_ganjil)) # False
print()

print(set_prima)
print(set_angka)
print(set_angka.issuperset(set_prima)) # False
print()