# ==========================================================
# Nama: Jhon Miguel Huang 
# NIM: J0403251025
# Kelas: A/P1
# ==========================================================

# ==========================================================
# Contoh Rekursi 1: Faktorial
# ==========================================================

# Fungsi untuk menghitung faktorial dari n
def faktorial(n):
    # Base case: kondisi berhenti
    # Jika n == 0, maka faktorial(0) = 1
    if n == 0:
        return 1
    
    # Recursive case:
    # n * faktorial(n - 1)
    # Artinya fungsi memanggil dirinya sendiri
    # dengan nilai yang lebih kecil (n-1)
    return n * faktorial(n - 1)

# Memanggil fungsi faktorial dengan nilai 5
print(faktorial(5))  # Output: 120
