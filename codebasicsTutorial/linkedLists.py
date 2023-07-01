
#defining linkedlist

class Node:
    def __init__(self,data = None,next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None #instance Variable
    
    def insert_at_beginning(self,data):
        node = Node(data,self.head)
        self.head = node

    def insert_at_end(self,data):
        if(self.head == None):
            self.insert_at_beginning(data)
            return
        itr = self.head
        while itr.next != None:
            itr = itr.next
        itr.next = Node(data,None)

    def get_length(self):
        if(self.head == None):
            return 0
        count = 0
        itr = self.head
        while itr:
            count = count + 1
            itr = itr.next
        return count
    
    def print_length(self):
        print("length of LinkedList : ",self.get_length())
    
    def insert_at_loc(self,pos,data):
        count = 1
        itr = self.head
        if pos < 0 or pos > self.get_length():
            raise Exception("Invalid Index")
        if pos == 0:
            self.insert_at_beginning(data)
            
        elif pos == self.get_length():
            self.insert_at_end(data)
            
        else:    
            while itr:
                if(count == pos):
                    break 
                count = count + 1
                itr = itr.next
            itr.next = Node(data,itr.next)
    
    # we just need to update the links no need to manually clear the removed node as it is taken care by the Garbage Collector in python
    def remove_at_begining(self):
        if(self.head == None):
            print("List is empty can't remove anything")
        else:
            self.head = self.head.next

    def remove_at_end(self):
        if(self.head == None):
            print("List is empty can't remove anything")
        else:
            itr = self.head
            while itr.next.next != None:
                itr = itr.next
            itr.next = None

    def remove_at_loc(self,pos):
        count = 1
        itr = self.head
        if(self.head == None):
            print("List is empty can't remove anything")
        if pos < 0 or pos > self.get_length():
            raise Exception("Invalid Index to remove element")
        if pos == 0:
            self.remove_at_begining()
        elif pos == self.get_length():
            self.remove_at_end()
        else:
            while itr:
                if(pos == count):
                    itr.next = itr.next.next
                    break
                itr = itr.next
                count = count + 1

    def print_list(self):
        if(self.head == None):
            print("Linked List is Empty")
            return
        itr = self.head
        listStr = ''
        while itr:
            listStr+=str(itr.data) + ' '
            itr = itr.next

        print("list contains : ",listStr)

if __name__ == '__main__':
    #its a way to store code that should only run when your file is executed as a script
    
    #LL of Integers
    ll = LinkedList()
    ll.insert_at_end(5)
    ll.insert_at_beginning(6)
    ll.insert_at_beginning(8)
    ll.insert_at_end(1)
    ll.insert_at_end(2)
    ll.insert_at_loc(3,9)
    ll.print_list()
    ll.print_length()
    ll.insert_at_loc(ll.get_length(),19)
    ll.insert_at_loc(0,45)
    ll.print_list()
    ll.print_length()
    ll.remove_at_begining()
    ll.remove_at_end()
    ll.remove_at_loc(3)
    ll.print_list()
    ll.print_length()
    #ll.remove_at_loc(67) # this raises exception

    print()
    # LL of Strings
    ls = LinkedList()
    ls.insert_at_beginning("Banana")
    ls.insert_at_end("Grapes")
    ls.insert_at_loc(2,"Mango")
    ls.insert_at_loc(2,"Apple")
    ls.print_list()
    ls.print_length()
    ls.remove_at_begining()
    ls.remove_at_end()
    ls.remove_at_loc(1)
    ls.print_list()
    ls.print_length()
       