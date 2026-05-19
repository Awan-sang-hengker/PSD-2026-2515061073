#Tugas Akhir Judul 4
#Nama  : Thariq Ariq Setiawan
#NPM   : 2515061073
#Kelas : PSD-E

# Mengimplementasikan Queue Array untuk playlist lagu Setiafy (Spotify but from Temu)


class QueueArray:
    def __init__(self, max_size=100):
        self.MAXN = max_size
        self.q = [None] * self.MAXN
        self.front_idx = -1
        self.rear_idx = -1

    def is_empty(self):
        return self.front_idx == -1

    def is_full(self):
        return (self.rear_idx + 1) % self.MAXN == self.front_idx

    def enqueue(self, x):
        if self.is_full():
            print("Playlist penuh")
            return
        if self.is_empty():
            self.front_idx = 0
            self.rear_idx = 0
        else:
            self.rear_idx = (self.rear_idx + 1) % self.MAXN
        self.q[self.rear_idx] = x
        print(f"Memasukkan lagu {x} berhasil")

    def dequeue(self):
        if self.is_empty():
            print("Playlist kosong")
            return
        print(f"Memutar {self.q[self.front_idx]}")
        if self.front_idx == self.rear_idx:
            self.front_idx = -1
            self.rear_idx = -1
        else:
            self.front_idx = (self.front_idx + 1) % self.MAXN

    def peek(self):
        if self.is_empty():
            print("Playlist kosong")
            return
        print(f"Lagu selanjutnya: {self.q[self.front_idx]}")

    def display(self):
        if self.is_empty():
            print("Playlist kosong")
            return
        print("Isi Playlist (mulai dari lagu  selanjutnya ke belakang):\n ", end="")
        i = self.front_idx
        while True:
            print(self.q[i], end=" ")
            if i == self.rear_idx:
                break
            i = (i + 1) % self.MAXN
        print()

    def clearall(self):
        self.front_idx = -1
        self.rear_idx = -1
        print("Playlist berhasil dikosongkan")

def main():
    queue = QueueArray()
    pilih = 0
    while pilih != 5:
        print("\n=== Playlist lagu Setiafy ===")
        print("1. Memasukkan lagu")
        print("2. Putar lagu selanjutnya")
        print("3. Lihat lagu selanjutnya")
        print("4. Tampilkan isi Playlist")
        print("5. Selesai")
        print("6. Kosongkan Playlist")
        try:
            pilih = int(input("Pilih: "))
        except ValueError:
            print("Input tidak valid!")
            continue
        if pilih == 1:
            try:
                val = str(input("Masukkan lagu: "))
                queue.enqueue(val)
            except ValueError:
                print("Input tidak valid!")
        elif pilih == 2:
            queue.dequeue()
        elif pilih == 3:
            queue.peek()
        elif pilih == 4:
            queue.display()
        elif pilih == 5:
            print("Program selesai.")
        elif pilih == 6:
            queue.clearall()
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()