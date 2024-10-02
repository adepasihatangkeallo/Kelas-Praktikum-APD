# nama = ["shandy",106,True,
#         3.96[123,"ADE",False,3.66],
#         "rehan"]
# print = (nama[4][2])

# matkul = ["APD",
#           "APL",
#             "WEB",
#             "JARKOM",
#             "srukdat",
#             "basdat",
#             "pti",
#             "kalkulus",
#             "probas"]

# print(matkul)[1]


# makanan = ["Bakso","Sate","soto","nasi goreng","mie ayam","ayam bakar"]
# print("Sebelum: ")
# print(makanan)
# # makanan.append("Nasi goreng")
# print("sesudah: ")
# makanan.clear
# print(makanan)
# del(makanan[5])
# data = makanan.pop(5)
# print(makanan)
# print(data)
# makanan.insert(2,"nasi goreng")
# makanan[0] = ["ayam","bebek"]
# print(makanan)

# minuman = ["jasjus","pos es","cendol","josu","es tesh","air kelapa"]
# print("sebelum")
# print(minuman)
# del minuman[2]
# print("sesudah")
# print(minuman)
# minuman[4] = "air putih"
# minuman.insert(0,"jus tomat")
# # print(minuman)


# makanan = ["ayam","ikan",["bakso","sate","sote","ikan","bebek"],["teh","kopi","air"]]

# for i in makanan :
#     if isinstance(i, list): 
#         for j in i : 
#             print(j)
#     else:
#          print(i)






akuns = []

while True:
    print("Halo! selamat datang di aplikasi Catatan")
    print("silahkan pilih 'daftar akun' jika belum buat akun,dan jika sudah memiliki akun silahkan 'login'")
    print("1. daftar Akun")
    print("Login")
    print("3 exit")
    print('_________________________')
    opsi = input("opsi: ")
    print(" ")

    if opsi == "1":
        print("Halo Penguna baru! Ayo Buat Akun dulu")
    username = input("Username: ")
    akuna = False
    for akun in akuns:
        if akun[0] == username: # Memeriksa apakah username sudah ada
            akuna = True
            break
    
    if akuna:
        print("nama sudah terpakai untuk registrasi silahkan coba lagi")
    else:
        password = input("Password")
        akuns.append([username, password, []] )
print(f"Akun anda berhasil terdaftar dengan ID: {username}")

         