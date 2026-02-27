# ==========================================================
# Nama: Jhon Miguel Huang 
# NIM: J0403251025
# Kelas: A/P1
# ==========================================================

# ==========================================================
# Contoh Rekursi 3: Menjumlahkan Elemen List
# ==========================================================

# Fungsi untuk menjumlahkan isi list secara rekursif
def jumlah_list(data, index=0):
    
    # Base case:
    # Jika index sudah sama dengan panjang list,
    # berarti semua elemen sudah dijumlahkan
    if index == len(data):
        return 0  # Tidak ada lagi yang ditambahkan
    
    # Recursive case:
    # Ambil elemen sekarang + hasil rekursi berikutnya
    return data[index] + jumlah_list(data, index + 1)

# Memanggil fungsi
print(jumlah_list([2, 4, 6, 8]))  # Output: 20