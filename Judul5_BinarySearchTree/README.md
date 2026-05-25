Judul Program: Mengimplementasikan Binary Search Tree menjadi WTCS (War Thunder Championship Series) Leaderboard

Program ini bertujuan untuk menjalankan algoritma Binary Search Tree menjadi leaderboard untuk turnamen dari game
War Thunder yang berjudul WTCS atau War Thunder Championship Series. Pada program ini mengubah data acak dengan 
poin dari masing masing tim sebagai acuan yang teratas. Setiap node menyimpan nama tim dan poin tim, lalu data 
disusun berdasarkan besar kecilnya poin. Jika poin lebih kecil maka data disimpan di subtree kiri, sedangkan jika
poin lebih besar disimpan di subtree kanan. Dengan cara ini, proses pencarian, penambahan, dan penghapusan data
dapat dilakukan lebih cepat dibanding pencarian biasa pada list.

Source:

<img width="1462" height="10020" alt="Sc TA PSD 5 rill" src="https://github.com/user-attachments/assets/b8712919-58a8-45cc-abc5-c8df933a37e2" />

1.	Mendefinisikan class TeamNode untuk membuat node BST.
2.	Mendefinisikan constructor init pada class TeamNode.
3.	Parameter nama_tim dan poin digunakan saat membuat node baru.
4.	Menyimpan nama tim ke atribut self.nama_tim.
5.	Menyimpan poin tim ke atribut self.poin.
6.	Child kiri diisi None.
7.	Child kanan diisi None.
8.	 
9.	Mendefinisikan class LeaderboardWarThunder.
10.	Mendefinisikan constructor class leaderboard.
11.	Root BST awalnya kosong (None).
12.	 
13.	Mendefinisikan fungsi insert_node.
14.	Jika root kosong maka membuat node baru.
15.	Membuat object TeamNode.
16.	 
17.	Jika poin lebih kecil dari root.
18.	Masuk ke subtree kiri secara rekursif.
19.	 
20.	Jika poin lebih besar dari root.
21.	Masuk ke subtree kanan secara rekursif.
22.	 
23.	Mengembalikan root setelah insert selesai.
24.	 
25.	Fungsi insert utama.
26.	Root BST diisi hasil insert.
27.	 
28.	Fungsi mencari node terkecil.
29.	Variabel current menunjuk root awal.
30.	 
31.	Perulangan selama node kiri masih ada.
32.	Bergerak terus ke kiri.
33.	 
34.	Mengembalikan node terkecil.
35.	 
36.	Fungsi menghapus node.
37.	Jika root kosong maka return None.
38.	 
39.	Jika poin lebih kecil dari root.
40.	Hapus node di subtree kiri.
41.	 
42.	Jika poin lebih besar dari root.
43.	Hapus node di subtree kanan.
44.	 
45.	Jika poin ditemukan.
46.	Jika node tidak punya child.
47.	Node dihapus dengan return None.
48.	 
49.	Jika hanya child kanan yang ada.
50.	Menggantikan node dengan child kanan.
51.	 
52.	Jika hanya child kiri yang ada.
53.	Menggantikan node dengan child kiri.
54.	 
55.	Jika node punya dua child.
56.	Mencari successor dari subtree kanan.
57.	 
58.	Mengganti poin root dengan poin successor.
59.	Mengganti nama tim root dengan nama successor.
60.	 
61.	Menghapus successor lama.
62.	 
63.	Mengembalikan root setelah delete selesai.
64.	 
65.	Fungsi delete utama.
66.	Root diisi hasil delete.
67.	 
68.	Fungsi menghitung tinggi pohon.
69.	Jika root kosong.
70.	Mengembalikan -1.
71.	 
72.	Menghitung tinggi subtree kiri.
73.	Menghitung tinggi subtree kanan.
74.	 
75.	Mengembalikan tinggi terbesar ditambah 1.
76.	 
77.	Fungsi traversal level-order.
78.	Jika root kosong.
79.	Menampilkan tulisan (kosong).
80.	Keluar dari fungsi.
81.	 
82.	Membuat queue kosong.
83.	Root dimasukkan ke queue.
84.	 
85.	Perulangan selama queue tidak kosong.
86.	Mengambil node paling depan queue.
87.	 
88.	Menampilkan nama tim dan poin.
89.	 
90.	Jika child kiri ada.
91.	Child kiri dimasukkan queue.
92.	 
93.	Jika child kanan ada.
94.	Child kanan dimasukkan queue.
95.	 
96.	Fungsi inorder descending.
97.	Jika root tidak kosong.
98.	Traversal subtree kanan terlebih dahulu.
99.	 
100.	Menampilkan nama tim dan poin.
101.	 
102.	Traversal subtree kiri.
103.	 
104.	Fungsi mencari successor.
105.	Variabel current menunjuk root.
106.	Variabel successor awalnya kosong.
107.	 
108.	Perulangan selama current tidak kosong.
109.	Jika poin lebih kecil dari current.
110.	Current menjadi kandidat successor.
111.	Bergerak ke kiri.
112.	 
113.	Jika poin lebih besar dari current.
114.	Bergerak ke kanan.
115.	 
116.	Jika poin ditemukan.
117.	Menghentikan perulangan.
118.	 
119.	Jika node tidak ditemukan.
120.	Return None dan False.
121.	 
122.	Jika subtree kanan ada.
123.	Successor adalah node terkecil subtree kanan.
124.	 
125.	Jika successor tidak ada.
126.	Return None dan False.
127.	 
128.	Mengembalikan nama tim successor, poin, dan status berhasil.
129.	 
130.	Fungsi mencari predecessor.
131.	Variabel current menunjuk root.
132.	Variabel predecessor awalnya kosong.
133.	 
134.	Perulangan selama current tidak kosong.
135.	Jika poin lebih besar dari current.
136.	Current menjadi kandidat predecessor.
137.	Bergerak ke kanan.
138.	 
139.	Jika poin lebih kecil dari current.
140.	Bergerak ke kiri.
141.	 
142.	Jika poin ditemukan.
143.	Menghentikan perulangan.
144.	 
145.	Jika node tidak ditemukan.
146.	Return None dan False.
147.	 
148.	Jika subtree kiri ada.
149.	Variabel sementara menunjuk subtree kiri.
150.	 
151.	Perulangan selama child kanan masih ada.
152.	Bergerak ke kanan terus.
153.	 
154.	Node terbesar subtree kiri menjadi predecessor.
155.	 
156.	Jika predecessor tidak ada.
157.	Return None dan False.
158.	 
159.	Mengembalikan nama tim predecessor, poin, dan status berhasil.
160.	 
161.	Mendefinisikan fungsi main.
162.	Membuat object leaderboard.
163.	 
164.	Variabel menu awal bernilai 0.
165.	 
166.	Perulangan program selama pilih bukan 7.
167.	Menampilkan judul program.
168.	Menampilkan menu tambah tim.
169.	Menampilkan menu hapus tim.
170.	Menampilkan menu leaderboard.
171.	Menampilkan menu tinggi pohon.
172.	Menampilkan menu successor.
173.	Menampilkan menu predecessor.
174.	Menampilkan menu keluar.
175.	 
176.	Mencoba membaca input menu.
177.	Input diubah menjadi integer.
178.	 
179.	Jika input bukan angka.
180.	Menampilkan pesan error.
181.	Mengulang menu.
182.	 
183.	Jika memilih menu 1.
184.	Mencoba input data tim.
185.	Input nama tim.
186.	Input poin tim.
187.	 
188.	Memasukkan tim ke BST.
189.	 
190.	Menampilkan pesan berhasil.
191.	 
192.	Jika input salah.
193.	Menampilkan pesan error.
194.	 
195.	Jika memilih menu 2.
196.	Mencoba input poin yang dihapus.
197.	 
198.	Menghapus tim dari BST.
199.	 
200.	Menampilkan pesan berhasil.
201.	 
202.	Jika input salah.
203.	Menampilkan pesan error.
204.	 
205.	Jika memilih menu 3.
206.	Menampilkan judul leaderboard.
207.	Menampilkan data secara descending.
208.	 
209.	Jika memilih menu 4.
210.	Menampilkan tinggi BST.
211.	 
212.	Jika memilih menu 5.
213.	Mencoba input poin successor.
214.	 
215.	Memanggil fungsi mencari successor.
216.	Root BST dikirim sebagai parameter.
217.	Poin yang dicari dikirim.
218.	 
219.	Jika successor ditemukan.
220.	Menampilkan data successor.
221.	 
222.	Jika successor tidak ada.
223.	Menampilkan pesan gagal.
224.	 
225.	Jika input salah.
226.	Menampilkan pesan error.
227.	 
228.	Jika memilih menu 6.
229.	Mencoba input poin predecessor.
230.	 
231.	Memanggil fungsi mencari predecessor.
232.	Root BST dikirim sebagai parameter.
233.	Poin yang dicari dikirim.
234.	 
235.	Jika predecessor ditemukan.
236.	Menampilkan data predecessor.
237.	 
238.	Jika predecessor tidak ada.
239.	Menampilkan pesan gagal.
240.	 
241.	Jika input salah.
242.	Menampilkan pesan error.
243.	 
244.	Jika memilih menu 7.
245.	Menampilkan pesan program selesai.
246.	 
247.	Jika menu tidak valid.
248.	Menampilkan pesan error.
249.	 
250.	Mengecek apakah file dijalankan langsung.
251.	Menjalankan fungsi main().

