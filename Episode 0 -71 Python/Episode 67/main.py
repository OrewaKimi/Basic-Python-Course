import os

if __name__ == "__main__":
    sistem_operasi = os.name
    
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

        user_option = input("Masukkan opsi: ")

        print("\n=========================\n")

        if user_option == "1":
            print("Read Data")
        elif user_option == "2":
            print("Create Data")
        elif user_option == "3":
            print("Update Data")
        elif user_option == "4":
            print("Delete Data")

        print("\n=========================\n")
        is_done = input("Apakah Selesai (y/n)? ")
        if is_done.lower() == "y":
            break

    print("Program Berakhir, Terima Kasih KAKAAAAA")
