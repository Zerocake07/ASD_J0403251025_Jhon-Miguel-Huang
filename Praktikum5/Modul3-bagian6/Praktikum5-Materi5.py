# ==========================================================
# Nama: Jhon Miguel Huang 
# NIM: J0403251025
# Kelas: A/P1
# ==========================================================

# ==========================================================
# Contoh Backtracking 2: Kombinasi Biner dengan Batas '1' (Pruning)
# ==========================================================


# Fungsi kombinasi biner dengan batas jumlah angka 1
def biner_batas(n, batas, hasil="", jumlah_1=0):
    
    # Pruning:
    # Jika jumlah angka 1 sudah melebihi batas,
    # hentikan cabang ini
    if jumlah_1 > batas:
        return
    
    # Base case:
    # Jika panjang string sudah n
    if len(hasil) == n:
        print(hasil)
        return
    
    # Pilih "0"
    # jumlah_1 tidak berubah
    biner_batas(n, batas, hasil + "0", jumlah_1)
    
    # Pilih "1"
    # jumlah_1 bertambah 1
    biner_batas(n, batas, hasil + "1", jumlah_1 + 1)

# Contoh pemanggilan
biner_batas(4, 2)