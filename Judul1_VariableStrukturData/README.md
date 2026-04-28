Judul program : Mengimplementasikan Doubly Linked List menjadi Spotify

Program ini adalah simulasi dari alur logika fitur playlist music player (seperti spotify) dengan python yang dibagun menggunakan struktur
data doubly linked list, setiap lagu direpresentasikan sebagai node yang terhubung dua arah (previous dan next). Sehingga bisa memungkinkan 
untuk ke lagu sebelumnya atau lagu setelahnya secara efisien. Di program ini juga memiliki penunjuk khusus yaitu current yang akan menandai 
lagu yang sedang diputar, sehingga fungsi next dan previous bisa bekerja tanpa dicari ulang dari awal playlist.

Untuk secara fungsional, program ini bisa memungkinkan pengguna untuk menambahkan lagu kedalam playlist, menampilkan playlist, dan mengontrol
pemutaran dengan pindah ke lagu sebelumnya atau berikutnya. Dalam program ini, saya belum menambahkan fitur-fitur seperti shuffle karena 
sedikit rumit dan belum saya mengerti bagaimana cara membuatnya. Sekian dan terimakasih.

Source :
<img width="1186" height="4206" alt="tugas_akhir_judul1" src="https://github.com/user-attachments/assets/54c5a75a-f5ae-44c6-a929-9642d8b8cef5" />

1. Mendefinisikan class untuk satu elemen (node) dalam linked list.
2. Untuk inisialisasi Node saat dibuat.
3. Menyimpan data lagu ke dalam node.
4. Pointer ke node sebelumnya.
5. Pointer ke node berikutnya.
6. 
7.
8. Class utama untuk mengelola playlist.
9. Untuk inisialisasi linked list.
10. Pointer ke node pertama.
11. Pointer ke node terakhir.
12. Pointer ke lagu yang sedang diputar.
13. 
14. Untuk membuat node baru.
15. Mengembalikan objek Node berisi lagu.
16. 
17. Cek apakah playlist masih kosong.
18. Set node baru sebagai node pertama.
19. Set node baru sebagai node terakhir.
20. Set node baru sebagai lagu yang sedang diputar.
21. Jika playlist tidak kosong.
22. Node baru menunjuk ke node terakhir sebelumnya.
23. Node terakhir lama menunjuk ke node baru.
24. Update node terakhir ke node baru.
25. 
26. Untuk menampilkan semua lagu.
27. Cek apakah playlist kosong.
28. Tampilkan pesan jika kosong.
29. Keluar dari fungsi.
30. 
31. Mulai traversal dari node pertama.
32. Menampilkan header playlist.
33. Loop selama node masih ada.
34. Cek apakah node ini sedang diputar.
35. Tampilkan lagu dengan tanda khusus.
36. Jika bukan lagu yang diputar.
37. Tampilkan lagu biasa.
38. Pindah ke node berikutnya.
39. 
40. Untuk menampilkan lagu yang sedang diputar.
41. Cek apakah ada lagu aktif.
42. Tampilkan lagu saat ini.
43. Jika tidak ada lagu.
44. Tampilkan pesan kosong.
45. 
46. Untuk pindah ke lagu berikutnya.
47. Cek apakah ada lagu berikutnya.
48. Geser ke node berikutnya.
49. Tampilkan lagu baru.
50. Jika tidak ada lagu berikutnya.
51. Tampilkan pesan.
52. 
53. Untuk pindah ke lagu sebelumnya.
54. Cek apakah ada lagu sebelumnya.
55. Geser ke node sebelumnya.
56. Tampilkan lagu baru.
57. Jika tidak ada lagu sebelumnya.
58. Tampilkan pesan.
59. 
60.
61. Fungsi utama program.
62. Membuat objek playlist.
63. 
64. Loop utama program (menu terus berjalan).
65. Tampilkan judul menu.
66. Opsi tambah lagu.
67. Opsi tampilkan playlist.
68. Opsi play sekarang.
69. Opsi next lagu.
70. Opsi previous lagu.
71. Opsi keluar.
72. 
73. Input pilihan user.
74. 
75. Jika user pilih tambah lagu.
76. Input judul lagu.
77. Buat node baru.
78. Masukkan ke playlist.
79. Konfirmasi ke user.
80. 
81. Panggil fungsi tampil.
82. 
83. Jika pilih play sekarang.
84. Panggil fungsi play.
85. 
86. Jika pilih next lagu.
87. Pindah ke lagu berikutnya.
88. 
89. Jika pilih lagu sebelumnya.
90. Pindah ke lagu sebelumnya.
91. 
92. Jika pilih keluar.
93. Tampilkan pesan selesai.
94. Keluar dari loop.
95. 
96. Jika input tidak valid.
97. Tampilkan error.
98. 
99.
100. Cek apakah file dijalankan langsung.
101. Jalankan fungsi utama.

