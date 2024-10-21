contoh sederhana while

x = 80
z = 1
while True:
    y = int(input(f"Masukkan nilai tes ke-{z} anda = "))
    z += 1
    if y >= x:
        break
