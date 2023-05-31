def bubble_sort_descending(da):
    n = len(da)
    for i in range(n):
        # Flag untuk menunjukkan apakah ada pertukaran dalam iterasi saat ini
        swapped = False
        for j in range(0, n-i-1):
            if da[j] < da[j+1]:
                # Lakukan pertukaran
                da[j], da[j+1] = da[j+1], da[j]
                swapped = True
        # Jika tidak ada pertukaran dalam iterasi saat ini, daftar angka sudah terurut
        if not swapped:
            break
    return da


# Daftar angka awal
da = [42, 19, 33, 8, 55]

# Panggil fungsi bubble_sort_descending untuk mengurutkan daftar angka
da_terurut = bubble_sort_descending(da)

# Tampilkan daftar angka terurut
print("Daftar angka terurut:", da_terurut)

# Nurul Azizah
