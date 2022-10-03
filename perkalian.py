print("aplikasi table perkalian 1 sampai 12")

while True:
    try:
        angka = int(input("Menampilkan tabel perkalian dari: ")) #INPUTAN BUAT MENGISI ANGKA
        for i in range(1,13): # LOOPING I UNTUK MENENTUKAN ANGKA RANGE/SETARA 1,12
            print(angka,'x',i,'=',angka*i) # TERIMA INPUTAN ANGKA DIKALI 1 SAMPAI 12 = MISAL HASIL INPUT 10 MAKA 10 X 1 SAMPAI 10 X 12
    except:
        print('inputan tidak di terima mungkin kosong atau input selain angka')
        continue
    else:
        print('thanks bro')
        break
        