#Lab 2 : Latihan 1
#Program untuk menentukan bilangan terbesar dari 4 bilangan menggunakan if

#Input 4 bilangan

a = "Masukkan bilangan pertama"

b = "Masukkan bilangan kedua"

c = "Masukkan bilangan ketiga"

d = "Masukkan bilangan keempat"

#Inisialisasi bilangan terbesar sebagai a

terbesar = a

a adalah bilangan paling terbesar

b > terbesar = b

b adalah bilangan yang terbesar

c > terbesar = c

c adalah bilangan yang terbesar

d > terbesar = d

d adalah bilangan yang terbesar

#Output hasil

Bilangan terbesar dari keempat bilangan adalah terbesar

Masukkan bilangan pertama: 9

Masukkan bilangan kedua: 8

Masukkan bilangan ketiga: 7

Masukkan bilangan keempat: 6

Bilangan terbesar dari keempat bilangan adalah: 9

#Lab 2 : Latihan 2

#Program untuk mengurutkan 3 bilangan dari terkecil ke terbesar

a = "Masukkan bilangan pertama"

b = "Masukkan bilangan kedua"

c = "Masukkan bilangan ketiga"

#Tampilkan bilangan asli

Masukkan Bilangan asli

Bilangan ke 1 = a

Bilangan ke 2 = b

Bilangan ke 3 = c

#Nested if mengurutkan atau membandingkan

a<=b dan a<=c 

a adalah bilangan paling kecil

b<=c : terkecil, tengah, terbesar = a, b, c
     
     : terkecil, tengah, terbesar = a,c, b
     
b<=a dan b<=c

b adalah bilangan yang kecil

a<=c : terkecil, tengah, terbesar = b, a, c

     : terkecil, tengah, terbesar = b, c, a

c adalah bilangan yang kecil

Masukkan bilangan pertama: 10

Masukkan bilangan kedua: 3

Masukkan bilangan ketiga: 5

Bilangan asli:

Bilangan ke-1 = 10

Bilangan ke-2 = 3

Bilangan ke-3 =5

Urutan bilangan dari terkecil ke terbesar

3   5  10
finish

#Lab 3 : latihan 1

import random(bilangan acak)


#Input nilai n pada saat runtime

n = 5 #Menggunakan nilai n yang diberikan: 5

#Menggunakan kombinasi while dan for

for digunakan untuk menghasilkan angka acak saat berjalan

random.random() akan menghasilkan angka acak antara 0.0 sampai 1.0

#Memastikan bilangan acak kurang dari 0.5

r < 0.5 angka lebih kecil dari 0.5

Tampilkan bilangan acak

Bilangan acak ke-1: 0.43114459247034775

Bilangan acak ke-2: 0.33151987641394887

Bilangan acak ke-3: 0.1028044044435602

Bilangan acak ke-4: 0.2162075192820223

Bilangan acak ke-5: 0.14792931607266968

finish

#Lab 3 : Latihan 2
#Jumlah baris dan kolom

n= 10 

for i in range : baris i yang bernilai 0 sampai 9

for j in range : kolom j yang bernilai 0 sampai 9

Hasil penjumlahan i+j disatu baris yang sama

print () membuat baris baru

0 1 2 3 4 5 6 7 8 9 
1 2 3 4 5 6 7 8 9 10 
2 3 4 5 6 7 8 9 10 11 
3 4 5 6 7 8 9 10 11 12 
4 5 6 7 8 9 10 11 12 13 
5 6 7 8 9 10 11 12 13 14 
6 7 8 9 10 11 12 13 14 15 
7 8 9 10 11 12 13 14 15 16 
8 9 10 11 12 13 14 15 16 17 
9 10 11 12 13 14 15 16 17 18 
