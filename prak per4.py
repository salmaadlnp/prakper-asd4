from builtins import input, int
import math

class Skincare:
    def __init__(self, id, nama, jenis, harga, stok):
        self.id = id
        self.nama = nama
        self.jenis = jenis
        self.harga = harga
        self.stok = stok
        self.next = None

class LinkedListSkincare:
    def __init__(self):
        self.head = None

    def tambah_skincare_awal(self, skincare):
        skincare.next = self.head
        self.head = skincare

    def tambah_skincare_akhir(self, skincare):
        if not self.head:
            self.head = skincare
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = skincare

    def tambah_skincare_diantara(self, skincare, id_sebelumnya):
        if not self.head:
            print("Tidak ada skincare tersedia.")
            return
        current = self.head
        while current:
            if current.id == id_sebelumnya:
                skincare.next = current.next
                current.next = skincare
                return
            current = current.next
        print("Skincare dengan ID {} tidak ditemukan.".format(id_sebelumnya))

    def hapus_skincare_awal(self):
        if not self.head:
            print("Tidak ada skincare tersedia.")
            return
        self.head = self.head.next

    def hapus_skincare_akhir(self):
        if not self.head:
            print("Tidak ada skincare tersedia.")
            return
        if not self.head.next:
            self.head = None
            return
        current = self.head
        prev = None
        while current.next:
            prev = current
            current = current.next
        prev.next = None

    def hapus_skincare_diantara(self, id_sebelumnya):
        if not self.head:
            print("Tidak ada skincare tersedia.")
            return
        if self.head.id == id_sebelumnya:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.id == id_sebelumnya:
                current.next = current.next.next
                return
            current = current.next
        print("Skincare dengan ID {} tidak ditemukan.".format(id_sebelumnya))

    def tampilkan_skincare(self):
        current = self.head
        if not current:
            print("Tidak ada skincare tersedia.")
        else:
            print("Daftar Skincare:")
            while current:
                print("ID:", current.id)
                print("Nama:", current.nama)
                print("Jenis:", current.jenis)
                print("Harga:", current.harga)
                print("Stok:", current.stok)
                print("-----------------------")
                current = current.next

    def bubble_sort(self, ascending=True):
        if not self.head or not self.head.next:
            return
        swapped = True
        while swapped:
            swapped = False
            prev = None
            current = self.head
            while current.next:
                if (ascending and current.id > current.next.id) or (not ascending and current.id < current.next.id):
                    if prev:
                        prev.next, current.next.next, current.next = current.next, current, current.next.next
                    else:
                        self.head, current.next.next, current.next = current.next, current, current.next.next
                    swapped = True
                prev, current = current, current.next

    def jump_search(self, search_id):
        if not self.head:
            print("Tidak ada skincare tersedia.")
            return None

        n = 0
        current = self.head
        while current:
            n += 1
            current = current.next

        step = int(math.sqrt(n))
        prev = None
        current = self.head
        while current and current.id < search_id:
            prev = current
            for _ in range(min(step, n)):
                current = current.next
            n -= step

        while prev and prev.id < search_id:
            prev = prev.next

        if prev and prev.id == search_id:
            return prev
        else:
            print("Skincare dengan ID {} tidak ditemukan.".format(search_id))
            return None

if __name__ == "__main__":
    toko = LinkedListSkincare()

    while True:
        print("\nMenu:")
        print("1. Tambah barang di awal")
        print("2. Tambah barang di akhir")
        print("3. Tambah barang di antara node")
        print("4. Hapus barang di awal")
        print("5. Hapus barang di akhir")
        print("6. Hapus barang di antara node")
        print("7. Lihat barang")
        print("8. Sorting Ascending")
        print("9. Sorting Descending")
        print("10. Cari barang")
        print("11. Keluar")

        pilihan = input("Masukkan pilihan Anda: ")

        if pilihan == "1":
            id = int(input("Masukkan ID: "))
            nama = input("Masukkan Nama: ")
            jenis = input("Masukkan Jenis: ")
            harga = int(input("Masukkan Harga: "))
            stok = int(input("Masukkan Stok: "))
            skincare = Skincare(id, nama, jenis, harga, stok)
            toko.tambah_skincare_awal(skincare)
        elif pilihan == "2":
            id = int(input("Masukkan ID: "))
            nama = input("Masukkan Nama: ")
            jenis = input("Masukkan Jenis: ")
            harga = int(input("Masukkan Harga: "))
            stok = int(input("Masukkan Stok: "))
            skincare = Skincare(id, nama, jenis, harga, stok)
            toko.tambah_skincare_akhir(skincare)
        elif pilihan == "3":
            id_sebelumnya = int(input("Masukkan ID sebelumnya: "))
            id = int(input("Masukkan ID: "))
            nama = input("Masukkan Nama: ")
            jenis = input("Masukkan Jenis: ")
            harga = int(input("Masukkan Harga: "))
            stok = int(input("Masukkan Stok: "))
            skincare = Skincare(id, nama, jenis, harga, stok)
            toko.tambah_skincare_diantara(skincare, id_sebelumnya)
        elif pilihan == "6":
            id_sebelumnya = int(input("Masukkan ID sebelumnya: "))
            toko.hapus_skincare_diantara(id_sebelumnya)
        elif pilihan == "7":
            toko.tampilkan_skincare()
        elif pilihan == "8":
            toko.bubble_sort(True)
            print("Sorting Ascending berhasil.")
        elif pilihan == "9":
            toko.bubble_sort(False)
            print("Sorting Descending berhasil.")
        elif pilihan == "10":
            search_id = int(input("Masukkan ID yang ingin dicari: "))
            result = toko.jump_search(search_id)
            if result:
                print("Skincare dengan ID {} ditemukan.".format(search_id))
                print("Detail Skincare:")
                print("ID:", result.id)
                print("Nama:", result.nama)
                print("Jenis:", result.jenis)
                print("Harga:", result.harga)
                print("Stok:", result.stok)
            else:
                print("Skincare dengan ID {} tidak ditemukan.".format(search_id))

