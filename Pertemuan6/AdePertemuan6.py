# daftar_buku = {
# "Buku1" : "Harry Potter",
# "Buku2" : "Percy Jackson",
# "Buku3" : "Twillight"
# }
# print(daftar_buku["Buku1"])
# print(daftar_buku["Buku2"])
# print(daftar_buku["Buku3"])
# print(daftar_buku)

# Biodata = {
# "Nama" : "Aldy Ramadhan Syahputra",
# "NIM" : 2109106079,
# "KRS" : ["Program Web", "Struktur Data", "Basis Data"],
# "Mahasiswa_Aktif" :True,
# "Social Media" : {
#     "Instagram" : "@aldyrmdhns_",
#     "Discord" : "Izanami#6848"
#     "Email"  "adepasiha@gmail.com"
#     }
# }

# print(Biodata["KRS"][1])
# print(Biodata["Social Media"]["Email"])



# games = dict(Sekiro = "Action", Pokemon = "Adventure",
# Valorant = {"nama" : {123 : "informatika"}})
# print(games['Valorant']['nama'][123])




# Games = {
#     "game1" : "pubg mobile"
#     "game2" : "mobile legends"
#     "game3" : {
#         "nama" : "coc",
#         "Ganre" : "srategy"
#     }
# }
# print((Games.get)) 

# Nilai = {
# "Matematika" : 80,
# "B. Indonesia" : 90,
# "B. Inggris" : 81,
# "Kimia" : 78,
# "Fisika" : 80
# }
# #tanpa menggunakan items
# for i in Nilai:
#     print(i)
# print("")
# #menggunakan items
# for i, j in Nilai.items():
#     print(f"Nilai {i} anda adalah {j}")


# Film = {
# "Avenger Endgame" : "Action",
# "Sherlock Holmes" : "Mystery",
# "The Conjuring" : "Horror"
# }
# #Sebelum Ditambah
# print(Film)

# Film["Zombieland"] = "Comedy",
# Film.update({"Hours" : "Thriller"})
# #Setelah Ditambah
# print(Film)

# pengunaan del

# Detelah ditambahkan
# penggunaan del
# del Film['Aveger Endgame']
# print(Film)
# simpan = Film.pop('Hours')
# #Film.clear
# print(Film)
# film["Hours"] = simpan
# print(Film)

# data = {
# "Nama" : "Aldy",
# "Umur" : 19,
# "Jurusan" : "Informatika"
# }
# #Sebelum Dihapus
# print(data)
# cache = data.pop("Nama")
# #Setelah dihapus
# print(data)
# #memanggil data yang telah dihapus pada dictionary
# print(data.get("Nama"))
# #memanggil data yang telah dihapus pada variabel cache
# print(cache)


# print("Jumlah Film = ", len("Film"))

# movies = Film.copy()
# print(movies)
# print("jumlah film = ", len(movies))


# key = "apel", "jeruk", "mangga"
# value = 2
# buah = dict.fromkeys(key, value)
# print(buah)

# Nilai = {
# "Matematika" : 80,
# "B. Indonesia" : 90,
# "B. Inggris" : 81,
# "Kimia" : 78,
# "Fisika" : 80
# }
# #menggunakan keys
# for i in Nilai.keys():
#     print(i)
# print("")
# #menggunakan value
# for i in Nilai.values():
#     print(i)


# Nilai = {
# "Matematika" : 80,
# "B. Indonesia" : 90,
# "B. Inggris" : 81
# }
# #sebelum Setdefault
# print(Nilai)
# print("")
# #menggunakan setdefault
# print("Nilai : ", Nilai.setdefault("Kimia", 70))
# print("")
# #setelah menggunakan setdefault
# print(Nilai)


# Musik = {
# "The Chainsmoker" : ["All we Know", "TheParis"],
# "Alan Walker" : ["Alone", "Lily"],
# "Neffex" : ["Best of Me", "Memories"]
# }
# for i, j in Musik.items():
#     print(f"Musik milik {i} adalah : ")
# for song in j:
#     print(song)
# print("")

# mahasiswa = {
# 101 : {"Nama" : "Aldy", "Umur" : 21},
# 111 : {"Nama" : "Abdul", "Umur" : 18}
# }
# for key, value in mahasiswa.items():
#     print("ID Mahasiswa : ", key)
# for key_a, value_a in value.items():
#     print (key_a, " : ", value_a)
# print("")


# mahasiswa = {
#     "Nama": "ade pasiha",
#     "Umur": 18,
#     "NIM": "2409106109",
#     "Jurusan": "Informatika",
#     "Angkatan": 2024

# }

# def tampilkan_data():
#     for key, value in mahasiswa.items():
#         print(f"{key}: {value}")







# nilai = {
#     "Matematika": 90,
#     "Fisika": 80,
#     "Biologi": 80,
#     "Kimia": 70
# }

# # Menghitung total nilai
# total_nilai = sum(nilai.values())

# # Menghitung rata-rata nilai
# rata_rata_nilai = total_nilai / len(nilai)

# # Menampilkan hasil
# print("Total Nilai:", total_nilai)
# print("Rata-rata Nilai:", rata_rata_nilai)


# mahasiswa = {
#     "nama": "ade",
#     "umur": 20,
#     "nIM": "2409106109",
#     "jurusan": "Informatika",
#     "angkatan": 2024
# }

# print(angkatan)
# angkatan["fakultas"] = input("Masukan fakultas")
# print
