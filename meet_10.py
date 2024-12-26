import sqlite3

a = sqlite3.connect('data.db')
b = a.cursor()


#membuat tabel 
b.execute('''
          create table if not exists users (
          id integer primary key,
          nama text not null,
          umur int not null,
          alamat text not null)
''' )
a.commit()#kegunaan function commit  dalah untuk menyimpan perubahan data yang telah dilakukan ke dalam database. 
 # kegunaan not null adalah untuk menghindari inputan kosong


#inputan dari user unutk menambahkan data
#disini saya menambahkna for loop untuk user input menambahkan data sebanyak 5 kali
for i in range(3):
    nama = input("masukkan nama:")
    umur = int(input("masukkan umur:"))
    alamat = input("masukkan alamat:")
    b.execute('''
        insert into users (nama,umur,alamat) values (?,?,?)''',(nama,umur,alamat))# kenapa harus tanda tanya ? karena itu adalah parameter yang akan diisi oleh user
a.commit()

#update data
b# Periksa data sebelum UPDATE
b.execute('''SELECT * FROM users''')
data = b.fetchall()
print("Data sebelum update:")
for i in data:
    print(i)

# Update data
b.execute('''
    UPDATE users SET nama = CASE
        WHEN id = 1 THEN 'agus'
        WHEN id = 2 THEN 'loli'
    END
    WHERE id IN (1, 2)
''')
a.commit()

# Periksa data setelah UPDATE
b.execute('''SELECT * FROM users''')
data = b.fetchall()
print("Data setelah update:")
for i in data:
    print(i)

#menghapus data
b.execute('''DELETE FROM users WHERE id IN (1, 2)''')
a.commit()
#menapilkan semua data 
b.execute('''select * from users''')
data = b.fetchall()
for i in data:
    print(i)


a.close()
# commit() hanya diperlukan setelah melakukan perubahan (INSERT, UPDATE, DELETE) pada database.