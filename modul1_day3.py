# # Boolean
# condition1 = True
# condition2 = False

# print(condition1, condition2)

# # Comparison Operator
# # >, <, >=, <=, !=, ==

# angka1 = 5
# angka2 = 7

# print(angka1 > angka2)

# print(angka2 > angka1)
# print(angka1 < angka2)

# print(angka1 > angka1)
# print(angka1 >= angka1)

# print(angka1 != angka2)
# print(angka1 == angka2)

# print(angka1 == 7)

# # Logical Operator
# # and, or, not
# condition1 = True
# condition2 = False

# print(condition1 and condition2)
# print(condition1 or condition2)
# print(not condition1)
# print(not condition2)

# print(not condition1 or condition2)
# print(condition2 and condition1) # False
# print(not condition2 and condition1) # True
# print(condition1 and condition2) # False
# print(not condition1 and condition2) # False, not cuman berlaku di condition1
# print(not (condition1 and condition2)) # True, not berlaku setelah condition1 and condition2 dijalankan
# print(condition1 and not condition2) # True, karena condition1 = True dan not condition2 = True

# print(5>3 and 5>7)
# print(5>3 or 5>7)

# nilai = 95

# print(90 < nilai < 100)

# # Conditional Statement
# # if statement
# # if elif statement
# # if elif else statement

# # if statement
# # if <condition>:
# #   <statement>

# umur = 19

# if umur >= 17: # True
#     print("Umur Anda telah memenuhi persyaratan pembuatan SIM")
#     print("abc")

# print("tes")


# # if-else statement
# # syntax

# # if statement
# # if <condition>:
# #   <statement>
# # else:
# #   <statement>


# umur = int(input("Masukkan umur Anda: "))

# if umur >= 17: # True
#     print("Umur Anda telah memenuhi persyaratan pembuatan SIM")
# else:
#     print("Umur Anda belum memenuhi syarat pembuatan SIM")

# print("tes")


# if-elif-else statement
# syntax

# if statement
# if <condition1>:
#   <statement>
# elif <condition2>:
#   <statement>
# elif <condition-n>:
#   <statement>
# else:
#   <statement>

# 90-100 --> A
# 80-89 --> B
# 70-79 --> C
# 60-69 --> D
# 0-59 --> F

# grade = int(input("Masukkan nilai Anda: "))

# if grade >= 90 and grade <=100:
#     print("Grade: A")
# elif grade >= 80 and grade <=89:
#     print("Grade: B")
# elif grade >= 70 and grade <=79:
#     print("Grade: C")
# elif grade >= 60 and grade <=69:
#     print("Grade: D")
# elif grade >= 0 and grade <=59:
#     print("Grade: F")
# else:
#     print("Grade tidak valid, grade hanya bisa di angka antara 0-100")

# print("Proses selesai")

# grade = int(input("Masukkan nilai Anda: "))

# if 90 <= grade <=100:
#     print("Grade: A")
# elif 80 <= grade <=89:
#     print("Grade: B")
# elif 70 <= grade <=79:
#     print("Grade: C")
# elif 60 <= grade <=69:
#     print("Grade: D")
# elif 0 <= grade <=59:
#     print("Grade: F")
# else:
#     print("Grade tidak valid, grade hanya bisa di angka antara 0-100")

# print("Proses selesai")


# grade = int(input("Masukkan nilai Anda: "))

# if grade > 100:
#     print("Grade tidak valid, grade hanya bisa di angka antara 0-100")
# elif 90 <= grade:
#     print("Grade: A")
# elif 80 <= grade:
#     print("Grade: B")
# elif 70 <= grade:
#     print("Grade: C")
# elif 60 <= grade:
#     print("Grade: D")
# elif 0 <= grade:
#     print("Grade: F")
# else: # grade < 0
#     print("Grade tidak valid, grade hanya bisa di angka antara 0-100")

# print("Proses selesai")


# latihan
# Buatlah sebuah program yang melakukan input angka
# Jika angka ganjil tampilkan: Bilangan <angka> merupakan bilangan Ganjil
# Jika angka genap tampilkan: Bilangan <angka> merupakan bilangan Genap
# a = int(input("Masukkan nilai: "))

# if a % 2 == 0:
#     print(f"Bilangan {a} merupakan bilangan Genap")
# else:
#     print(f"Bilangan {a} merupakan bilangan Ganjil")


# Buatlah sebuah program yang melakukan input angka
# Angka hanya boleh dari 1 sampai 100.
# Jika angka di luar range, tampilkan: Angka tidak valid
# Jika angka ganjil tampilkan: Bilangan <angka> merupakan bilangan Ganjil
# Jika angka genap tampilkan: Bilangan <angka> merupakan bilangan Genap

# a = int(input("Masukkan nilai: "))

