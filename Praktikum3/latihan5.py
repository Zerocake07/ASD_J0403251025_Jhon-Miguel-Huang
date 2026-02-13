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

    # Tampilkan list
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")

    # ====== Reverse Linked List ======
    def reverse(self):
        prev = None
        current = self.head

        while current:
            next_node = current.next   # simpan node berikutnya
            current.next = prev       # balik arah pointer
            prev = current            # geser prev
            current = next_node       # geser current

        self.head = prev

ll = LinkedList()
ll.insert_at_end(1)
ll.insert_at_end(2)
ll.insert_at_end(3)
ll.insert_at_end(4)
ll.insert_at_end(5)

print("Linked List sebelum dibalik:")
ll.display()

ll.reverse()

print("Linked List setelah dibalik:")
ll.display()
