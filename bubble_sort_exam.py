def bubble_sort(dn):
    n = len(dn)
    for i in range(n):
        # Flag untuk menunjukkan apakah ada pertukaran dalam iterasi saat ini
        swapped = False
        for j in range(0, n-i-1):
            if dn[j] > dn[j+1]:
                # Lakukan pertukaran
                dn[j], dn[j+1] = dn[j+1], dn[j]
                swapped = True
        # Jika tidak ada pertukaran dalam iterasi saat ini, daftar nilai sudah terurut
        if not swapped:
            break
    return dn


# Daftar nilai awal
dn = [78, 65, 90, 82, 70]

# Panggil fungsi bubble_sort untuk mengurutkan daftar nilai
dn_terurut = bubble_sort(dn)

# Tampilkan daftar nilai terurut
print("Daftar nilai terurut:", dn_terurut)

# Nurul Azizah
