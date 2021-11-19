suhu_tubuh = float(input ("masukkan suhu tubuh anda: "))
if suhu_tubuh < 32:
    print("Anda kedinginan! Silahkan cari sesuatu yang hangat ")
elif suhu_tubuh >= 32 and suhu_tubuh <= 37.5:
    print(" Suhu Anda normal")
elif suhu_tubuh > 37.5 and suhu_tubuh <= 50:
    print("Anda demam! jangan berpergian ke fasilitas Umum")
else:
    print ("Anda bukan Manusia :) ")
