def bubble_sort_books(db):
    n = len(db)
    for i in range(n):
        # Flag untuk menunjukkan apakah ada pertukaran dalam iterasi saat ini
        swapped = False
        for j in range(0, n-i-1):
            if db[j]["Jumlah Halaman"] > db[j+1]["Jumlah Halaman"]:
                # Lakukan pertukaran
                db[j], db[j+1] = db[j+1], db[j]
                swapped = True
        # Jika tidak ada pertukaran dalam iterasi saat ini, daftar buku sudah terurut
        if not swapped:
            break
    return db


# Daftar buku awal
db = [
    {"No.": 1, "Judul Buku": "Harry Potter and the Sorcerer's Stone",
        "Penulis": "J.K. Rowling", "Jumlah Halaman": 320},
    {"No.": 2, "Judul Buku": "To Kill a Mockingbird",
        "Penulis": "Harper Lee", "Jumlah Halaman": 281},
    {"No.": 3, "Judul Buku": "The Great Gatsby",
        "Penulis": "F. Scott Fitzgerald", "Jumlah Halaman": 180},
    {"No.": 4, "Judul Buku": "Pride and Prejudice",
        "Penulis": "Jane Austen", "Jumlah Halaman": 432},
    {"No.": 5, "Judul Buku": "1984", "Penulis": "George Orwell", "Jumlah Halaman": 328}
]

# Panggil fungsi bubble_sort_books untuk mengurutkan daftar buku
db_terurut = bubble_sort_books(db)

# Tampilkan daftar buku terurut
print("Daftar buku terurut berdasarkan jumlah halaman:")
for buku in db_terurut:
    print("No.:", buku["No."])
    print("Judul Buku:", buku["Judul Buku"])
    print("Penulis:", buku["Penulis"])
    print("Jumlah Halaman:", buku["Jumlah Halaman"])
    print()
