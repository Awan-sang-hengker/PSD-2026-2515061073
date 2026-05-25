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











Link Youtube:

Thumbnail:
