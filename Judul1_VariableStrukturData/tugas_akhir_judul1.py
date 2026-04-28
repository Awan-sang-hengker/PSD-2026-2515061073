#Tugas Akhir Judul 1
#Nama  : Thariq Ariq Setiawan
#NPM   : 2515061073
#Kelas : PSD-E

#Mengimplementasikan Doubly Linked List menjadi Spotify

class Node:
    def __init__(self, lagu):
        self.data = lagu
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.start = None
        self.rear = None
        self.current = None

    def bikin_node(self, lagu):
        return Node(lagu)

    def masuk_node(self, new_node):
        if self.start is None:
            self.start = new_node
            self.rear = new_node
            self.current = new_node
        else:
            new_node.prev = self.rear
            self.rear.next = new_node
            self.rear = new_node

    def tampil_playlist(self):
        if self.start is None:
            print("Playlist kosong")
            return

        temp = self.start
        print("\n=== PLAYLIST ===")
        while temp is not None:
            if temp == self.current:
                print(f"> {temp.data} (sedang diputar)")
            else:
                print(f"- {temp.data}")
            temp = temp.next

    def play_sekarang(self):
        if self.current:
            print(f"\nMemutar: {self.current.data}")
        else:
            print("Tidak ada lagu")

    def next_lagu(self):
        if self.current and self.current.next:
            self.current = self.current.next
            self.play_sekarang()
        else:
            print("Sudah di lagu terakhir")

    def prev_lagu(self):
        if self.current and self.current.prev:
            self.current = self.current.prev
            self.play_sekarang()
        else:
            print("Sudah di lagu pertama")


def main():
    playlist = DoublyLinkedList()

    while True:
        print("\n=== MENU SPOTIFY ===")
        print("1. Tambah lagu")
        print("2. Tampilkan playlist")
        print("3. Putar lagu sekarang")
        print("4. Lagu berikutnya")
        print("5. Lagu sebelumnya")
        print("6. Keluar")

        choice = input("Pilih menu: ")

        if choice == "1":
            song = input("Masukkan judul lagu: ")
            node = playlist.bikin_node(song)
            playlist.masuk_node(node)
            print("Lagu ditambahkan")

        elif choice == "2":
            playlist.tampil_playlist()

        elif choice == "3":
            playlist.play_sekarang()

        elif choice == "4":
            playlist.next_lagu()

        elif choice == "5":
            playlist.prev_lagu()

        elif choice == "6":
            print("Program selesai")
            break

        else:
            print("Pilihan tidak valid")


if __name__ == "__main__":
    main()