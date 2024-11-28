from . import Operasi

def update_console():
    data_file = Operasi.read()
    while True:
        print("Silahkan pilih nomor buku yang akan diupdate")
        no_buku = int(input("Nomor Buku: "))
        data_buku = Operasi.read(index=no_buku)

        if data_buku:
            break
        else:
            print("Nomor tidak valid, silahkan masukkan lagi")

    data_break = data_buku.split(',')
    if len(data_break) >= 5:
        pk = data_break[0]
        data_add = data_break[1]
        penulis = data_break[2]
        judul = data_break[3]
        tahun = data_break[4][:-1]
    else:
        print("Data tidak lengkap")
        return

    while True:
        # data yang ingin diupdate
        print("\n" + "=" * 100)
        print("Silahkan pilih data apa yang ingin anda ubah")
        print(f"1. Judul\t: {judul:.40}")
        print(f"2. Penulis\t: {penulis:.40}")
        print(f"3. Tahun\t: {tahun:4}")

        # memilih mode untuk update
        user_option = input("Pilih data [1,2,3]: ")
        print("\n" + "=" * 100)
        match user_option:
            case "1":
                judul = input("Judul\t: ")
            case "2":
                penulis = input("Penulis\t: ")
            case "3":
                while True:
                    try:
                        tahun = int(input("Tahun\t: "))
                        if len(str(tahun)) == 4:
                            break
                        else:
                            print("Tahun harus angka, silahkan masukkan tahun lagi (yyyy)")
                    except ValueError:
                        print("Tahun harus angka, silahkan masukkan tahun lagi (yyyy)")
            case _:
                print("Index tidak valid")

        print("Data baru anda")
        print(f"1. Judul\t: {judul:.40}")
        print(f"2. Penulis\t: {penulis:.40}")
        print(f"3. Tahun\t: {tahun:4}")
        is_done = input("Apakah data sudah sesuai(y/n)? ")
        if is_done.lower() == "y":
            break

    Operasi.update(no_buku, pk, data_add, tahun, judul, penulis)


def create_console():
    print("\n\n" + "=" * 100)
    print("Silahkan tambah data buku\n")
    penulis = input("Penulis\t: ")
    judul = input("Judul\t: ")
    while True:
        try:
            tahun = int(input("Tahun\t: "))
            if len(str(tahun)) == 4:
                break
            else:
                print("Tahun harus angka, silahkan masukkan tahun lagi (yyyy)")
        except ValueError:
            print("Tahun harus angka, silahkan masukkan tahun lagi (yyyy)")

    Operasi.create(tahun, judul, penulis)
    print("\nBerikut adalah data baru anda")
    read_console()



def read_console():
    data_file = Operasi.read()
    
    index = "No"
    judul = "Judul"
    penulis = "Penulis"
    tahun = "Tahun"

    # Header
    print("\n" + "=" * 100)
    print(f"{index:4} | {judul:40} | {penulis:40} | {tahun:5}")
    print("-" * 100)
    
    # Data
    for index, data in enumerate(data_file):
        data_break = data.split(",")
        if len(data_break) >= 5:
            pk = data_break[0]
            date_add = data_break[1]
            penulis = data_break[2]
            judul = data_break[3]
            tahun = data_break[4]
            print(f"{index + 1:4} | {judul:.40} | {penulis:.40} | {tahun:4}", end="")
        else:
            print("Data tidak lengkap:", data)
            continue

    # Footer
    print("=" * 100 + "\n")