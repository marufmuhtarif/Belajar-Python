def sapa_nama(nama):
    if nama is None:
        print("Silahkan masukkan nama anda!")
        return
    elif nama == "":
        print("Nama tidak boleh kosong!")
        return
    print(f"Halo {nama}, selamat datang di dunia pemrograman!")

sapa_nama("Ma'ruf")