# if 1 <= a <= 100:
#     if a % 2 == 0:
#         print(f"Bilangan {a} merupakan bilangan Genap")
#     else:
#         print(f"Bilangan {a} merupakan bilangan Ganjil")
# else:
#     print("Angka tidak valid")

# if a <1 or a > 100:
#     print("Angka tidak valid")
# elif a % 2 == 0:
#     print(f"Bilangan {a} merupakan bilangan Genap")
# else:
#     print(f"Bilangan {a} merupakan bilangan Ganjil")


# Buatlah sebuah program yang melakukan input sebuah password
# password harus memiliki panjang 6 dan hanya boleh A-z, 0-9, _
# jika password valid tampilkan: Password Anda valid
# jika password tidak valid tampilkan: Password tidak valid, silakan coba lagi!

# password = input("Masukkan password Anda: ")

# if len(password) == 6 and (password.isalnum() or '_' in password):
#     print("Password valid")
# else:
#     print("Password tidak valid, silakan coba lagi!")

# Looping Statement
# While --> melakukan looping berdasarkan sebuah kondisi. Looping berkahir ketika kondisi sudah False
# For --> melakukan looping sebanyak total item. looping berakhir ketika item sudah habis

# While
# print halo 3x

# i = 1
# while i <= 3:
#     print("Halo")
#     i += 1

# # print angka 1 sampai 100

# angka = 1
# while angka <= 100:
#     print(angka, end=' ')
#     angka += 1


# For loop
# range(start, stop, step)

# print(list(range(1,10,2)))

# for i in range(5,8,1): # [5, 6, 7]
#     print("Hello World!")

# latihan
# print angka 1 sampai 100 dengan menggunakan for

# for i in range(1,101):
#     print(i, end=" ")

# list_buah = ["apel", "jeruk", "anggur"]

# # for i in list_buah:
# #     print("halo")

# for i in list_buah:
#     print(i)

# kalimat = "Selamat datang di purwadhika"

# # for i in kalimat.split():
# #     print(i)

# print(kalimat.split())



# for i in range(1, 101):
#     print(i)
#     if i == 27:
#         print("Angka 27 ditemukan")
#         break


# for i in range(1, 101):
#     if i == 27:
#         continue
#         print("Angka 27 ditemukan")
#         print(i)
#     else:
#         print(i)


# for i in range(1, 101):
#     if i == 27:
#         pass
#     else:
#         print(i)


# latihan
# tampilkan angka dari 1 sampai 100
# ketika angka kelipatan 3, maka tulis <angka> merupakan kelipatan 3
# ketika angka kelipatan 5, maka tulis <angka> merupakan kelipatan 5
# ketika angka kelipatan 3 dan kelipatan 5, maka tulis <angka> merupakan kelipatan 3 dan kelipatan 5

# 1
# 2
# 3 merupakan kelipatan 3
# 4 
# 5 merupakan kelipatan 5
# .
# .
# .
# 15 merupakan kelipatan 3 dan kelipatan 5
# .
# .
# .
# 100

# for angka in range(1, 101):
#     if angka%15 == 0:
#         print(f"{angka} merupakan kelipatan 3 dan kelipatan 5")
#     elif angka%5 == 0:
#         print(f"{angka} merupakan kelipatan 5")
#     elif angka%3 == 0:
#         print(f"{angka} merupakan kelipatan 3")
#     else:
#         print(angka)

# for angka in range(1, 101):
#     if angka in range(15, 101, 15):
#         print(f"{angka} merupakan kelipatan 3 dan kelipatan 5")
#     elif angka in range(5, 101, 5):
#         print(f"{angka} merupakan kelipatan 5")
#     elif angka in range(3, 101, 3):
#         print(f"{angka} merupakan kelipatan 3")
#     else:
#         print(angka)




# Buatlah sebuah program yang melakukan input sebuah password
# password harus memiliki panjang 6 dan hanya boleh A-z, 0-9, _
# jika password valid tampilkan: Password Anda valid
# jika password tidak valid tampilkan: Password tidak valid, silakan coba lagi!
# buat program selalu looping input hingga password valid


# a = 0
# while a==0:
#     password = input("Masukkan password Anda: ")

#     if len(password) == 6 and (password.isalnum() or '_' in password):
#         print("Password valid")
#         a = 1
#     else:
#         print("Password tidak valid, silakan coba lagi!")

# while True:
#     password = input("Masukkan password Anda: ")

#     if len(password) == 6 and (password.isalnum() or '_' in password):
#         print("Password valid")
#         break
#     else:
#         print("Password tidak valid, silakan coba lagi!")

# password = input("Masukkan password Anda: ")
# while not (len(password) == 6 and (password.isalnum() or '_' in password)):
#     print("Password tidak valid, silakan coba lagi!")
#     password = input("Masukkan password Anda: ")
# else:
#     print("Password valid")

