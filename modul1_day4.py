# Lopping statement
list_buah = ["Apel", "Mangga", "Jeruk", "Anggur", "Melon", "Pepaya", "Stroberi", "Naga"]

# Mangga, Anggur, Pepaya, Naga
print(list_buah[1])
print(list_buah[3])
print(list_buah[5])
print(list_buah[7])

print()
# looping:
#     print(list_buah[i])

for i in range(1,6,2):
    print(list_buah[i])

print()

for i in range(1, len(list_buah), 2):
    print(list_buah[i])

# Enumerate
list_buah = ["Apel", "Mangga", "Jeruk", "Anggur", "Melon", "Pepaya", "Stroberi", "Naga"]
for i in enumerate(list_buah):
    print(i)

# unpacking
list_buah = ["Apel", "Mangga", "Jeruk", "Anggur", "Melon", "Pepaya", "Stroberi", "Naga"]
for index, item in enumerate(list_buah): # (index, item)
    print(index)
    print(item)


list_buah = ["Apel", "Mangga", "Jeruk", "Anggur", "Melon", "Pepaya", "Stroberi", "Naga"]
for index, item in enumerate(list_buah): # (index, item)
    if item == "Mangga" or item == "Anggur" or item == "Pepaya" or item == "Naga":
        print(item)

# latihan
# output:
# Buah {Apel} berada pada index ke-{0}
# Buah Mangga berada pada index ke-1
# ...
# Buah Naga berada pada index ke-7
list_buah = ["Apel", "Mangga", "Jeruk", "Anggur", "Melon", "Pepaya", "Stroberi", "Naga"]

for index, item in enumerate(list_buah):
    print(f'Buah {item.upper()} berada pada index ke-{index}')


# list di dalam list
contoh_list = [["a", 100], ["b", 200], ["c",300]]

print(len(contoh_list)) # --> 3
print(contoh_list[1])
print(contoh_list[1][1])
print(contoh_list[1][0])

# latihan
# tampilkan 100, 200, 300
print(contoh_list[0][1])
print(contoh_list[1][1])
print(contoh_list[2][1])
print()

for i in range(len(contoh_list)):
    print(contoh_list[i][1])

print()

for i in range(len(contoh_list)):
    print(contoh_list[i][1], end=" ")

# latihan
# tampilkan a, b, c
contoh_list = [["a", 100], ["b", 200], ["c",300]]
print(contoh_list[0][0])
print(contoh_list[1][0])
print(contoh_list[2][0])
print()

for i in range(len(contoh_list)):
    print(contoh_list[i][0])

# latihan
# output:
# a
# 100
# b
# 200
# c
# 300
contoh_list = [["a", 100], ["b", 200], ["c",300]]

# cara1: 
for item in contoh_list: 
    print(item[0])
    print(item[1])
print()

# cara2: 
for huruf, angka in contoh_list: # item --> (huruf, angka)
    print(huruf)
    print(angka)
print()

# cara3:
print(contoh_list[0][0])
print(contoh_list[0][1])
print(contoh_list[1][0])
print(contoh_list[1][1])
print(contoh_list[2][0])
print(contoh_list[2][1])
print()

for i in range(len(contoh_list)): # [0,1,2] --> Outer Loop
    for j in range(2): # [0,1] --> Inner Loop
        print(contoh_list[i][j])

# latihan
mobil = ["toyota", "bmw", "tesla"]
negara = ["jepang", "jerman", "usa"]

# output:
# Mobil {Toyota} berasal dari {Jepang}
# Mobil {BMW} berasal dari {Jerman}
# Mobil {Tesla} berasal dari {Usa}

# manual
print(f"Mobil {mobil[0].title()} berasal dari {negara[0].title()}")
print(f"Mobil {mobil[1].title()} berasal dari {negara[1].title()}")
print(f"Mobil {mobil[2].title()} berasal dari {negara[2].title()}")
print()

# looping:
for i in range(len(mobil)):
    print(f"Mobil {mobil[i].title()} berasal dari {negara[i].title()}")

