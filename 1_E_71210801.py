print ("=" * 4, "Kalkulator Akar dan Pangkat", "=" * 4 )
print (" Pilihan menu : ")
print (" 1. Pangkat 2 ")
print (" 2. Pangkat 3 ")
print (" 3. Akar kuadrat ")

masukkan_menu = input("masukkan menu yang ada pilih : ")

if masukkan_menu == '1':
    z = int(input("masukkan bilangan yang ingin di pangkatkan: "))
    k = z **2 
    print ("Hasil dari pemangkatan bilangan", z, "dengan 2 (Kuadrat) adalah ",k)

elif masukkan_menu == '2':
    z = int(input("masukkan bilangan yang ingin di pangkatkan: "))
    k = z **3 
    print ("Hasil dari pemangkatan bilangan", z, "dengan 3 (Kubik) adalah ",k)

elif masukkan_menu == '3':
    z = int(input("masukkan bilangan yang ingin di pangkatkan: "))
    k = z **(1/2) 
    print ("Hasil akar kuadrat bilangan", z, "adalah",k)
    
    
else:
    print("Pilihan menu yang dimasukkan tidak sesuai")

