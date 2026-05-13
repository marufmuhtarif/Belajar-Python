def add (a = None, b = None):
    if a is None or b is None:
        print("Parameter tidak lengkap!")
        return
    total = a + b
    return total
def subtract (a = None, b = None):
    if a is None or b is None:
        print("Parameter tidak lengkap!")
        return
    selisih = a - b
    return selisih

def bmi (berat = None, tinggi = None):
    if berat is None or tinggi is None:
        print("Parameter tidak lengkap!")
        return
    tinggi_m = tinggi / 100
    bmi_value = berat / (tinggi_m ** 2)
    return bmi_value

BB = float(input("Masukkan Berat badan (kg): "))
TB = float(input("Masukkan Tinggi badan (m): "))

BMI = BB / (TB * TB)
print(f"BMI Kamu adalah: {BMI}")
if BMI <18.5:
    print("Kategori: Berat badan kurang")
elif 18.5 <= BMI < 25:
    print("Kategori: Berat badan normal")
elif 25 <= BMI < 30:
    print("Kategori: Berat badan berlebih")
else:
    print("Kategori: Obesitas")
    