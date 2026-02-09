#=======================================================
#Praktikum 1: Konsep ADT dan File Handling
#Latihan Dasar 1: Mmebca seluruh isi file data 
#======================================================

print("=====Membuka file dalam satu string=====")
with open("data_mahasiswa.txt", "r", encoding = "utf-8") as file:
    isi_file = file.read()
print(isi_file)

print("Tipe data :", type(isi_file))

#membuka file per baris
print("====Membuka fill perbaris====")
jumlah_baris = 0
with open("data_mahasiswa.txt", "r", encoding = "utf-8") as file:
    for baris in file:
        jumlah_baris =  jumlah_baris + 1
        baris = baris.strip()#menghilangkan karakter baris baru
        print("Baris ke- ", jumlah_baris)
        print("isinya :", baris)


#=======================================================
#Praktikum 1: Konsep ADT dan File Handling
#Latihan Dasar 3: Memnbaca dan menyimpannya ke dalam list 
#======================================================

# Parsing baris menjadi data satuan dan menampilkannya dalam bentuk kolom2 data
with open("data_mahasiswa.txt", "r", encoding = "utf-8") as file:
    for baris in file:
        baris = baris.strip()#menghilangkan karakter baris baru
        nim, nama, nilai = baris.split(",") #pecah menjadi data satuan dan simpan ke variabel
        print("NIM :", nim, "| NAMA :", nama, "| NILAI :", nilai) #menampilkan satuan data dalam bentuk kolom  



data_list = [] #inisialisasi list untuk menampung data  
with open("data_mahasiswa.txt", "r", encoding = "utf-8") as file:
    for baris in file:
        baris = baris.strip()#menghilangkan karakter baris baru
        nim, nama, nilai = baris.split(",") #pecah menjadi data satuan dan simpan ke variabel
        data_list.append([nim,nama,int(nilai)])
print('====Menampilkan list====')
print(data_list)
print("Contoh record pertama", data_list[0])
print("Contoh record kedua", data_list[1])
print("Contoh record kedua", data_list[2])
print("Contoh record kedua", data_list[3])
print("Contoh record kedua", data_list[4])
print("Contoh record kedua", data_list[5])
print("Contoh record kedua", data_list[6])
print("Contoh record kedua", data_list[7])
print("Contoh record kedua", data_list[8])
print("Contoh record kedua", data_list[9])

print("Jumlah record pada list", len(data_list))

#=======================================================
#Praktikum 1: Konsep ADT dan File Handling
#Latihan Dasar 4: Membaca data dan menyimpannya ke struktur data dictionary 
#======================================================


data_dict = {} #INISIALISASI DICTIONARY

with open("data_mahasiswa.txt", "r", encoding = "utf-8") as file:
    for baris in file:
        baris = baris.strip()#menghilangkan karakter baris baru
        nim, nama, nilai = baris.split(",") #pecah menjadi data satuan dan simpan ke variabel
        #simpan data dalam dictionary (key dan value)
        data_dict[nim] = {
            "nama" : nama,
            "nilai" : int(nilai)
        }
print("===menampilkan data dictionary===")
print(data_dict)

        
 
