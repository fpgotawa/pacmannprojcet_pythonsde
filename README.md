# Python Project - Sekolah Data Pacmann

### Background

Dalam rencana melakukan ekspansi bisnis, diperlukan suatu sistem kasir yang bersifat self-service. Dengan sistem ini diharapkan customer dapat langsung memasukkan item yang akan dibeli beserta jumlah dan harga per itemnya serta fitur lainnya yang diperlukan. Diharapkan melalui project ini dapat dibuat fitur-fitur terkait agar sistem self-service di supermarket dapat berjalan dengan lancar.

### Objective

* Customer dapat menambahkan nama item, jumlah item, dan harga item.
* Customer dapat melakukan perbaikan apabila terdapat kesalahan input nama item, jumlah item, maupun harga item.
* Customer dapat menghapus sebagian atau seluruh item.
* Customer dapat mengecek daftar belanja yang telah diinput.
* Customer dapat menghitung total belanja yang sudah dibeli dengan ketentuan diskon tertentu.

### Flow

<img src="picture\flow.png" width="1000">

##### 1. Membuat ID Transaksi

Customer membuat ID transaksi dengan membuat objek dari class misalnya trnsct_123 = Transaction()

##### 2. Memasukkan Nama, Jumlah, dan Harga Item

Customer memasukkan nama item, jumlah item, dan harga dari item

##### 3. Melakukan pengecekan item

Customer melakukan pengecekan item yang sudah diinput. Customer memastikan bahwa data dari item yang dimasukkan sudah tepat.

##### 4. Memperbaiki dan/atau Menghapus Item

Setelah dilakukan pengecekan, dalam hal terdapat kesalahan, customer dapat memperbaiki nama, jumlah maupun harga dari item. Customer juga dapat menghapus item yang tidak diinginkan atau menghapus seluruh item.

##### 5. Menghitung Total Harga

Setelah seluruh item belanja sudah tepat, customer dapat menghitung total harga yang perlu dibayarkan sesuai ketentuan diskon pada supermarket yaitu:
* Jika total harga per item diatas Rp 200.000 maka akan mendapatkan diskon 5%
* Jika total harga per item diatas Rp 300.000 maka akan mendapatkan diskon 6%
* Jika total harga per item diatas Rp 500.000 maka akan mendapatkan diskon 7%

### Feature

1. Inisiasi Class

<img src="picture\init.png" width="500">

Melakukan inisiasi class dan membuat dictionary kosong untuk menampung item belanja. Dilakukan dengan set variabel pada class Transaction(). Contohnya:

trnsct_123 = Transaction()

2. add_item(nama_item, jumlah_item, harga_per_item)

<img src="picture\add_item.png" width="500">

Menambahkan item yang ingin dibeli. Dilakukan dengan memasukkan parameter nama_item, jumlah_item, dan harga_per_item dengan ketentuan sebagai berikut:

* nama_item berupa string berisi nama item yang akan dibeli, misalnya "Ayam Goreng"
* jumlah_item berupa integer berisi jumlah item yang akan dibeli, misalnya 2
* harga_per_item berupa float berisi harga dari item yang akan dibeli, misalnya 20000.0. Bisa juga berupa integer misalnya 20000.

Contoh:
trnsct_123.add_item("Ayam Goreng", 2, 20000)

3. update_item_name(nama_item, update_nama_item)

<img src="picture\update_item_name.png" width="500">

Mengubah nama item yang sudah diinput. Dilakukan dengan memasukkan parameter nama_item, dan update_nama_item dengan ketentuan sebagai berikut:

* nama_item berupa string berisi nama item yang akan diubah namanya, misalnya "Ayam Goreng"
* update_nama_item berupa string berisi nama item yang baru, misalnya "Ikan Goreng"

Contoh:
trnsct_123.update_item_name("Ayam Goreng", "Ikan Goreng")

4. update_item_qty(nama_item, update_jumlah_item)

<img src="picture\update_item_qty.png" width="500">

