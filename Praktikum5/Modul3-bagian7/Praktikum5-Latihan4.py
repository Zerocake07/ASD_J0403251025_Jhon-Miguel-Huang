# ==========================================================
# Nama: Jhon Miguel Huang 
# NIM: J0403251025
# Kelas: A/P1
# ==========================================================

# ==========================================================
# Latihan 4: Kombinasi Huruf
# ==========================================================

# Fungsi untuk membuat semua kombinasi huruf A dan B sepanjang n
def kombinasi(n, hasil=""):
    
    # Base case:
    # Jika panjang string sudah sama dengan n
    if len(hasil) == n:
        print(hasil)  # Cetak kombinasi
        return        # Hentikan cabang ini
    
    # Tambahkan huruf "A"
    kombinasi(n, hasil + "A")
    
    # Tambahkan huruf "B"
    kombinasi(n, hasil + "B")

# Memanggil fungsi dengan panjang 2
kombinasi(2)