Output

Setelah di run:

<img width="657" height="256" alt="image" src="https://github.com/user-attachments/assets/f9e0e5d7-1991-4eb5-ae9a-8573ea2ce404" />

Jika pilihan tidak valid:

<img width="315" height="86" alt="image" src="https://github.com/user-attachments/assets/5a54612b-dbfa-4861-8eb5-ea5651811d50" />

Jika input tidak valid:

<img width="236" height="40" alt="image" src="https://github.com/user-attachments/assets/60ead2cd-9565-446e-8b5a-0bad53ff6080" />

Pilih 1:

<img width="305" height="71" alt="image" src="https://github.com/user-attachments/assets/86a35949-a243-48ec-abb6-e19c5f57ffec" />

Setelah mengisi nama tim:

<img width="270" height="75" alt="image" src="https://github.com/user-attachments/assets/7dbc9572-dcc8-49be-97d1-0d8fd5cea65d" />

Setelah mengisi poin tim:

<img width="311" height="55" alt="image" src="https://github.com/user-attachments/assets/6e087455-e504-4d7c-93cb-4c71af8e9727" />

Pilih 2:

<img width="255" height="69" alt="image" src="https://github.com/user-attachments/assets/ad9a6166-2e3c-494e-89a7-2d54be048141" />

Setelah mengisi poin yang ingin dihapus:

