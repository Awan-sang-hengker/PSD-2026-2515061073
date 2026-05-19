Judul Program: Mengimplementasikan Queue Array untuk playlist lagu Setiafy (Spotify but from Temu)

Program ini bertujuan untuk menjalankan algoritma Queue Array menjadi fitur antrian lagu dalam Setiafy (kw nya spotify).
Penggunaan Queue Array digunakan karena seperti dengan prinsip nya FIFO (First In First Out) yang cocok untuk membuat
antrian. Cara kerja Queue Array pada program ini adalah dengan cara Enqueue data dari belakang kemudian jika Dequeue
dari depan sesuai urutan dari masuknya.

Source :
<img width="1602" height="3978" alt="source TA PSD 5" src="https://github.com/user-attachments/assets/5b40b7e4-0735-4c67-bf1d-50309367fa2d" />

1. Mendefinisikan class QueueArray sebagai implementasi struktur data Queue menggunakan array.
2. Mendefinisikan method constructor __init__ yang akan dijalankan saat objek dibuat.
3. Parameter max_size=100 menentukan ukuran maksimum queue, default bernilai 100.
4. Menyimpan ukuran maksimum queue ke variabel self.MAXN.
5. Membuat list/array q berisi None sebanyak ukuran maksimum queue.
6. Menginisialisasi indeks depan (front_idx) dengan -1 sebagai tanda queue kosong.
7. Menginisialisasi indeks belakang (rear_idx) dengan -1 sebagai tanda queue kosong.
8. 
9. Mendefinisikan method is_empty untuk mengecek apakah queue kosong.
10. Mengembalikan nilai True jika front_idx == -1, berarti queue kosong.
11. 
12. Mendefinisikan method is_full untuk mengecek apakah queue penuh.
13. Mengecek apakah posisi belakang berikutnya sama dengan posisi depan menggunakan circular queue.
14. 
15. Mendefinisikan method enqueue untuk menambahkan data ke queue.
16. Mengecek apakah queue penuh dengan memanggil is_full().
17. Jika queue penuh, tampilkan pesan "Playlist penuh".
18. Menghentikan proses penambahan data menggunakan return.
19. Mengecek apakah queue kosong dengan memanggil is_empty().
20. Jika queue kosong, indeks depan diatur menjadi 0.
21. Jika queue kosong, indeks belakang juga diatur menjadi 0.
22. Jika queue tidak kosong, masuk ke blok else.
23. Memindahkan indeks belakang satu langkah maju menggunakan konsep circular queue.
24. Menyimpan data x pada posisi indeks belakang queue.
25. Menampilkan pesan bahwa lagu berhasil dimasukkan.
26. 
27. Mendefinisikan method dequeue untuk menghapus atau memutar lagu dari queue.
28. Mengecek apakah queue kosong.
29. Jika queue kosong, tampilkan pesan "Playlist kosong".
30. Menghentikan proses dequeue menggunakan return.
31. Menampilkan lagu yang berada di posisi depan queue.
32. Mengecek apakah queue hanya memiliki satu elemen.
33. Jika hanya satu elemen, indeks depan direset menjadi -1.
34. Indeks belakang juga direset menjadi -1.
35. Jika elemen lebih dari satu, masuk ke blok else.
36. Memindahkan indeks depan satu langkah maju menggunakan circular queue.
37. 
38. Mendefinisikan method peek untuk melihat elemen paling depan tanpa menghapusnya.
39. Mengecek apakah queue kosong.
40. Jika queue kosong, tampilkan pesan "Playlist kosong".
41. Menghentikan proses menggunakan return.
42. Menampilkan lagu yang berada di posisi depan queue.
43.
44. Mendefinisikan method display untuk menampilkan seluruh isi queue.
45. Mengecek apakah queue kosong.
46. Jika queue kosong, tampilkan pesan "Playlist kosong".
47. Menghentikan proses menggunakan return.
48. Menampilkan teks judul isi playlist.
49. Menginisialisasi variabel i dengan posisi indeks depan queue.
50. Memulai perulangan tak terbatas menggunakan while True.
51. Menampilkan elemen queue pada indeks i.
52. Mengecek apakah indeks saat ini sama dengan indeks belakang.
53. Jika sama, perulangan dihentikan menggunakan break.
54. Memindahkan indeks i satu langkah maju secara circular.
55. Mencetak baris baru setelah semua isi queue ditampilkan.
56. 
57. Mendefinisikan method clearall untuk mengosongkan queue.
58. Mengatur indeks depan menjadi -1 untuk menandakan queue kosong.
59. Mengatur indeks belakang menjadi -1.
60. Menampilkan pesan bahwa playlist berhasil dikosongkan.
61. 
62. Mendefinisikan fungsi main sebagai program utama.
63. Membuat objek queue dari class QueueArray.
64. Menginisialisasi variabel pilih dengan nilai 0.
65. Memulai perulangan selama pilih tidak sama dengan 5.
66. Menampilkan judul menu program.
67. Menampilkan menu pilihan nomor 1.
68. Menampilkan menu pilihan nomor 2.
69. Menampilkan menu pilihan nomor 3.
70. Menampilkan menu pilihan nomor 4.
71. Menampilkan menu pilihan nomor 5.
72. Menampilkan menu pilihan nomor 6.
73. Memulai blok try untuk menangani error input.
74. Meminta input pilihan menu dari pengguna lalu mengubahnya menjadi integer.
75. Menangkap error ValueError jika input bukan angka.
76. Menampilkan pesan "Input tidak valid!".
77. Melanjutkan perulangan menggunakan continue.
78. Mengecek apakah pengguna memilih menu 1.
79. Memulai blok try untuk input lagu.
80. Meminta input nama lagu dari pengguna.
81. Menambahkan lagu ke queue menggunakan method enqueue.
82. Menangkap error ValueError.
83. Menampilkan pesan "Input tidak valid!".
84. Mengecek apakah pengguna memilih menu 2.
85. Menjalankan method dequeue untuk memutar lagu berikutnya.
86. Mengecek apakah pengguna memilih menu 3.
87. Menjalankan method peek untuk melihat lagu berikutnya.
88. Mengecek apakah pengguna memilih menu 4.
89. Menjalankan method display untuk menampilkan isi playlist.
90. Mengecek apakah pengguna memilih menu 5.
91. Menampilkan pesan "Program selesai.".
92. Mengecek apakah pengguna memilih menu 6.
93. Menjalankan method clearall untuk mengosongkan playlist.
94. Jika pilihan tidak sesuai menu, masuk ke blok else.
95. Menampilkan pesan "Pilihan tidak valid!".
96. 
97. Mengecek apakah file dijalankan langsung sebagai program utama.
98. Menjalankan fungsi main().

