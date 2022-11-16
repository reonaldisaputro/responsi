# *
# **
# ***
# ****

count = 1
sisi = 9
# for i in range(sisi):
#     print("*"*count)
#     count += 1

spasi = int(sisi/2)
while True:

    if (count % 2):
        print(" " * spasi, "*" * count)

        # decrement
        spasi -= 1
        #increment
        count += 1
    
    else :
        count +=1
        continue

    if count > sisi:
        break

print(1 % 2)
