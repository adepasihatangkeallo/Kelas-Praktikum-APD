cuaca = "mendung"

if cuaca == "mendung":
      print("diam di rumah")
else:
      print("hari ini mendung")




Umur = int(input("masukan nama anda: "))
if Umur > 0:
    if Umur <= 10:
       print(" umur anda termasuk anak anak")
    elif Umur <= 18:
       print(" umur anda termasuk kategori remaja")
    elif Umur <=35:
       print(" umur Anda termasuk kategori dewasa")
    elif Umur <=65:
       print(" umur Anda termasuk kategori paruh baya")
    else:
        print(" umur Anda termasuk kategori Tua")
else:
        print(" Umur Anda Termasuk Kategori Tua")              

nim =int(input("Masukan Nim"))


if nim >= 1 and nim <= 45 :
    if nim >= 1 and nim <= 22 :
        print("Kelas A'1")
    else :
        print("Kelas A'2")
elif nim >= 51 and nim <= 100:
    if nim >= 51 and nim <= 75:
        print("Kelas B'1")
    else :
        print("Kelas B'2")
elif nim >= 101 and nim <= 121:
    if nim >= 46 and nim <= 90:
        print("Kelas C'1")
    else :
        print("Kelas C'2") 
else :
    print("Anda Bukan Mahasiswa Informatika 24" )




angka = int(input("Masukkan angka: "))
result = "Genap" if angka % 2 == 0 else "Ganjil"
print(angka, "adalah angka",result)


nim = int(int("masukan nim: "))
hasil = "Kelas A" if nim >= 1 and nim <=50 else "kelas B" if nim >= 51 and nim <= 100 else "Kelas C" if nim >= 101 and nim <= 121 else "mahasiswa siluman"
print("NIM", nim, " anda anak",hasil)