<img width="360" height="60" alt="image" src="https://github.com/user-attachments/assets/c43bef34-8c5c-4b53-8098-be5664d65082" />



Pilih 3:

<img width="403" height="168" alt="image" src="https://github.com/user-attachments/assets/9090e499-6c0a-4285-9338-1b6076b7b3f6" />

Pilih 4:

<img width="272" height="74" alt="image" src="https://github.com/user-attachments/assets/a45d2092-5ad6-4611-85fb-9efcde8608ca" />

Pilih 5:

<img width="361" height="65" alt="image" src="https://github.com/user-attachments/assets/47ff76f2-9769-4557-ad6c-e705e0e6c74f" />

Setelah isi cari successor dari poin:

<img width="360" height="92" alt="image" src="https://github.com/user-attachments/assets/323c77d4-8bb4-4644-90c6-3863fabf99fd" />

Pilih 6:

<img width="307" height="69" alt="image" src="https://github.com/user-attachments/assets/4e22992b-bbc8-4ec8-aa4a-a5a2d2a11847" />

Setelah isi cari predecessor dari poin:

<img width="389" height="73" alt="image" src="https://github.com/user-attachments/assets/28743367-199d-43f6-9b6b-924d8a8428b9" />

Pilih 7:

<img width="329" height="84" alt="image" src="https://github.com/user-attachments/assets/9f473e80-2ce5-4fa2-8e98-02bc810bcefd" />


Link Youtube:
https://youtu.be/FXOl_HXcKn4

Thumbnail:

<img width="1365" height="740" alt="image" src="https://github.com/user-attachments/assets/dd284521-0f1c-4a6c-a08c-87e3e303f646" />
