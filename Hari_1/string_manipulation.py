#  UPPER CASE


text_a = "data analyst"
text_upper = (text_a).upper()


print(text_upper)

# lower case

text_b = "DATA analyst"
text_lower = (text_b).lower()
print(text_lower)


# INTEGERE


# variabel untuk a
a = 1
# variabel untuk b
b = 2
# variable penjumlahan
c = a + b
# variable perkalian
d = a * b + a / b




# STRING


print("hasil dari a + b =")
print(c)
print("hasil dari a * b + a / b =")
print(d)




print("aku" + " " + "suka" + " " + "sate")  # ini adalah contoh string concatenation




# FLOAT
pi = 3.14
r = 5
luas_lingkaran = pi * r * r
print("luas lingkaran dengan jari-jari 5 adalah")
print(luas_lingkaran)


# BOOLEAN
is_raining = True
is_sunny = False


# print("apakah sedang hujan?")
# print(is_raining)
# print("apakah sedang cerah?")
# print(is_sunny)


print("apakah sedang hujan?", is_raining, type(is_raining))
print("apakah sedang cerah?", is_sunny, type(is_sunny))




# NILAI NULL
x = None
print("nilai x adalah", x, type(x))



# INPUT

# Input Selalu String


nama = input("Masukkan Nama: ")
umur = input("Masukkan Umur: ")


print("Hello ", nama)
print("Umur mu sekarang ", umur)




# KONVERSI

a = "10"
b = "3.14"
c = 1
d = 0
e = 1000


int_a = int(a)
print(int_a + int_a)


float_b = float(b)
print(float_b * int_a * int_a)


bool_c = bool(c)
print("konversi dari ", c, " ialah ", bool_c)
bool_d = bool(d)
print("konversi dari ", d, " ialah ", bool_d)




str_e = str(e)
print(str_e, type(str_e))
print(str_e + str_e)




# STRING MANIPULATION

# UPPER CASE


text_a = "data analyst"
text_upper = (text_a).upper()


print(text_upper)

# LOWER CASE
text_b = "DATA_Science"
text_lower = (text_b).lower()


print(text_lower)


print(len(text_b))
print(text_b[0])
print(text_b[1])
print(text_b[2])
print(text_b[3])
print(text_b[4])
# print(text_b[5])
# print(text_b[6])
# print(text_b[7])
# print(text_b[8])
# print(text_b[9])
# print(text_b[10])
# print(text_b[11])


print(text_b[0:4])

# F-STRING

a = "hello"
b = 123


print(a, b)
print("a b")
print(f"{a} world!, Negara di dunia ada {b}")

# ARITMATIKA

# TAMBAH KURANG KALI BAGI
a = 10
b = 5


plus = a + b
minus = a - b
multiple = a * b
divide = a / b


# Bagi Bulat
c = 10
d = 3
bagi_bulat = 10 // 3


print(f"Bagi bulat dari {c} dengan {d} ialah {bagi_bulat}")


# Bagi Sisa (Modulo)
bagi_sisa = 10 % 3
print(f"Bagi sisa dari {c} dengan {d} ialah {bagi_sisa}")


# Pangkat
pangkat = c**d
print(f"Pangkat dari {c} dengan {d} ialah {pangkat}")

# OPERATOR

a = 100
b = 10**2
c = 101


a_apakah_sama_dengan_b = a == b
a_apakah_sama_dengan_c = a == c


# Sama Dengan


print(f"nilai a adalah {a}")
print(f"nilai b adalah {b}")
print(f"nilai c adalah {c}")




print(f"a apakah sama dengan b? {a_apakah_sama_dengan_b}")
print(f"a apakah sama dengan c? {a_apakah_sama_dengan_c}")


# Tidak Sama Dengan


a_apakah_tdk_sama_dengan_c = a != c
print(f"a apakah tidak sama dengan c? {a_apakah_tdk_sama_dengan_c}")


# Lebih Besar
a_lebih_besar_dari_b = a > b
print(f"a lebih besar dari b? {a_lebih_besar_dari_b}")


# Lebih Kecil
a_lebih_kecil_dari_c = a < c
print(f"a lebih kecil dari c? {a_lebih_kecil_dari_c}")


# Lebih Besar Sama Dengan
a_lebih_besar_sama_dengan_c = a >= c
print(f"a lebih besar sama dengan c? {a_lebih_besar_sama_dengan_c}")


# Lebih Kecil Sama Dengan
a_lebih_kecil_sama_dengan_c = a <= c
print(f"a lebih kecil sama dengan c? {a_lebih_kecil_sama_dengan_c}")


# IF ELSE

nilai = int(input("Masukkan Nilai: "))


if nilai >= 80:
   print("A")
elif nilai >= 70:
   print("B")
elif nilai >= 50:
   print("C")
else:
   print("D")


