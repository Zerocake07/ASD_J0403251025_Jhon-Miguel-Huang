# ==========================================================
# Nama: Jhon Miguel Huang 
# NIM: J0403251025
# Kelas: A/P1
# ==========================================================

#==========================================
#Latihan 1: Rekursi Pangkat
#==========================================

def pangkat(a, n): #mendefenisikan fungsi sebagai pangkat dan terdapat parameter a, n
  #base case
  if n == 0: #mengecek pangkat apakah bernilai 0
    return 1 #0 = 1
  #Recursive case
  return a * pangkat(a, n - 1)#Mengalikan a dengan hasil fungsi pangkat yang akan di panggil ulang dengan n dikurangi 1
print(pangkat(2, 4)) #memanggil angka 2,4 untuk di jalankan pangkat

