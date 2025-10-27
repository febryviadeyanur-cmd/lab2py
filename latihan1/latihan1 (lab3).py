import random

# Input nilai n pada saat runtime (dalam contoh ini, n = 5)
n = 5  # Menggunakan nilai n yang diberikan: 5

# Menggunakan kombinasi while dan for
for i in range(n):
    while True:
        # Menghasilkan bilangan acak antara 0 dan 1
        r = random.random()
        # Memastikan bilangan acak kurang dari 0.5
        if r < 0.5:
            print(f"Bilangan acak ke-{i+1}: {r}")
            break