Judul Program:

Source:

Mendefinisikan kelas SlotState.
Mendefinisikan konstanta EMPTY bernilai 0 (slot kosong).
Mendefinisikan konstanta OCCUPIED bernilai 1 (slot terisi).
Mendefinisikan konstanta DELETED bernilai 2 (slot pernah diisi lalu dihapus).
Mendefinisikan kelas Entry.
Mendefinisikan konstruktor init().
Menginisialisasi item_id dengan None.
Menginisialisasi item_name dengan None.
Menginisialisasi quantity dengan 0.
Mengatur status awal slot menjadi EMPTY.
Mendefinisikan kelas MinecraftInventory.
Mendefinisikan konstruktor init(size=10).
Menyimpan ukuran inventory ke self.SIZE.
Membuat tabel berisi objek Entry sebanyak SIZE.
Mendefinisikan fungsi hash.
Mengembalikan hasil item_id % SIZE.
Mendefinisikan fungsi add_item().
Menentukan indeks awal menggunakan fungsi hash.
Menyimpan posisi slot terhapus pertama dengan nilai awal -1.
Melakukan probing sebanyak ukuran tabel.
Menghitung indeks yang sedang diperiksa.
Mengecek apakah slot sedang terisi (OCCUPIED).
Mengecek apakah item_id sudah ada.
Menambahkan jumlah item jika item sudah ada.
Mengembalikan True karena berhasil.
Mengecek apakah slot berstatus DELETED.
Mengecek apakah belum ada slot terhapus yang dicatat.
Menyimpan indeks slot terhapus pertama.
Menangani kondisi slot kosong (EMPTY).
Mengecek apakah pernah ditemukan slot DELETED.
Menggunakan slot DELETED tersebut.
Menyimpan item_id ke slot.
Menyimpan nama item ke slot.
Menyimpan jumlah item ke slot.
Mengubah status slot menjadi OCCUPIED.
Mengembalikan True karena berhasil menambah item.
Mengembalikan False jika tabel penuh.
Mendefinisikan fungsi search_item().
Menghitung indeks awal menggunakan hash.
Melakukan probing pada tabel.
Menghitung indeks yang diperiksa.
Mengecek apakah slot kosong.
Mengembalikan None karena item tidak ditemukan.
Awal kondisi pencarian item.
Mengecek apakah slot terisi.
Mengecek apakah item_id sesuai.
Akhir kondisi.
Mengembalikan objek item yang ditemukan.
Mengembalikan None jika item tidak ada.
Mendefinisikan fungsi remove_item().
Mencari item berdasarkan item_id.
Mengecek apakah item tidak ditemukan.
Mengembalikan False.
Mengubah status item menjadi DELETED.
Mengembalikan True karena berhasil dihapus.
Mendefinisikan fungsi display_inventory().
Menampilkan judul inventory.
Melakukan perulangan seluruh slot.
Menampilkan nomor slot.
Mengecek apakah slot kosong.
Menampilkan teks "Kosong".
Mengecek apakah slot berstatus DELETED.
Menampilkan teks "Item Dihapus".
Menangani kondisi slot berisi item.
Memulai pemanggilan print() multi-baris.
Menampilkan nama item.
Menampilkan jumlah item.
Menutup pemanggilan print().
Mendefinisikan fungsi main().
Membuat objek MinecraftInventory.
Menambahkan item Dirt sebanyak 64.
Menambahkan item Stone sebanyak 32.
Menambahkan item Diamond sebanyak 5.
Menambahkan item Oak Wood sebanyak 20.
Menampilkan isi inventory.
Mencari item dengan ID 21.
Mengecek apakah item ditemukan.
Memulai print() multi-baris.
Menampilkan teks "Item ditemukan:".
Menampilkan nama dan jumlah item.
Menutup print().
Menghapus item dengan ID 11.
Menampilkan teks setelah Stone dihapus.
Menampilkan inventory kembali.
Mencari lagi item dengan ID 21.
Mengecek apakah Diamond masih ditemukan.
Memulai print() multi-baris.
Menampilkan teks "Diamond masih ada:".
Menampilkan jumlah Diamond yang tersisa.
Menutup print().
Mengecek apakah file dijalankan langsung sebagai program utama.
Memanggil fungsi main().
Output

Setelah di run:
