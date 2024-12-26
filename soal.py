def g():
    x = 3
    return x

hasil = g()
print(hasil)  # Output: 3

def cekVar(angka):
    if angka % 2 == 0:
        return "genap"
    else:
        return "ganjil"

c = input('masukan angka : ')
try:
    
    cekVarr = int(c)
    hasil = cekVar(cekVarr)
    print(hasil)
except ValueError:
    print("masukan harus angka")

angka = int(input("Masukkan sebuah angka: "))
if angka > 0:
    print("Angka ini adalah bilangan positif.")
elif angka < 0:
    print("Angka ini adalah bilangan negatif.")
else:
    print("Angka ini adalah nol.")
#  no 2

# no 1
angka1=float(input("masukkan bilangan angka1="))
angka2=float(input("masukkan bilangan angka2="))

penjumlahan= angka1 + angka2
pengurangan= angka1 - angka2
pembagian= angka1 / angka2
perkalian= angka1 * angka2

print("hasil dari penjumlahan",penjumlahan)
print("hasil dari pengurangan",pengurangan)
print("hasil dari pembagian",pembagian)
print("hasil dari perkalian",perkalian)

# no 3
angka = int(input("Masukkan sebuah angka: "))
if angka % 2 == 0:
    print("Angka ini adalah bilangan genap.")
else:
    print("Angka ini adalah bilangan ganjil.")

#no 4
kota_list = ["Jakarta", "Surabaya", "Bandung", "Medan", "Yogyakarta"]
for kota in kota_list:
    print("Kota:",(kota))

print()