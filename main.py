# %%
# Import numpy library untuk membantu membuat urutan nomor item pada tabel
import numpy as np

# Import pandas library untuk membuat tabel transaksi
import pandas as pd

# Import SQLite library untuk menyimpan data
import sqlite3

# %%
# Untuk membuat tabel awal
'''
conn = sqlite3.connect('transaction_data.db')
cursor = conn.cursor()
query_create_table = """
                        CREATE TABLE shop_transaction(
                            no_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nama_item VARCHAR(255),
                            jumlah_item INT,
                            harga FLOAT,
                            total_harga FLOAT,
                            diskon FLOAT,
                            harga_diskon FLOAT
                        )
                    """

cursor.execute(query_create_table)
conn.close()
'''

# %%
# Fungsi untuk menambahkan data ke db
def insert_to_table(list_data):
    conn = sqlite3.connect('transaction_data.db')
    cursor = conn.cursor()
    query = """
                INSERT INTO shop_transaction(
                    nama_item,
                    jumlah_item,
                    harga,
                    total_harga,
                    diskon,
                    harga_diskon
                    )
                VALUES(
                    :nama_item,
                    :jumlah_item,
                    :harga,
                    :total_harga,
                    :diskon,
                    :harga_diskon
                    )
            """
    cursor.executemany(query, list_data)
    conn.commit()
    conn.close()

# %%
# Buat class
class Transaction:
    # Inisiasi class, buat dictionary kosong untuk menampung item transaksi
    def __init__(self):
        self.ordered_item = dict()

    # Fungsi 1, menambahkan item baru dengan mengisi nama, jumlah, dan harga per item    
    def add_item(self, nama_item, jumlah_item, harga_per_item):
        self.ordered_item[nama_item] = [jumlah_item, harga_per_item]
        print(f"Item yang dibeli adalah: {self.ordered_item}")

    # Fungsi 2, mengubah nama item
    def update_item_name(self, nama_item, update_nama_item):
        self.ordered_item[update_nama_item] = self.ordered_item[nama_item]
        del self.ordered_item[nama_item]
        print("Nama item berhasil diubah.")
        print(f"Item yang dibeli adalah: {self.ordered_item}")

    # Fungsi 3, mengubah jumlah item
    def update_item_qty(self, nama_item, update_jumlah_item):
        self.ordered_item[nama_item][0] = update_jumlah_item
        print("Jumlah item berhasil diubah.")
        print(f"Item yang dibeli adalah: {self.ordered_item}")

    # Fungsi 4, mengubah harga per item
    def update_item_price(self, nama_item, update_harga_item):
        self.ordered_item[nama_item][1] = update_harga_item
        print("Harga item berhasil diubah.")
        print(f"Item yang dibeli adalah: {self.ordered_item}")

    # Fungsi 5, menghapus satu item tertentu
    def delete_item(self, nama_item):
        del self.ordered_item[nama_item]
        print(f"{nama_item} berhasil dihapus.")

    # Fungsi 6, menghapus semua item yang sudah diinput
    def reset_transaction(self):
        self.ordered_item = dict()
        print("Semua item berhasil dihapus.")

    # Fungsi 7, melakukan pengecekan input apakah sudah sesuai dan menampilkan tabel item yang akan dibeli
    def check_order(self):
        self.table_order = pd.DataFrame.from_dict(self.ordered_item, orient="index", columns=["Jumlah Item", "Harga/Item"])
        self.table_order.index.names = ["Nama Item"]
        self.table_order.reset_index(inplace=True)
        self.table_order.index = np.arange(1, len(self.table_order) + 1)
        self.table_order.index.names = ["No"] 

        # Melakukan pengecekan apakah tipe data yang diinput sudah sesuai 
        try:
            for key, value in self.ordered_item.items():
                key = str(key)
                value[0] = int(value[0])
                value[1] = float(value[1])
      
            self.table_order["Total Harga"] = self.table_order["Jumlah Item"] * self.table_order["Harga/Item"]
            print("Pemesanan sudah benar.")
            print(self.table_order)
        except:
            print("Terdapat kesalahan input data. Silakan dicek kembali.")
            print(self.table_order)

    # Fungsi 8, menampilkan total harga yang harus dibayarkan setelah diskon
    def check_out(self):
        try:
            self.table_order['Diskon'] = np.where(self.table_order["Total Harga"]>500000,0.07,np.where(self.table_order["Total Harga"]>300000,0.06,np.where(self.table_order["Total Harga"]>200000,0.05,0.00)))
            self.table_order['Harga Diskon'] = self.table_order['Total Harga'] - (self.table_order['Total Harga'] * self.table_order['Diskon'])
            insert_to_table(self.table_order.values.tolist())
            print(self.table_order)
            print(f"Total Belanja Anda adalah sebesar Rp{self.table_order['Harga Diskon'].sum()}")
        except:
            print("Anda belum melakukan pengecekan item. Silakan gunakan check_order() untuk melakukan pengecekan sebelum menghitung total.")
    

        

# %%
trnsct_123 = Transaction()

# %%
# Test 1
trnsct_123.add_item("Ayam Goreng", 2, 20000)
trnsct_123.add_item("Pasta Gigi", 3, 15000)


# %%
# Test 2
trnsct_123.delete_item("Pasta Gigi")

# %%
# Test 3
trnsct_123.reset_transaction()

# %%
# Test 4
trnsct_123.add_item("Ayam Goreng", 2, 20000)
trnsct_123.add_item("Pasta Gigi", 3, 15000)
trnsct_123.add_item("Mainan Mobil", 1, 200000)
trnsct_123.add_item("Mi Instan", 5, 3000)

trnsct_123.check_order()
trnsct_123.check_out()


