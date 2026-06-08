Judul Program: Mengimplementasikan Hash Map untuk Inventory Minecraft dengan Open Addressing

Program ini merupakan simulasi inventory Minecraft yang menerapkan struktur data Hash Map 
dengan metode Open Addressing (Linear Probing). Program memungkinkan pengguna untuk 
menambahkan, mencari, menghapus, dan menampilkan item dalam inventaris berdasarkan ID item. 
Untuk mengatasi collision, program menggunakan teknik Linear Probing dengan memeriksa slot 
berikutnya hingga ditemukan slot yang sesuai. Setiap slot memiliki status kosong, terisi, 
atau dihapus, sehingga pengelolaan data inventaris dapat dilakukan secara efisien.

Source:

<img width="1216" height="5042" alt="tugas_akhir_judul6" src="https://github.com/user-attachments/assets/dc088749-3182-4783-a5a9-c3130ced6216" />

1.	Mendefinisikan kelas SlotState.
2.	Mendefinisikan konstanta EMPTY bernilai 0 (slot kosong).
3.	Mendefinisikan konstanta OCCUPIED bernilai 1 (slot terisi).
4.	Mendefinisikan konstanta DELETED bernilai 2 (slot pernah diisi lalu dihapus).
5.	 
6.	Mendefinisikan kelas Entry.
7.	Mendefinisikan konstruktor __init__().
8.	Menginisialisasi item_id dengan None.
9.	Menginisialisasi item_name dengan None.
10.	Menginisialisasi quantity dengan   0.
11.	Mengatur status awal slot menjadi EMPTY.
12.	 
13.	Mendefinisikan kelas MinecraftInventory.
14.	Mendefinisikan konstruktor __init__(size=10).
15.	Menyimpan ukuran inventory ke self.SIZE.
16.	Membuat tabel berisi objek Entry sebanyak SIZE.
17.	 
18.	Mendefinisikan fungsi hash.
19.	Mengembalikan hasil item_id % SIZE.
20.	 
21.	Mendefinisikan fungsi add_item().
22.	Menentukan indeks awal menggunakan fungsi hash.
23.	Menyimpan posisi slot terhapus pertama dengan nilai awal -1.
24.	 
25.	Melakukan probing sebanyak ukuran tabel.
26.	Menghitung indeks yang sedang diperiksa.
27.	 
28.	Mengecek apakah slot sedang terisi (OCCUPIED).
29.	Mengecek apakah item_id sudah ada.
30.	Menambahkan jumlah item jika item sudah ada.
31.	Mengembalikan True karena berhasil.
32.	 
33.	Mengecek apakah slot berstatus DELETED.
34.	Mengecek apakah belum ada slot terhapus yang dicatat.
35.	Menyimpan indeks slot terhapus pertama.
36.	 
37.	Menangani kondisi slot kosong (EMPTY).
38.	Mengecek apakah pernah ditemukan slot DELETED.
39.	Menggunakan slot DELETED tersebut.
40.	 
41.	Menyimpan item_id ke slot.
42.	Menyimpan nama item ke slot.
43.	Menyimpan jumlah item ke slot.
44.	Mengubah status slot menjadi OCCUPIED.
45.	Mengembalikan True karena berhasil menambah item.
46.	 
47.	Mengembalikan False jika tabel penuh.
48.	 
49.	Mendefinisikan fungsi search_item().
50.	Menghitung indeks awal menggunakan hash.
51.	 
52.	Melakukan probing pada tabel.
53.	Menghitung indeks yang diperiksa.
54.	 
55.	Mengecek apakah slot kosong.
56.	Mengembalikan None karena item tidak ditemukan.
57.	 
58.	Awal kondisi pencarian item.
59.	Mengecek apakah slot terisi.
60.	Mengecek apakah item_id sesuai.
61.	Akhir kondisi.
62.	Mengembalikan objek item yang ditemukan.
63.	 
64.	Mengembalikan None jika item tidak ada.
65.	 
66.	Mendefinisikan fungsi remove_item().
67.	Mencari item berdasarkan item_id.
68.	 
69.	Mengecek apakah item tidak ditemukan.
70.	Mengembalikan False.
71.	 
72.	Mengubah status item menjadi DELETED.
73.	Mengembalikan True karena berhasil dihapus.
74.	 
75.	Mendefinisikan fungsi display_inventory().
76.	Menampilkan judul inventory.
77.	 
78.	Melakukan perulangan seluruh slot.
79.	Menampilkan nomor slot.
80.	 
81.	Mengecek apakah slot kosong.
82.	Menampilkan teks "Kosong".
83.	 
84.	Mengecek apakah slot berstatus DELETED.
85.	Menampilkan teks "Item Dihapus".
86.	 
87.	Menangani kondisi slot berisi item.
88.	Memulai pemanggilan print() multi-baris.
89.	Menampilkan nama item.
90.	Menampilkan jumlah item.
91.	Menutup pemanggilan print().
92.	 
93.	Mendefinisikan fungsi main().
94.	Membuat objek MinecraftInventory.
95.	 
96.	Menambahkan item Dirt sebanyak 64.
97.	Menambahkan item Stone sebanyak 32.
98.	Menambahkan item Diamond sebanyak 5.
99.	Menambahkan item Oak Wood sebanyak 20.
100.	 
101.	Menampilkan isi inventory.
102.	 
103.	Mencari item dengan ID 21.
104.	 
105.	Mengecek apakah item ditemukan.
106.	Memulai print() multi-baris.
107.	Menampilkan teks "Item ditemukan:".
108.	Menampilkan nama dan jumlah item.
109.	Menutup print().
110.	 
111.	Menghapus item dengan ID 11.
112.	 
113.	Menampilkan teks setelah Stone dihapus.
114.	Menampilkan inventory kembali.
115.	 
116.	Mencari lagi item dengan ID 21.
117.	 
118.	Mengecek apakah Diamond masih ditemukan.
119.	Memulai print() multi-baris.
120.	Menampilkan teks "Diamond masih ada:".
121.	Menampilkan jumlah Diamond yang tersisa.
122.	Menutup print().
123.	 
124.	Mengecek apakah file dijalankan langsung sebagai program utama.
125.	Memanggil fungsi main().

Output

Setelah di run:

<img width="1340" height="879" alt="image" src="https://github.com/user-attachments/assets/236a3883-ef68-48d2-9539-69fdaf3db9f0" />

Link Youtube:


Thumbnail:

<img width="683" height="384" alt="Thumnail Judul 6" src="https://github.com/user-attachments/assets/5609e2b5-559a-4f86-b959-03fe38b02020" />
