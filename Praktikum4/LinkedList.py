#=====================================================
#Nama   : Jhon Miguel Huang
#NIM    : J0403251025
#Kelas  : P1
#=====================================================

#=====================================================
#Implementasi Dasar: Node pada Linked List
#=====================================================

class Node:
  #Konstruktor yang dijalankan secara otomatis ketika class Node di panggil/diinstantiasi
  def __init__(self, data):
    self.data = data #menyimpan nilai atau data pada list
    self.next = None #pointer ini menunjuk ke note berikutnya (awal=none)

#membuat node dengan instantiasi class node (1)
nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")

#Menghubungkan Node: A - B - C - none (2)
head = nodeA
nodeA.next = nodeB
nodeB.next = nodeC

# Transversal : Menelusuri node dari head sampai ke None (4)
current = head
while current is not  None:
  print(current.data) #menampilkan data pada node saat ini
  current = current.next #pindah ke node berikutnya



#=====================================================
#Implementasi Dasar: Stack 
#=====================================================