def selection_sort_players(dftr_pemain):
    n = len(dftr_pemain)
    for i in range(n-1):
        # Cari pemain dengan jumlah gol terbanyak di antara pemain yang belum terurut
        max_index = i
        for j in range(i+1, n):
            if dftr_pemain[j]["Jumlah Gol"] > dftr_pemain[max_index]["Jumlah Gol"]:
                max_index = j

        # Tukar pemain pada posisi iterasi saat ini dengan pemain terbanyak gol
        dftr_pemain[i], dftr_pemain[max_index] = dftr_pemain[max_index], dftr_pemain[i]

    return dftr_pemain


# Daftar pemain awal
dftr_pemain = [
    {"No.": 1, "Nama Pemain": "Kylian Mbappe",
        "Klub": "Paris Saint Germain", "Jumlah Gol": 40},
    {"No.": 2, "Nama Pemain": "Victor Osimhen",
        "Klub": "Napoli", "Jumlah Gol": 28},
    {"No.": 3, "Nama Pemain": "Robert Lewandowski",
        "Klub": "Barcelona", "Jumlah Gol": 33},
    {"No.": 4, "Nama Pemain": "Erling Haaland", "Klub": " ", "Jumlah Gol": 52},
    {"No.": 5, "Nama Pemain": "Christopher Nkunku",
        "Klub": "RB Leipzig", "Jumlah Gol": 22},
]

# Panggil fungsi selection_sort_players untuk mengurutkan daftar pemain
dftr_pemain_terurut = selection_sort_players(dftr_pemain)

# Tampilkan daftar pemain terurut
print("Daftar pemain terurut berdasarkan jumlah gol:")
for pemain in dftr_pemain_terurut:
    print("No.:", pemain["No."])
    print("Nama Pemain:", pemain["Nama Pemain"])
    print("Klub:", pemain["Klub"])
    print("Jumlah Gol:", pemain["Jumlah Gol"])
    print()
