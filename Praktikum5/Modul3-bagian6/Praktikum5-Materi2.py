# ==========================================================
# Nama: Jhon Miguel Huang 
# NIM: J0403251025
# Kelas: A/P1
# ==========================================================

# ==========================================================
# Contoh Rekursi 2: Tracing Masuk/Keluar
# ==========================================================

# Fungsi untuk melihat proses masuk dan keluar rekursi
def hitung(n):
    
    # Base case: jika n sudah 0
    if n == 0:
        print("Selesai")  # Tampilkan selesai
        return            # Hentikan fungsi
    
    # Fase stacking (masuk ke rekursi)
    print("Masuk:", n)
    
    # Pemanggilan rekursif dengan n-1
    hitung(n - 1)
    
    # Fase unwinding (keluar dari rekursi)
    print("Keluar:", n)

# Memanggil fungsi
hitung(3)