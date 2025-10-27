#Program untuk mengurutkan dari terkecil hingga terbesar

# Input 3 bilangan
a = int(input("Masukkan bilangan pertama: "))
b = int(input("Masukkan bilangan kedua: "))
c = int(input("Masukkan bilangan ketiga: "))

# Tampilkan bilangan asli
print(f"Bilangan asli:")
print(f"Bilangan ke-1 = (a)")
print(f"Bilangan ke-2 = (b)")
print(f"Bilangan ke-3 = (c)")
# Nested if untuk mengurutkan (membandingkan semua kemungkinan)
if a <= b and a <= c:
    if b <= c:
        terkecil, tengah, terbesar = a, b, c
    else:
        terkecil, tengah, terbesar = a, c, b
elif b <= a and b <= c:
    if a <= c:
        terkecil, tengah, terbesar = b, a, c
    else:
        terkecil, tengah, terbesar = b, c, a
else:  # c adalah yang terkecil
    if a <= b:
        terkecil, tengah, terbesar = c, a, b
    else:
        terkecil, tengah, terbesar = c, b, a

# Tampilkan hasil urutan
print("Urutan bilangan dari terkecil ke terbesar:")
print(f"(terkecil) (tengah) (terbesar)")
