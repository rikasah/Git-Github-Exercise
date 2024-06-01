def calculate_bmi(weight, height):
    """
    Menghitung BMI berdasarkan berat badan (kg) dan tinggi badan (meter).

    :param weight: Berat badan dalam kilogram
    :param height: Tinggi badan dalam meter
    :return: BMI (Indeks Massa Tubuh)
    """
    try:
        bmi = weight / (height ** 2)
        return round(bmi, 2)
    except ZeroDivisionError:
        return "Tinggi badan tidak boleh nol."

def bmi_category(bmi):
    """
    Menentukan kategori BMI.

    :param bmi: Nilai BMI
    :return: Kategori BMI
    """
    if bmi < 18.5:
        return "Underweight (Kurus)"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight (Berat badan normal)"
    elif 25 <= bmi < 29.9:
        return "Overweight (Berat badan berlebih)"
    else:
        return "Obesity (Obesitas)"

# Contoh penggunaan
weight = float(input("Masukkan berat badan (kg): "))
height = float(input("Masukkan tinggi badan (meter): "))

bmi = calculate_bmi(weight, height)
category = bmi_category(bmi)

print(f"BMI: {bmi}")
print(f"Kategori: {category}")
