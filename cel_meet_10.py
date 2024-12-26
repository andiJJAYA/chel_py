# import sqlite3


# conn = sqlite3.connect('siswa.db')


# cursor = conn.cursor()


# cursor.execute('''
# CREATE TABLE IF NOT EXISTS siswa (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     nama TEXT,
#     usia INTEGER,
#     nilai TEXT
# )
# ''')


# data_siswa = [
#     ("Andi", 20, "A"),
#     ("Budi", 22, "B"),
#     ("Citra", 19, "C")
# ]


# cursor.executemany('INSERT INTO siswa (nama, usia, nilai) VALUES (?, ?, ?)', data_siswa)


# nama_siswa4 = input("Masukkan nama siswa 4: ")
# usia_siswa4 = int(input("Masukkan usia siswa 4: "))
# nilai_siswa4 = "A"  


# cursor.execute('INSERT INTO siswa (nama, usia, nilai) VALUES (?, ?, ?)', (nama_siswa4, usia_siswa4, nilai_siswa4))


# print("Semua data siswa:")
# cursor.execute('SELECT * FROM siswa')
# all_siswa = cursor.fetchall()
# for siswa in all_siswa:
#     print(siswa)


# print("\nData siswa dengan nilai 'A':")
# cursor.execute('SELECT * FROM siswa WHERE nilai = "A"')
# siswa_nilai_A = cursor.fetchall()
# for siswa in siswa_nilai_A:
#     print(siswa)


# print("\nData siswa dengan usia kurang dari 20 tahun:")
# cursor.execute('SELECT * FROM siswa WHERE usia < 20')
# siswa_usia_kurang_20 = cursor.fetchall()
# for siswa in siswa_usia_kurang_20:
#     print(siswa)

# cursor.execute('UPDATE siswa SET nilai = "A+" WHERE nama = "Budi"')


# cursor.execute('DELETE FROM siswa WHERE nama = "Andi"')


# print("\nData siswa setelah menghapus 'Andi':")
# cursor.execute('SELECT * FROM siswa')
# remaining_siswa = cursor.fetchall()
# for siswa in remaining_siswa:
#     print(siswa)


# conn.commit()
# conn.close() 


# conn = sqlite3.connect('siswa.db')


# cursor = conn.cursor()


# cursor.execute('''
# CREATE TABLE IF NOT EXISTS siswa (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     nama TEXT,
#     usia INTEGER,
#     nilai TEXT
# )
# ''')


# data_siswa = [
#     ("Andi", 20, "A"),
#     ("Budi", 22, "B"),
#     ("Citra", 19, "C")
# ]


# cursor.executemany('INSERT INTO siswa (nama, usia, nilai) VALUES (?, ?, ?)', data_siswa)


# nama_siswa4 = input("Masukkan nama siswa 4: ")
# usia_siswa4 = int(input("Masukkan usia siswa 4: "))
# nilai_siswa4 = "A" 


# cursor.execute('INSERT INTO siswa (nama, usia, nilai) VALUES (?, ?, ?)', (nama_siswa4, usia_siswa4, nilai_siswa4))


# print("Semua data siswa:")
# cursor.execute('SELECT * FROM siswa')
# all_siswa = cursor.fetchall()
# for siswa in all_siswa:
#     print(siswa)


# print("\nData siswa dengan nilai 'A':")
# cursor.execute('SELECT * FROM siswa WHERE nilai = "A"')
# siswa_nilai_A = cursor.fetchall()
# for siswa in siswa_nilai_A:
#     print(siswa)


# print("\nData siswa dengan usia kurang dari 20 tahun:")
# cursor.execute('SELECT * FROM siswa WHERE usia < 20')
# siswa_usia_kurang_20 = cursor.fetchall()
# for siswa in siswa_usia_kurang_20:
#     print(siswa)


# cursor.execute('UPDATE siswa SET nilai = "A+" WHERE nama = "Budi"')


# cursor.execute('DELETE FROM siswa WHERE nama = "Andi"')


# print("\nData siswa setelah menghapus 'Andi':")
# cursor.execute('SELECT * FROM siswa')
# remaining_siswa = cursor.fetchall()
# for siswa in remaining_siswa:
#     print(siswa)


# conn.commit()
# conn.close()


import sqlite3

mass = sqlite3.connect('uty.db')
kursor = mass.cursor()
kursor.execute('''
    CREATE TABLE IF NOT EXISTS dosen(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nama VARCHAR(50) NOT NULL ,
        nik INT(10) NOT NULL,
        umur INT (3)   NOT NULL     )
''')
mass.commit()



 
kursor.execute('''
    INSERT INTO dosen (nama,nik, umur) VALUES
               ('widi',123,22),
               ('budi',121,21)
              
''')

mass.commit()

nama = input('masukan nama')
nik = int(input('masukan nik'))
umur = int(input('masukan umur'))

kursor.execute('''
    INSERT INTO dosen (nama, nik,umur)
               VALUES (?, ?,?)
''',(nama,nik,umur)
)

mass.commit()

kursor.execute('''UPDATE dosen SET nama = "Antara" WHERE id = 1''')
mass.commit()

kursor.execute('''DELETE FROM dosen WHERE id = 2''')
mass.commit()

print("Semua data dosen:")
kursor.execute('SELECT * FROM dosen')
for boy in kursor.fetchall():
    print(boy)

mass.close()

