BB = float(input("Masukkan Berat badan (kg): "))
TB = float(input("Masukkan Tinggi badan (m): "))

BMI = BB / (TB * TB)
print(f"Indeks Massa Tubuh (BMI): {BMI}")
if BMI <18.5:
    print("Kategori: Berat badan kurang")
elif 18.5 <= BMI < 25:
    print("Kategori: Berat badan normal")
elif 25 <= BMI < 30:
    print("Kategori: Berat badan berlebih")
else:
    print("Kategori: Obesitas")
    