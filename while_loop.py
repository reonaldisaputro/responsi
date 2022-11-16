
# continue adalah untuk mebuat skip suatu kondisi program
# break akan mengakhiri kondisi program

angka = 0

print(f"angka sekarang -> {angka}")

while angka < 5:
    # angka = angka + 1
    angka += 1

    # if angka == 3:
    #     continue

    if angka == 4:
        break

    print(f"angka sekarang -> {angka}")
    
    