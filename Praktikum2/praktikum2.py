# =======================================================
# Praktikum 2: Konsep ADT dan File Handling (STUDI KASUS)
# Latihan 1: Membuat Fungsi Load Data
# =======================================================

#VARIABEL MENYIMPAN DATA FILE
nama_file = "data_mahasiswa.txt"

def baca_data(nama_file):
    data_dict = {} #INISIALISASI DATA DICTIONARY
    with open(nama_file, "r", encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip() #AMBIL DATA PER BARIS DAN HILANGKAN NEW LINE
            nim, nama, nilai = baris.split(",") #AMBIL DATA PER ITEM
            data_dict[nim] = {"nama": nama, "nilai": int(nilai)} #MASUKKAN DALAM DICTIONARY
    return data_dict

# =======================================================
# Praktikum 2: Konsep ADT dan File Handling (STUDI KASUS)
# Latihan 2: Membuat Fungsi Menampilkan Data
# =======================================================

def tampilkan_data(data_dict):
    #MEMBUAT HEADER TABEL
    print("\n======= DAFTAR MAHASISWA ========")
    print(f"{'NIM' : <10} | {'Nama' : <12} | {'Nilai' : >5}")
    '''
    untuk tampilan yang rapi, atur lebar kolom
    {'NIM' : <10} artinya nim rata kiri dengan lebar kolom 10 karakter
    {'Nama' : <12} artinya nim rata kiri dengan lebar kolom 12 karakter
    {'Nilai' : >5} artinya nim rata kanan dengan lebar kolom 5 karakter
    '''
    print("-"*33) #MEMBUAT GARIS

    #MENAMPILKAN ISI DATANYA
    for nim in sorted(data_dict.keys()):
        nama = data_dict[nim]["nama"]
        nilai = data_dict[nim]["nilai"]
        print(f"{nim : <10} | {nama : <12} | {int(nilai) : >5}")

# =======================================================
# Praktikum 2: Konsep ADT dan File Handling (STUDI KASUS)
# Latihan 3: Membuat Fungsi Mencari Data
# =======================================================

#MEMBUAT FUNGSI PENCARIAN DATA
def cari_data(data_dict):
    #PENCARIAN DATA BERDASARKAN NIM SEBAGAI KEY DICTIONARY
    #MEMBUAT INPUT NIM MAHASISWA YANG AKAN DICARI
    nim_cari = input("Masukkan NIM mahasiswa yang ingin dicari: ").strip()

    if nim_cari in data_dict:
        nama = data_dict[nim_cari]["nama"]
        nilai = data_dict[nim_cari]["nilai"]
        
        print("===== DATA MAHASISWA DITEMUKAN =====")
        print(f"NIM     : {nim_cari}")
        print(f"Nama    : {nama}")
        print(f"Nilai   : {nilai}")
    else:
        print("Data tidak ditemukan. Pastikan NIM yang dimasukkan benar")

# =======================================================
# Praktikum 2: Konsep ADT dan File Handling (STUDI KASUS)
# Latihan 4: Membuat Fungsi Update Data
# =======================================================

#MEMBUAT FUNGSI UPDATE DATA
def ubah_data(data_dict):
    #AWALI DENGAN MENCARI NIM / DATA MAHASISWA YANG INGIN DI UPDATE
    nim = input("Masukkan NIM mahasiswa yang ingin diubah datanya: ").strip()

    if nim not in data_dict:
        print("NIM tidak ditemukan. Update dibatalkan")
        return
    
    try:
        nilai_baru = int(input("Masukkan nilai baru 0-100: ").strip())
    except ValueError:
        print("Nilai harus berupa angka. Update dibatalkan")

    if nilai_baru < 0 or nilai_baru > 100:
        print("Nilai harus antara 0 sampai 100. Update Dibatalkan")

    nilai_lama = data_dict[nim]["nilai"]
    data_dict[nim]["nilai"] = nilai_baru

    print(f"Update Berhasil. Nilai {nim} berubah dari {nilai_lama} menjadi {nilai_baru}")

# =======================================================
# Praktikum 2: Konsep ADT dan File Handling (STUDI KASUS)
# Latihan 5: Membuat Fungsi Menyimpan Data pada File
# =======================================================

#MEMBUAT FUNGSI MENYIMPAN DATA KE FILE
def simpan_data(nama_file, data_dict):
    with open(nama_file, "w", encoding="utf-8") as file:
        for nim in sorted(data_dict.keys()):
            nama = data_dict[nim]["nama"]
            nilai = data_dict[nim]["nilai"]
            file.write(f"{nim},{nama},{nilai}\n")

# =======================================================
# Praktikum 2: Konsep ADT dan File Handling (STUDI KASUS)
# Latihan 6: Membuat Menu Interaktif
# =======================================================

def main():
    #LOAD DATA OTOMATIS SAAT PROGRAM DIMULAI
    buka_data = baca_data(nama_file) #MEMANGGIL FUNGSI LOAD DATA DAN MENYIMPAN DALAM VARIABEL

    while True:
        print("=== MENU DATA MAHASISWA ===")
        print("1. Tampilkan Data Mahasiswa")
        print("2. Cari Data Berdasarkan NIM")
        print("3. Ubah Nilai Mahasiswa")
        print("4. Simpan Data ke File")
        print("0. Keluar")

        pilihan = input("Pilih Menu: ").strip()
        
        if pilihan == "1":
            tampilkan_data(buka_data)
        elif pilihan == "2":
            cari_data(buka_data)
        elif pilihan == "3":
            ubah_data(buka_data)
        elif pilihan == "4":
            simpan_data(nama_file, buka_data)
            print("Data Berhasil Disimpan")
        elif pilihan == "0":
            print("Program selesai")
            break
        else:
            print("Pilihan tidak valid. Silahkan coba lagi.")

if __name__ == "__main__":
    main()