#Tugas Akhir Judul 2
#Nama  : Thariq Ariq Setiawan
#NPM   : 2515061073
#Kelas : PSD-E

# Mengurutkan transaksi penjualan berdasarkan profit tertinggi menggunakan Insertion Sort

def insertion_sort(transaksi, n):
    for i in range(1, n):
        temp = transaksi[i]
        j = i - 1
        

        while j >= 0 and transaksi[j]['profit'] < temp['profit']:
            transaksi[j + 1] = transaksi[j]
            j -= 1
        
        transaksi[j + 1] = temp


def main():
    try:
        n = int(input("Masukkan jumlah transaksi: "))
    except ValueError:
        print("Input tidak valid!")
        return

    transaksi = []

    print("Masukkan data transaksi:")
    for i in range(n):
        print(f"\nTransaksi ke-{i+1}")
        nama = input("Nama transaksi: ")
        
        while True:
            try:
                profit = int(input("Profit: "))
                break
            except ValueError:
                print("Input tidak valid, masukkan angka!")

        transaksi.append({
            'nama': nama,
            'profit': profit
        })

    print("\nData sebelum diurutkan:")
    for t in transaksi:
        print(f"{t['nama']} - Profit: {t['profit']}")

    insertion_sort(transaksi, n)

    print("\nData setelah diurutkan (profit tertinggi):")
    for t in transaksi:
        print(f"{t['nama']} - Profit: {t['profit']}")


if __name__ == "__main__":
    main()