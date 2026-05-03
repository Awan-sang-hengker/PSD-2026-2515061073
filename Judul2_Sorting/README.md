Judul Program : Mengurutkan transaksi penjualan berdasarkan profit tertinggi menggunakan Insertion Sort

Program ini bertujuan untuk mengurutkan data transaksi berdasarkan profit tertinggi menggunakan Insertion Sort.
Pengurutan dalam program ini bersifat Descending dikarenakan profit berdasarkan dari profit terbesar hingga
terkecil. Diawal fungsi insertion_sort dengan cara mengambil satu elemen dan diletakkan dalam temp lalu di
bandingkan dengan elemen sebelumnya. Jika menemukan elemen yaang lebih kecil maka data akan digeser ke kanan
sampai ke posisi yang tepat, sehingga hasil akhirnya menjadi profit yang besar hingga ke kecil.

Source :
<img width="1310" height="2268" alt="tugas_akhir_judul2" src="https://github.com/user-attachments/assets/8586d3f4-4c2e-44dd-b351-06b17c7db09c" />

1. Mendefinisikan fungsi insertion_sort dengan parameter transaksi dan n.
2. Melakukan perulangan dari indeks 1 sampai n-1.
3. Menyimpan elemen saat ini ke variabel sementara temp.
4. Menyimpan indeks sebelumnya ke variabel j.
5. 
6. 
7. Memulai loop untuk membandingkan selama indeks valid dan profit lebih kecil dari temp.
8. Menggeser elemen ke kanan jika profit lebih kecil.
9. Mengurangi indeks j untuk terus membandingkan ke kiri.
10.  
11. Menempatkan temp ke posisi yang sesuai setelah pergeseran.
12. 
13. 
14. Mendefinisikan fungsi utama main.
15. Memulai blok try untuk menangani error input.
16. Mengambil input jumlah transaksi dan mengubahnya menjadi integer.
17. Menangkap error jika input bukan angka.
18. Menampilkan pesan error input.
19. Menghentikan program dengan return.
20. 
21. Membuat list kosong transaksi.
22. 
23. Menampilkan pesan untuk mulai input data.
24. Melakukan perulangan sebanyak jumlah transaksi.
25. Menampilkan nomor transaksi yang sedang diinput.
26. Mengambil input nama transaksi.
27. 
28. Memulai loop validasi input profit.
29. Memulai blok try untuk input profit.
30. Mengambil input profit dan mengubah ke integer.
31. Keluar dari loop jika input valid.
32. Menangkap error jika input tidak valid.
33. Menampilkan pesan kesalahan input.
34. 
35. Menambahkan data transaksi ke dalam list sebagai dictionary.
36. Menyimpan nama transaksi.
37. Menyimpan nilai profit.
38. Menutup dictionary.
39. 
40. Menampilkan data sebelum diurutkan.
41. Melakukan iterasi setiap elemen dalam list transaksi.
42. Menampilkan nama dan profit tiap transaksi.
43. 
44. Memanggil fungsi insertion sort untuk mengurutkan data.
45. 
46. Menampilkan data setelah diurutkan.
47. Melakukan iterasi untuk menampilkan hasil akhir.
48. Menampilkan nama dan profit setelah sorting.
49. 
50. 
51. Mengecek apakah file dijalankan sebagai program utama.
52. Jalankan fungsi utama.