Mengubah jumlah item yang sudah diinput. Dilakukan dengan memasukkan parameter nama_item, dan update_jumlah_item dengan ketentuan sebagai berikut:

* nama_item berupa string berisi nama item yang akan diubah jumlahnya, misalnya "Ayam Goreng"
* update_jumlah_item berupa integer berisi jumlah item yang baru, misalnya 5

Contoh:
trnsct_123.update_item_qty("Ayam Goreng", 5)

5. update_item_price(nama_item, update_harga_item)

<img src="picture\update_item_price.png" width="500">

Mengubah harga item yang sudah diinput. Dilakukan dengan memasukkan parameter nama_item, dan update_harga_item dengan ketentuan sebagai berikut:

* nama_item berupa string berisi nama item yang akan diubah harganya, misalnya "Ayam Goreng"
* update_harga_item berupa integer atau float berisi harga item yang baru, misalnya 30000

Contoh:
trnsct_123.update_item_price("Ayam Goreng", 30000)

6. delete_item(nama_item)

<img src="picture\delete_item.png" width="500">

Menghapus item yang sudah diinput. Dilakukan dengan memasukkan parameter nama_item dengan ketentuan berupa string berisi nama item yang akan dihapus, misalnya "Ayam Goreng"

Contoh:
trnsct_123.delete_item("Ayam Goreng")

7. reset_transaction()

<img src="picture\reset_transaction.png" width="500">

Menghapus seluruh item yang sudah diinput

8. check_order()

<img src="picture\check_order.png" width="500">

Menampilkan daftar belanja yang sudah diinput sekaligus mengecek apakah data yang diinput sudah tepat

9. check_out()

<img src="picture\check_out.png" width="500">

Menampilkan total harga dari seluruh daftar belanja yang sudah diinput sekaligus menampilkan diskon yang didapat

### Test Case

**Test 1**

Customer ingin menambahkan dua item baru menggunakan method add_item(). Item yang ingin ditambahkan adalah:
* Nama Item: Ayam Goreng, Qty: 2, Harga: 20000
* Nama Item: Pasta Gigi, Qty: 3, Harga: 15000

Input:

<img src="picture\test1q.png" width="500">

Output:

<img src="picture\test1a.png" width="500">

**Test 2**

Ternyata customer salah membeli salah satu item dari belanjaan yang sudah ditambahkan, maka customer menggunakan method delete_item() untuk menghapus item. Item yang ingin dihapuskan adalah Pasta Gigi

Input:

<img src="picture\test2q.png" width="500">

Output:

<img src="picture\test2a.png" width="500">

**Test 3**

Ternyata setelah dipikir-pikir customer salah memasukkan item yang ingin dibelanjakan. Daripada menghapusnya satu-satu, maka Customer cukup menggunakan method reset_transaction() untuk menghapus semua item yang sudah ditambahkan

Input:

<img src="picture\test3q.png" width="500">

Output:

<img src="picture\test3a.png" width="500">

**Test 4**

Setelah customer selesai berbelanja, akan menghitung total belanja yang harus dibayarkan menggunakan method check_out(). Sebelum mengeluarkan output total belanja akan menampilkan item-item yang dibeli.

Input:

<img src="picture\test4q.png" width="500">

Output:

<img src="picture\test4a.png" width="500">

### Conclusion

Melalui project ini, fitur dasar untuk self-service supermarket sesuai yang tercantum pada requirement sudah terpenuhi. Customer dapat menambahkan, memperbaiki, dan menghapus item yang akan dibeli. Customer juga dapat melakukan cek order atas item yang akan dibeli. Customer juga dapat menghitung total dengan diskon sesuai ketentuan.

Tentunya project ini masih dapat disempurnakan lagi dengan fitur-fitur yang lebih baik. Adapun contoh fitur yang dapat dikembangkan antara lain:
* Pengecekan data input ketika awal melakukan input sehingga kesalahan dapat diminimalisir
