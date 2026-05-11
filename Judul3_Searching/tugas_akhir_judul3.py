#Tugas Akhir Judul 3
#Nama  : Thariq Ariq Setiawan
#NPM   : 2515061073
#Kelas : PSD-E

# Mengimplementasikan Binary Search menjadi Netflix

def binary_search(film, n, target):
    l = 0
    r = n - 1
    hasil = []

    while l <= r:
        m = l + (r - l) // 2

        print(f"Median: {m}, nilai: {film[m]}")

        if target.lower() in film[m].lower():

            hasil.append((m, film[m]))

            i = m - 1
            while i >= 0:
                if target.lower() in film[i].lower():
                    hasil.append((i, film[i]))
                i -= 1

            i = m + 1
            while i < n:
                if target.lower() in film[i].lower():
                    hasil.append((i, film[i]))
                i += 1

            break

        elif film[m].lower() < target.lower():
            print("Mencari di kanan")
            l = m + 1

        else:
            print("Mencari di kiri")
            r = m - 1

    return hasil


def main():

    film = [
        "12 Angry Man",
        "18x2 Beyond Youthful Days",
        "1917",
        "2001 : a Space Odyssey",
        "2012",
        "28 Days Later",
        "28 Weeks Later",
        "28 Years Later",
        "All Quiet on the Western Front",
        "Always",
        "American Sniper",
        "Andor",
        "Apollo",
        "Arrival",
        "Battle : Los Angeles",
        "Big Fish",
        "Blade Runner 2049",
        "Bridge to Terabithia",
        "Civil War",
        "Cloverfield",
        "Dark Mapple",
        "Dunkirk",
        "Even If This Love Disappear From The World Tonight",
        "Everything Everywhere All at Once",
        "Fantastic Beast",
        "Fantastic Four",
        "Final Destination",
        "First Man",
        "Forget Me Not",
        "Fury",
        "Ghost Rider",
        "God Particle",
        "Gravity",
        "Greyhound",
        "Hacksaw Ridge",
        "Harry Potter",
        "Interstellar",
        "King Arthur",
        "Lilo and Stitch",
        "Megan Leavey",
        "Midway",
        "Narnia",
        "Once We Were Us",
        "Parasite",
        "Peaky Blinders",
        "Project Hail Mary",
        "Rogue One",
        "Saving Private Ryan",
        "Snow White and the Huntsman",
        "Star Wars",
        "Superman",
        "Tenet",
        "Terminator",
        "The Big Four",
        "The Core",
        "The Hobit",
        "The Lord of The Rings",
        "The Martian",
        "The Maze Runner",
        "The Outpost",
        "The Raid",
        "The Truman Show",
        "The World Behind",
        "Top Gun : Maverick",
        "Train to Busan",
        "Warfare",
        "Warhorse",
        "World War Z"
    ]

    n = len(film)

    print("Daftar Film:\n")

    for i in range(n):
        print(f"{i + 1}. {film[i]}")

    target = input("\nMasukkan judul film yang ingin dicari: ")

    hasil = binary_search(film, n, target)

    if len(hasil) > 0:

        print("\nFilm ditemukan:\n")

        for i in range(len(hasil)):
            indeks, judul = hasil[i]
            print(f"{i + 1}. Film '{judul}' ditemukan di indeks ke-{indeks}")

    else:
        print("Film tidak ditemukan")


if __name__ == "__main__":
    main()