# zip
mobil = ["toyota", "bmw", "tesla"]
negara = ["jepang", "jerman", "usa"]
list_gabungan = list(zip(mobil,negara)) # --> (toyota, jepang), (bmw, jerman), (tesla, usa)
print(list_gabungan)

for mobil, negara in list_gabungan: 
    print(f"Mobil {mobil.title()} berasal dari {negara.title()}")

print()

for item in list_gabungan: 
    print(f"Mobil {item[0].title()} berasal dari {item[1].title()}")


# Loop Control Statement
# Break --> Untuk memberhentikan looping terdekat
# Continue --> Untuk melewatkan looping di iterasi tersebut
# Pass --> do nothing (jarang dipakai, biasa dipakai jika masih belum tau akan menulis code apa)

# Break
list_angka = range(1,101,1)

for i in list_angka:
    print(i)
    if i == 25:
        print("Angka 25 sudah ditemukan")
        break

kalimat = "Saya merupakan siswa Data Science di Purwadhika"

index = 0
for i in kalimat:
    if i.lower() == "d":
        print(f"huruf D pertama kali ditemukan di index ke-{index}")
        break
    index += 1


# Continue
kalimat = "Saya merupakan siswa Data Science di Purwadhika"

for huruf in kalimat:
    if huruf in ["a", "i", "u", "e", "o"]:
        continue
        print(huruf, end="")
    else:
        print(huruf, end="")

# Pass
kalimat = "Saya merupakan siswa Data Science di Purwadhika"

for huruf in kalimat:
    if huruf in ["a", "i", "u", "e", "o"]:
        pass # do nothing
        print(huruf, end="")
    else:
        print(huruf, end="")

# nested loop
# Suapan 1 makan nasi
# Suapan 1 makan daging
# Suapan 1 makan sayur
# Suapan 2 makan nasi
# Suapan 2 makan daging
# Suapan 2 makan sayur
#... Suapan 7 makan sayur

list_makanan = ["nasi", "daging", "sayur"]

for i in range(1,8): # [1, 2, 3, 4, 5, 6, 7]
    for makanan in list_makanan: # ["nasi", "daging", "sayur"]
        print(f"Suapan {i} makan {makanan}")

# Suapan 1
# makan nasi
# makan daging
# makan sayur
# Suapan 2
# makan nasi
# makan daging
# makan sayur

list_makanan = ["nasi", "daging", "sayur"]

for i in range(1,8): # [1, 2, 3, 4, 5, 6, 7] --> Outer Loop
    print(f"Suapan {i}")

    for makanan in list_makanan: # ["nasi", "daging", "sayur"] --> Inner loop
        print(f"makan {makanan}")

# latihan:

# masukkan input: 5
# * * *
# * * *
# * * *
# * * *
# * * *

angka = int(input("Masukkan input: "))

for i in range(angka):
    print("* * *")

angka = int(input("Masukkan input: "))

for i in range(angka):
    for j in range(3): # [0, 1, 2]
        print("*", end=" ")
    print()

# latihan
# 1 2 3
# 4 5 6
# 7 8 9

#cara 1:
count = 1
for i in range(3): # Outer loop merepresentasikan jumlah baris
    for j in range(3): # Inner loop merepresentasikan kolom
        print(count, end=" ")
        count +=1
    print()

#cara 2:
for i in range(0,7,3): # [0, 3, 6] Outer loop merepresentasikan jumlah baris
    for j in range(1, 4): # [1, 2, 3] Inner loop merepresentasikan kolom
        print(j+i, end=" ")
    print()


# latihan
# 1 
# 1 2 
# 1 2 3
# 1 2 3 4

# *
# * *
# * * *
# * * * *

for i in range(1, 5): # [1, 2, 3, 4]
    for j in range(i):
        print("*", end=" ")
    print()

for i in range(1, 5): # [1, 2, 3, 4]
    for j in range(i):
        print(j+1, end=" ")
    print()