nama =["Alice", "Bob", "Charlie", "David", "Eve"]
nilai = [85, 92, 78, 90, 88]
# Menampilkan nama dan nilai
print(nama)
print(nilai)

# print dengan index
print("\n")
print("Print dengan index")
# print(f"Nama: {nama[0]}, Nilai: {nilai[0]}")
for i in range(len(nama)):
    print(f"Nama: {nama[i]}, Nilai: {nilai[i]}")

    # Menambahkan data baru
input_nama = input("Masukkan nama baru:")
input_nilai = int(input("Masukkan nilai baru:"))
nama.append(input_nama)
nilai.append(input_nilai)
print("\nData setelah ditambahkan: ")
print(nama)
print(nilai)
for i in range(len(nama)):
    print(f"Nama: {nama[i]}, Nilai: {nilai[i]}")

pop_nama = input("Masukkan nama yang ingin dihapus:")
if pop_nama in nama:
    index = nama.index(pop_nama)
    nama.pop(index)
    nilai.pop(index)
    print("\n Data setelah dihapus:")
    print(nama)
    print(nilai)
    for i in range(len(nama)):
        print(f"Nama: {nama[i]}, Nilai: {nilai[i]}")
    else:
        # print("Nama tidak ditemukan dalm daftar.")
        if pop_nama in nama:
            index = nama.index(pop_nama)
            nama.pop(index)
            nilai.pop(index)
            print("\n Data setelah dihapus: ")
            print(nama)
            print(nilai)
            for i in range(len(nama)):
                print(f"Nama: {nama[i]}, Nilai: {nilai[i]}")
            else:
                print("Nama tidak ditemukan dalam daftar.")

# ===============================================================================================================================


# index = [0, 1, 2, 3, 4, 5, 6]
# nama = ["Alice", "Bob", "Farah", "Edi", "Charlie", "Gita", "Hasti"]


# nama_slice_3_tengah = nama[2:5]


# print(nama_slice_3_tengah)  # ['Charlie', 'Edi', 'Farah']


# nama_slice_3_tengah[2] = "Clara"
# print("\n")
# print(nama_slice_3_tengah)


# # INSERT
# nama_slice_3_tengah.insert(1, "Zara")
# print("\n INSERT")
# print(nama_slice_3_tengah)


# # APPEND
# nama_slice_3_tengah.append("Dina")
# print("\n APPEND")
# print(nama_slice_3_tengah)


# # SORT
# nama_slice_3_tengah.sort()
# print("\n SORT")
# print(nama_slice_3_tengah)


# # Print dengan index
# # print("\n")


# # print("Print dengan index")
# # print(f"indeks -1 adalaha {nama[-1]}")
# # print(f"panjang data dari nama = {len(nama)}")


# # print(f"Nama {nama[1]} mendapatkan nilai {nilai[1]}")


# # for z in range(len(nama)):
# #     print(f"Nama {nama[z]} mendapatkan nilai {nilai[z]}")


