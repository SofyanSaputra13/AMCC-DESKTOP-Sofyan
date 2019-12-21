# dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
# print ("dict[Name]    : ", dict['Name'])
# print ("dict[Age]     : ", dict['Age'])

# dict['Age'] = 8
# dict ['School'] = "DPS School"
# print ("dict[Age]     : ", dict['Age'])
# print ("dict[School]  : ", dict['School'])

# Membuat Fungsi
def salam():
    print ('Hello, Selamat Pagi !')

# Memanggil Fungsi
salam()  

# Membuat Fungsi Dengan Parameter
def luas_segitiga(alas, tinggi):
   luas = (alas * tinggi) / 2
   print ("Luas Segitiga : %f" %luas)

# Pemanggilan Fungsi
luas_segitiga(4, 6)

# Membuat Variabel Global
nama = 'Salsa'
versi = '1.0.0'

def help():
    # Ini Variabel Lokal
    nama = 'Programku'
    versi = '1.0.2'
    # Mengakses Variabel Lokal
    print ('Nama : %s'%nama)
    print ('Versi : %s'%versi)

# Mengakses Variabel Global
print ('Nama : %s'%nama)
print ('Versi : %s'%versi)

# Memanggil Fungsi help()
help()