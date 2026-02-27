# ==========================================================
# Nama: Jhon Miguel Huang 
# NIM: J0403251025
# Kelas: A/P1
# ==========================================================

# ==========================================================
# Studi Kasus: Generator PIN
# ==========================================================

# Fungsi untuk membuat kombinasi PIN dengan panjang tertentu
def buat_pin(panjang, hasil=""):
    
    # Base case:
    # Jika panjang PIN sudah sesuai
    if len(hasil) == panjang:
        print("PIN:", hasil)  # Cetak PIN
        return                # Hentikan cabang
    
    # Loop untuk memilih angka
    for angka in ["0", "1", "2"]:
        
        # Tambahkan angka ke hasil lalu lanjut rekursi
        buat_pin(panjang, hasil + angka)

# Membuat PIN sepanjang 3 digit
buat_pin(3)