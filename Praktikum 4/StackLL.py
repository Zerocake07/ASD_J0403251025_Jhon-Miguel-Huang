#=====================================================
#Nama   : Jhon Miguel Huang
#NIM    : J0403251025
#Kelas  : P1
#=====================================================

#=====================================================
#Implementasi Dasar: Stack
#=====================================================

class Node:
  #Konstruktor yang dijalankan secara otomatis ketika class Node di panggil/diinstantiasi
  def __init__(self, data):
    self.data = data #menyimpan nilai atau data pada list
    self.next = None #pointer ini menunjuk ke note berikutnya (awal=none)
  
#Stack ada operasi push(memasukkan head baru) dan pop (menghapus head)

class stack:
  def __init__(self):
    self.top = None #top menunjuk ke node paling atas(awalnya kosong)
    
  def push(self,data): #memamsukkan data baru pada stack
    #membuat node baru (1)
    nodeBaru = Node(data) #instantiasi/memanggil konstruktor pada class Node

    #node baru harus menunduk ke top yang lama (head lama) (2)
    nodeBaru.next = self.top

    #geser top ke node baru (3)
    self.top = nodeBaru
  
  def is_empty(self):
    return self.top is None #stack kosong jika top = None
  
  def pop(self): #mengambil / menghapus node paling atas (top/head)
    if self.is_empty():
      print("Stack kosong, tidak bisa pop")
      return None
    data_terhapus = self.top.data #soroti bagian top dan simpan di variabell
    self.top = self.top.next #geser top ke node berikutnya
    return data_terhapus 
  
  def peek(self):
    #melihat data yang paling atas tanpa menghapus
    if self.is_empty(): 
      return None
    return self.top.data

  def tampilkan(self):
    current = self.top
    print("Top" , end=" -> ")
    while current is not None:
      print(current.data, end=" -> ")
      current = current.next
    print("None")

#instantiasi class stack
s = stack()
s.push("A")
s.push("B")
s.push("C")
s.tampilkan()
print("Peek (Lihat Top): ", s.peek())
s.pop()
s.tampilkan()
print("Peek (Lihat Top): ", s.peek())
