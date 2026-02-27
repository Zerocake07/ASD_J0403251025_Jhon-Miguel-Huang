# ==========================================================
# Nama: Jhon Miguel Huang 
# NIM: J0403251025
# Kelas: A/P1
# ==========================================================

#==========================================
#Latihan 2: Tracing Rekursi
#==========================================\

# Membuat fungsi countdown dengan parameter n
def countdown(n):
    
    # Base case: jika n sudah 0
    if n == 0:
        print("Selesai")  # Cetak "Selesai"
        return            # Hentikan fungsi (tidak lanjut rekursi)
    
    # Ditampilkan sebelum pemanggilan rekursif (fase stacking / masuk)
    print("Masuk:", n)
    
    # Fungsi memanggil dirinya sendiri dengan nilai lebih kecil
    countdown(n - 1)
    
    # Ditampilkan setelah rekursi selesai (fase unwinding / keluar)
    print("Keluar:", n)

# Memanggil fungsi dengan nilai awal 3
countdown(3)