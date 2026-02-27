# ==========================================================
# Nama: Jhon Miguel Huang 
# NIM: J0403251025
# Kelas: A/P1
# ==========================================================

#==========================================
#Latihan 3: Mencari Nilai Maksimum
#==========================================\

# Fungsi untuk mencari nilai maksimum dalam list
def cari_maks(data, index=0):
    
    # Base case:
    # Jika index sudah di elemen terakhir
    if index == len(data) - 1:
        return data[index]  # Kembalikan elemen terakhir
    
    # Recursive case:
    # Cari maksimum dari sisa elemen setelah index sekarang
    maks_sisa = cari_maks(data, index + 1)
    
    # Bandingkan elemen sekarang dengan maksimum sisa
    if data[index] > maks_sisa:
        return data[index]   # Jika lebih besar, kembalikan ini
    else:
        return maks_sisa     # Jika tidak, kembalikan maksimum sisa

# List angka
angka = [3, 7, 2, 9, 5]

# Cetak hasil maksimum
print("Nilai maksimum:", cari_maks(angka))