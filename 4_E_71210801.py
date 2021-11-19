x = int ( input ("masukkan bilangan 1: " ))
y = int ( input ("masukkan bilangan 2: " ))
z = int ( input ("masukkan bilangan 3: " ))
if x < y and x < z:
    if y < z:
        print("Urutan bilangan dari yang terkecil adalah", x,y,z)
    else:
        print("Urutan bilangan dari yang terkecil adalah", x, z, y)
elif y < x and y < z:
    if x < z:
        print("Urutan bilangan dari yang terkecil adalah", y,x,z)
    else:
        print("Urutan bilangan dari yang terkecil adalah", y,z,x )
else:
    if x < y:
        print("Urutan bilangan dari yang terkecil adalah", z,x,y)
    else:
        print("Urutan bilangan dari yang terkecil adalah", z, y, x)
