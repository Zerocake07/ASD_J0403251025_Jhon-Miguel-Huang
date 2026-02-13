# Node untuk Doubly Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

# Class Doubly Linked List
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Tambah data di akhir
    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

    # Fungsi pencarian
    def search(self, key):
        temp = self.head
        posisi = 1

        while temp:
            if temp.data == key:
                print(f"Elemen {key} ditemukan pada posisi ke-{posisi}.")
                return True
            temp = temp.next
            posisi += 1

        print(f"Elemen {key} tidak ditemukan dalam Doubly Linked List.")
        return False

    # Tampilkan data
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")

dll = DoublyLinkedList()

# Input data
data_list = [2, 6, 9, 14, 20]
for data in data_list:
    dll.append(data)

print("Masukkan elemen ke dalam Doubly Linked List:", data_list)

# Input pencarian
key = int(input("Masukkan elemen yang ingin dicari: "))

# Tampilkan & cari
dll.display()
dll.search(key)
