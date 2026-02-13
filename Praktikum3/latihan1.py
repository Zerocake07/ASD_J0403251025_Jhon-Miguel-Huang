# ====== Class Node ======
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# ====== Class Linked List ======
class LinkedList:
    def __init__(self):
        self.head = None

    # Insert di akhir
    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    # Fungsi hapus node (sesuai soal)
    def delete_node(self, key):
        temp = self.head

        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return

        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:
            print("Data tidak ditemukan")
            return

        prev.next = temp.next
        temp = None

    # Tampilkan data
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# ===== main program =====
ll = LinkedList()

# Contoh Data
ll.insert_at_end(10)
ll.insert_at_end(20)
ll.insert_at_end(30)
ll.insert_at_end(40)
ll.insert_at_end(50)

print("Sebelum dihapus:")
ll.display()
# Hapus nilai tertentu
ll.delete_node(10)
print("Sesudah dihapus:")
ll.display()
