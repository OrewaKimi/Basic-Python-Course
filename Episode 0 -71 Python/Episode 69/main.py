import os
import CRUD as CRUD

if __name__ == "__main__":
    sistem_operasi = os.name

    if sistem_operasi == "posix":
        os.system("clear")
    elif sistem_operasi == "nt":
        os.system("cls")

    print("SELAMAT DATANG DI PROGRAM")
    print("DATABASE PERPUSTAKAAN")
    print("=========================")

    # check database itu ada atau tidak
    CRUD.init_console()

    while True:
        if sistem_operasi == "posix":
            os.system("clear")
        elif sistem_operasi == "nt":
            os.system("cls")
        
        print("SELAMAT DATANG DI PROGRAM")
        print("DATABASE PERPUSTAKAAN")
        print("=========================")

        print(f"1. Read Data")
        print(f"2. Create Data")
        print(f"3. Update Data")
        print(f"4. Delete Data\n")

        user_option = input("Masukan opsi: ")

        if user_option == "1":
            CRUD.read_console()
        elif user_option == "2":
            CRUD.create_console()
        elif user_option == "3":
            print("Update Data")
        elif user_option == "4":
            print("Delete Data")

        is_done = input("Apakah Selesai (y/n)? ")
        if is_done.lower() == "y":
            break

    print("Program Berakhir, Terima Kasih KAKAAAAA")