Output

Setelah di run:
<img width="170" height="152" alt="image" src="https://github.com/user-attachments/assets/cab47de8-e66e-4629-9899-26625bda535e" />

Jika menginputkan 1:
<img width="188" height="26" alt="image" src="https://github.com/user-attachments/assets/7c86d865-1574-48ce-b12a-ec43bd8eba41" />

Jika sudah memasukkan judul lagu:
<img width="278" height="40" alt="image" src="https://github.com/user-attachments/assets/0dee1649-481e-4715-8470-062d3be1e830" />


Jika menginputkan 2:
a. Sebelum diisi lagu
<img width="123" height="25" alt="image" src="https://github.com/user-attachments/assets/525b57c5-de58-452e-a29e-21269d6a6b7b" />

b. Setelah diisi 3 lagu
<img width="282" height="78" alt="image" src="https://github.com/user-attachments/assets/e8220075-7ea3-4c93-8bd9-93c7dcb6bcbe" />


Jika menginputkan 3:
a. Sebelum diisi lagu
<img width="121" height="19" alt="image" src="https://github.com/user-attachments/assets/7f449506-bc75-486a-91d3-ee78ff969a00" />

b. Setelah diisi lagu
<img width="197" height="34" alt="image" src="https://github.com/user-attachments/assets/bdf0bf8a-f050-4133-b5eb-23b74ee3ceac" />


Jika menginputkan 4:
a. Sebelum diisi lagu:
<img width="176" height="23" alt="image" src="https://github.com/user-attachments/assets/fde7b0af-a595-401e-ac52-03e75a0d372a" />

b. Setelah diisi lagu (Lagu Pertama):
<img width="143" height="29" alt="image" src="https://github.com/user-attachments/assets/0efdfb77-6db3-4064-a95b-06c91b7b5e1a" />

c. Setelah diisi lagu (Lagu terakhir):
<img width="170" height="20" alt="image" src="https://github.com/user-attachments/assets/28f3492c-1946-420e-a0f1-c40cb92fe4c1" />


Jika menginputkan 5:
a. Sebelum diisi lagu:
<img width="212" height="21" alt="image" src="https://github.com/user-attachments/assets/c2aaba89-0da7-4ef7-8a34-4a8b9ed77128" />

b. Setelah diisi lagu (Lagu terakhir)
<img width="142" height="27" alt="image" src="https://github.com/user-attachments/assets/3e9a039c-19b2-42dd-8f61-cfb157b1e2ec" />

c. Setelah diisi lagu (Lagu pertama):
<img width="159" height="26" alt="image" src="https://github.com/user-attachments/assets/3a7e7b6a-75eb-45fd-9d9d-e24bec52c803" />


Jika menginputkan 6:
<img width="127" height="20" alt="image" src="https://github.com/user-attachments/assets/a21e0cb0-dea5-4c17-a63e-7d28c2c650e4" />

Jika inputan tidak valid:
<img width="148" height="20" alt="image" src="https://github.com/user-attachments/assets/775767fc-81ac-4f3d-ba60-62fafb4a950a" />

Link youtube:
https://youtu.be/o_SAo3qpmCQ

thumbnail:
<img width="393" height="274" alt="image" src="https://github.com/user-attachments/assets/6bbbca37-2aef-40a1-b213-1747f0e14e20" />
