Judul Program : Mengimplementasikan Binary Search menjadi Netflix

Program ini bertujuan untuk menjalankan algoritma Binary Search menjadi pencarian judul film seperti Netflix.
Dalam program ini ada 68 film katalog film recommended yang bisa dicari menggunakan kata kunci yang tidak 
mengharuskan user menginputkan full judulnya untuk mencari film yang ada. Algoritma Binary Search dipilih 
karena digunakan untuk data yang besar dan juga digunakan pada data yang sudah terurut agar optimal dari segi
algoritma searching.

Cara kerja algoritma Binary Search pada program ini dengan cara menentukan suatu acuan dengan median pada
tengah-tengah data, kemudian jika huruf pada judul film lebih rendah maka pencarian dicari ke kiri, jika lebih 
tinggi maka pencarian ke arah kanan, begitu seterusnya sampai judul film ketemu.

Source :
<img width="1408" height="8482" alt="tugas_akhir_judul3" src="https://github.com/user-attachments/assets/9e3fd277-c0be-47e4-a418-57b3f6cb2d87" />

Penjelasan dalam rumus tertulis :
<img width="830" height="1280" alt="1" src="https://github.com/user-attachments/assets/f61a2010-8887-4743-9347-8d3663a1bfb0" />
<img width="876" height="1280" alt="2" src="https://github.com/user-attachments/assets/289c875b-0ba6-4e6b-8e98-6c0cc689457b" />

1. Mendefinisikan fungsi binary_search dengan parameter film, n, dan target.
2. Variabel 1 diisi 0 sebagai indeks kiri awal pencarian.
3. Variabel r diisi n-1 sebagai indeks kanan awal pencarian.
4. Membuat list kosong hasil untuk menyimpan film yang ditemukan.
5. 
6. Melakukan perulangan selama indeks kiri kurang dari atau sama dengan indeks kanan.
7. Menghitung indeks tengah menggunakan rumus Binary Search.
8. 
9. Menampilkan posisi median dan nilai film pada indeks tengah.
10. 
11. Mengecek apakah input pencarian ada di dalam judul film.
12. 
13. Menambahkan indeks dan judul film yang ditemukan ke dalam list hasil.
14. 
15. Variabel i diisi indeks sebelah kiri dari median.
16. Melakukan perulangan ke kiri selama indeks masih valid.
17. Mengecek apakah target ada di judul film sebelah kiri.
18. Menambahkan film sebelah kiri ke list hasil.
19. Mengurangi nilai i agar bergerak terus ke kiri.
20. 
21. Variabel i diisi indeks sebelah kanan dari median.
22. Melakukan perulangan ke kanan selama indeks masih valid.
23. Mengecek apakah target ada di judul film sebelah kanan.
24. Menambahkan film sebelah kanan ke list hasil.
25. Menambah nilai i agar bergerak terus ke kanan.
26. 
27. Menghentikan perulangan utama jika film sudah ditemukan.
28. 
29. Mengecek apakah nilai film median lebih kecil dari target.
30. Menampilkan pesan pencarian bergerak ke kanan.
31. Menggeser batas kiri ke m+1.
32. 
33. Jika kondisi sebelumnya salah maka masuk ke bagian else.
34. Menampilkan pesan pencarian bergerak ke kiri.
35. Menggeser batas kanan ke m-1.
36. 
37. Mengembalikan list hasil.
38. 
39. 
40. Mendefinisikan fungsi utama.
41. 
42. Membuat list bernama film.

[Line 43 sampai 113 Judul film nya]

114. Menentukan panjang list film dan menyimpannya ke variabel n.
115. 
116. Menampilkan teks "Daftar Film".
117. 
118. Melakukan perulangan untuk menampilkan semua film.
119. Menampilkan nomor urut dan judul film.
120. 
121. Meminta input judul film yang ingin dicari.
122. 
123. Memanggil fungsi binary_search.
124. 
125. Mengecek apakah ada hasil pencarian.
126. 
127. Menampilkan teks "Film ditemukan".
128. 
129. Melakukan perulangan untuk menampilkan hasil pencarian.
130. Mengambil indeks dan judul dari list hasil.
131. Menampilkan nomor, judul film, dan indeks tempat film ditemukan.
132. 
133. Jika hasil kosong maka masuk ke bagian else.
134. Menampilkan pesan "Film tidak ditemukan".
135. 
136. 
137. Mengecek apakah file dijalankan sebagai program utama.
138. Memanggil fungsi utama.

Output

Setelah di run :
<img width="868" height="244" alt="image" src="https://github.com/user-attachments/assets/0a8a1a44-1b10-46bb-aa23-f1f87d70148f" />
<img width="768" height="198" alt="image" src="https://github.com/user-attachments/assets/5e704423-2f29-4284-b353-f5b07a7974f4" />

Jika tidak valid dan judul tidak ada :
<img width="353" height="123" alt="image" src="https://github.com/user-attachments/assets/d145ff8c-fef4-4c19-a9cf-83afffc2a6c6" />

Jika memasukkan kata kunci tidak full judul film :
<img width="369" height="337" alt="image" src="https://github.com/user-attachments/assets/348e1c0b-2b6c-4f56-8124-06efcccb66d6" />

Jika yang dicari full judul film :
<img width="520" height="294" alt="image" src="https://github.com/user-attachments/assets/72103ec7-e711-40ef-b2e6-130af29b8624" />

Link Youtube :

Thumbnail :
