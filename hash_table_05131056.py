from Crypto.Hash import MD5

class ListNode:
     
     def __init__(self,val):
          self.val = val
          self.next = None

class MyHashSet:
     
     def __init__(self,capacity=5):
          self.capacity = capacity
          self.data = [None]*capacity

     def add(self,key):
          h = MD5.new()
          h.update(key.encode("utf-8"))
          value = int(h.hexdigest(),16)
          pos = value%self.capacity
          if self.data[pos] == None:
               self.data[pos] = ListNode(value)
          else:
               self.add2(self.data[pos],value)
     def add2(self,node,key_int):
          if node.next:
               if node.val == key_int:
                    return
               else:
                    self.add2(node.next,key_int)
          else:
               node.next = ListNode(key_int)

     def contains(self,key):
          h = MD5.new()
          h.update(key.encode("utf-8"))
          value = int(h.hexdigest(),16)
          pos = value%self.capacity
          node = self.data[pos]
          while node:
               if node.val == value:
                    return True
               node = node.next
          return False

     def remove(self,key):
          h = MD5.new()
          h.update(key.encode("utf-8"))
          value = int(h.hexdigest(),16)
          pos = value%self.capacity
          if self.data[pos]:
               self.remove2(self.data[pos],value)
               if self.data[pos].val == value:
                    self.data[pos] = self.data[pos].next
     def remove2(self,node,key_int):
          if node.next:
               if node.next.val == key_int:
                    node.next = node.next.next
                    self.remove2(node,key_int)
               else:
                    self.remove2(node.next,key_int)
'''
#擺入字串
print("擺入a,b,c,d")
a=MyHashSet(capacity=2)
a.add('a')
a.add('b')
a.add('c')
a.add('d')
#確認是否存在
print("b存在:",a.contains('b')==True)
print("e存在:",a.contains('e')==True)
#刪除
a.remove('b')
print("刪除b後，b存在:",a.contains('b')==True)
'''
'''
擺入a,b,c,d
b存在: True
e存在: False
刪除b後，b存在: False
'''
#參考資料:自己
