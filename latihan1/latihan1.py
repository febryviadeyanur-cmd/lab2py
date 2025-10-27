# Program untuk menemukan bilangan terbesar dari 4 bilangan menggunakan if

# Input 4 bilangan
a = int(input("Masukkan bilangan pertama: "))
b = int(input("Masukkan bilangan kedua: "))
c = int(input("Masukkan bilangan ketiga: "))
d = int(input("Masukkan bilangan keempat: "))

# Inisialisasi bilangan terbesar sebagai a
terbesar = a

# Bandingkan dengan b
if b > terbesar:
    terbesar = b

# Bandingkan dengan c
if c > terbesar:
    terbesar = c

# Bandingkan dengan d
if d > terbesar:
    terbesar = d

# Output hasil
print(f"Bilangan terbesar dari keempat bilangan adalah: {terbesar}")
