# # Aplikasi To-Do List Sederhana
# # Berikut adalah contoh aplikasi sederhana menggunakan Python 
# # yang tidak memerlukan database. Aplikasi ini adalah
# # "To-Do List" yang memungkinkan pengguna untuk menambahkan,
# # menampilkan, dan menghapus tugas.

# def tampilkan_tugas(tugas):
#     if not tugas:
#         print("Tidak ada tugas dalam daftar.")
#     else:
#         print("\nDaftar Tugas:")
#         for i, tugas_item in enumerate(tugas, start=1):
#             print(f"{i}. {tugas_item}")

# def main():
#     tugas = []
#     while True:
#         print("\nPilih opsi:")
#         print("1. Tambah Tugas")
#         print("2. Tampilkan Tugas")
#         print("3. Hapus Tugas")
#         print("4. Keluar")

#         pilihan = input("Masukkan pilihan (1/2/3/4): ")

#         if pilihan == '1':
#             tugas_item = input("Masukkan tugas: ")
#             tugas.append(tugas_item)
#             print(f"Tugas '{tugas_item}' telah ditambahkan.")
#         elif pilihan == '2':
#             tampilkan_tugas(tugas)
#         elif pilihan == '3':
#             tampilkan_tugas(tugas)
#             if tugas:
#                 index = int(input("Masukkan nomor tugas yang ingin dihapus: ")) - 1
#                 if 0 <= index < len(tugas):
#                     removed = tugas.pop(index)
#                     print(f"Tugas '{removed}' telah dihapus.")
#                 else:
#                     print("Nomor tugas tidak valid.")
#         elif pilihan == '4':
#             print("Terima kasih! Sampai jumpa.")
#             break
#         else:
#             print("Pilihan tidak valid. Silakan coba lagi.")

# if __name__ == "__main__":
#     main()





# # Berikut adalah contoh aplikasi rekursi sederhana dalam 
# # Python yang menghitung faktorial dari sebuah bilangan bulat
def faktorial(a):
    # Basis: jika a adalah 0 atau 1, kembalikan 1
    if a == 0 or a == 1:
        return 1
    else:
        # Rekursi: a * faktorial(a-1)
        return a * faktorial(a - 1)

# Input dari pengguna
angka = int(input("Masukkan angka untuk menghitung faktorial: "))

# Memastikan input valid
if angka < 0:
    print("Faktorial tidak didefinisikan untuk bilangan negatif.")
else:
    hasil = faktorial(angka)
    print(f"Faktorial dari {angka} adalah {hasil}.")




