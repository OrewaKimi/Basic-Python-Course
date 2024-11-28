from time import time
from . import Database
from .Util import random_string

def update(no_buku, pk, data_add, tahun, judul, penulis):
    data = Database.TEMPLATE.copy()

    data["pk"] = pk
    data["date_add"] = data_add
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):]
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):]
    data["tahun"] = str(tahun)

    data_str = f'{data["pk"]},{data["date_add"]},{data["penulis"]},{data["judul"]},{data["tahun"]}\n'
    
    panjang_data = len(data_str)

    try:
        with open(Database.DB_NAME, 'r+', encoding="utf-8") as file:
            file.seek(panjang_data * (no_buku - 1))
            file.write(data_str)
    except Exception as e:
        print(f"Error dalam update data: {e}")

from time import time, strftime, gmtime  # Tambahkan import strftime dan gmtime

def create(tahun, judul, penulis):
    data = Database.TEMPLATE.copy()

    data["pk"] = random_string(6)
    data["date_add"] = strftime("%Y-%m-%d-%H-%M-%S%z", gmtime())  # Gunakan strftime dan gmtime
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):]
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):]
    data["tahun"] = str(tahun)

    data_str = f'{data["pk"]},{data["date_add"]},{data["penulis"]},{data["judul"]},{data["tahun"]}\n'
    
    try:
        with open(Database.DB_NAME, 'a', encoding="utf-8") as file:
            file.write(data_str)
    except Exception as e:
        print(f"Data sulit ditambahkan: {e}")

def create_first_data():
    penulis = input("Penulis: ")
    judul = input("Judul: ")
    while True:
        try:
            tahun = int(input("Tahun\t: "))
            if len(str(tahun)) == 4:
                break
            else:
                print("Tahun harus angka, silahkan masukkan tahun lagi (yyyy)")    
        except ValueError:
            print("Tahun harus angka, silahkan masukkan tahun lagi (yyyy)")

    data = Database.TEMPLATE.copy()

    data["pk"] = random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z", time.gmtime())
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):]
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):]
    data["tahun"] = str(tahun)

    data_str = f'{data["pk"]},{data["date_add"]},{data["penulis"]},{data["judul"]},{data["tahun"]}\n'
    print(data_str)
    try:
        with open(Database.DB_NAME, 'w', encoding="utf-8") as file:
            file.write(data_str)
    except Exception as e:
        print(f"Udah lah Gagal: {e}")

def read(**kwargs):
    try:
        with open(Database.DB_NAME, 'r') as file:
            content = file.readlines()
            jumlah_buku = len(content)
            if "index" in kwargs:
                index_buku = kwargs["index"] - 1
                if 0 <= index_buku < jumlah_buku:
                    return content[index_buku]
                else:    
                    return False
            else:
                return content
    except Exception as e:
        print(f"Membaca database error: {e}")
        return False
