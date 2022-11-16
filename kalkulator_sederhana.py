
angka1 = float(input("masukkan angka 1 ="))
operator = input("operator (+,-,x,/) : ")
angka2 = float(input("masukkan angka 2 ="))

if operator == "+":
    hasil = angka1 + angka2
    print(f"hasilnya adalah {hasil}")
elif operator == "-":
    hasil = angka1 - angka2
    print(f"hasilnya adalah {hasil}")
elif operator == "x" and operator == "*":
    hasil = angka1 * angka2
    print(f"hasilnya adalah {hasil}")
elif operator == "/" and operator == ":" :
    hasil = angka1 / angka2
    print(f"hasilnya adalah {hasil}")
else :
    print("masukkin yang bener dong")

print("akhir dari program, terima gaji")