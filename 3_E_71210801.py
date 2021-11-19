daftar = str(input("Masukkan daftar siswa: "))
daftar_nama=[]
kata_depan_besar=daftar.title()
daftar_nama.append(kata_depan_besar)
print("Daftar Siswa : ",daftar_nama)
masuk_siswa_ditambah=str(input("Masukkan siswa yang ingin ditambahkan :"));
sinta= 'SINTA'
nama = 12
kata_besar= masuk_siswa_ditambah.upper()
kata_depan_besar=daftar.title()
if kata_besar == sinta:
    print("Siswa atas nama",kata_besar,"sudah berada dalam daftar siswa")

elif nama == 12:
    daftar_nama=[]
    daftar_nama.append(kata_depan_besar)
    daftar_nama.append(kata_besar)
    print("Hasil penambahan pada daftar siswa : ",daftar_nama)
      
