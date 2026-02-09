# =======================================================
# Praktikum 2: Konsep ADT dan File Handling (STUDI KASUS)
# Studi Kasus: Sistem Stok Barang Kantin
# =======================================================

nama_file = "stok_barang.txt"

# =======================================================
# Fungsi Load Data
# =======================================================
def baca_data(nama_file):
    data_dict = {}
    with open(nama_file, "r", encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip()
            kode, nama, stok = baris.split(",")
            data_dict[kode] = {"nama": nama, "stok": int(stok)}
    return data_dict

# =======================================================
# Fungsi Menampilkan Data
# =======================================================
def tampilkan_data(data_dict):
    print("\n======= DATA STOK BARANG =======")
    print(f"{'Kode' : <8} | {'Nama Barang' : <15} | {'Stok' : >5}")
    print("-"*36)
    for kode in sorted(data_dict.keys()):
        nama = data_dict[kode]["nama"]
        stok = data_dict[kode]["stok"]
        print(f"{kode : <8} | {nama : <15} | {stok : >5}")

# =======================================================
# Fungsi Cari Data
# =======================================================
def cari_data(data_dict):
    kode = input("Masukkan kode barang: ").strip()
    if kode in data_dict:
        print("=== DATA DITEMUKAN ===")
        print(f"Kode  : {kode}")
        print(f"Nama  : {data_dict[kode]['nama']}")
        print(f"Stok  : {data_dict[kode]['stok']}")
    else:
        print("Barang tidak ditemukan")

# =======================================================
# Fungsi Tambah Barang
# =======================================================
def tambah_barang(data_dict):
    kode = input("Masukkan kode barang baru: ").strip()
    if kode in data_dict:
        print("Kode sudah digunakan")
        return
    nama = input("Masukkan nama barang: ").strip()
    try:
        stok = int(input("Masukkan stok awal: ").strip())
    except ValueError:
        print("Stok harus berupa angka")
        return
    data_dict[kode] = {"nama": nama, "stok": stok}
    print("Barang berhasil ditambahkan")

# =======================================================
# Fungsi Update Stok
# =======================================================
def update_stok(data_dict):
    kode = input("Masukkan kode barang: ").strip()
    if kode not in data_dict:
        print("Barang tidak ditemukan")
        return

    print("1. Tambah stok")
    print("2. Kurangi stok")
    pilih = input("Pilih menu: ").strip()

    try:
        jumlah = int(input("Masukkan jumlah: ").strip())
    except ValueError:
        print("Jumlah harus angka")
        return

    if pilih == "1":
        data_dict[kode]["stok"] += jumlah
        print("Stok berhasil ditambahkan")
    elif pilih == "2":
        if data_dict[kode]["stok"] - jumlah < 0:
            print("Stok tidak boleh negatif")
        else:
            data_dict[kode]["stok"] -= jumlah
            print("Stok berhasil dikurangi")
    else:
        print("Pilihan tidak valid")

# =======================================================
# Fungsi Simpan Data
# =======================================================
def simpan_data(nama_file, data_dict):
    with open(nama_file, "w", encoding="utf-8") as file:
        for kode in sorted(data_dict.keys()):
            nama = data_dict[kode]["nama"]
            stok = data_dict[kode]["stok"]
            file.write(f"{kode},{nama},{stok}\n")

# =======================================================
# Menu Utama
# =======================================================
def main():
    data = baca_data(nama_file)

    while True:
        print("\n=== MENU STOK BARANG KANTIN ===")
        print("1. Tampilkan Data Stok")
        print("2. Cari Barang")
        print("3. Tambah Barang")
        print("4. Update Stok")
        print("5. Simpan Data ke File")
        print("0. Keluar")

        pilih = input("Pilih Menu: ").strip()

        if pilih == "1":
            tampilkan_data(data)
        elif pilih == "2":
            cari_data(data)
        elif pilih == "3":
            tambah_barang(data)
        elif pilih == "4":
            update_stok(data)
        elif pilih == "5":
            simpan_data(nama_file, data)
            print("Data berhasil disimpan")
        elif pilih == "0":
            print("Program selesai")
            break
        else:
            print("Pilihan tidak valid")

if __name__ == "__main__":
    main()
