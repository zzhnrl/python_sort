def selection_sort(da):
    n = len(da)
    for i in range(n-1):
        # Cari nilai terkecil di antara angka yang belum terurut
        min_index = i
        for j in range(i+1, n):
            if da[j] < da[min_index]:
                min_index = j

        # Tukar angka pada posisi iterasi saat ini dengan angka terkecil
        da[i], da[min_index] = da[min_index], da[i]

    return da


# Daftar angka awal
da = [9, 5, 3, 8, 2]

# Panggil fungsi selection_sort untuk mengurutkan daftar angka
da_terurut = selection_sort(da)

# Tampilkan daftar angka terurut
print("Daftar angka terurut:", da_terurut)
