# ==========================================================
# Nama: Jhon Miguel Huang 
# NIM: J0403251025
# Kelas: A/P1
# ==========================================================

# ==========================================================
# Contoh Backtracking 1: Kombinasi Biner (n)
# ==========================================================

# Fungsi untuk menghasilkan semua kombinasi biner sepanjang n
def biner(n, hasil=""):
    
    # Base case:
    # Jika panjang string sudah sama dengan n
    if len(hasil) == n:
        print(hasil)  # Cetak hasil kombinasi
        return        # Hentikan cabang ini
    
    # Choose + Explore:
    # Tambahkan "0" lalu lanjut rekursi
    biner(n, hasil + "0")
    
    # Tambahkan "1" lalu lanjut rekursi
    biner(n, hasil + "1")

# Memanggil fungsi
biner(3)
