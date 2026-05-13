import aritmatika as f
# print(aritmatika.add(10, 10))
# print(aritmatika.subtract(20, 6))

BB = float(input("Masukkan Berat badan (kg): "))
TB = float(input("Masukkan Tinggi badan (m): "))

# BMI = f.bmi(BB, TB)
# print(f"BMI Kamu adalah: {BMI}")
bmi = f.bmi(BB, TB)
print ("BMI Kamu adalah:", bmi)
f.bmi_check(bmi)
