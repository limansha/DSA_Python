
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

    #Exercise
    def insert_after_value(self, data_after, data_to_insert):
    # Search for first occurance of data_after value in linked list
    # Now insert data_to_insert after data_after node
        if(self.head == None):
            raise Exception("List is empty So can't find value : ",data_after)
        itr = self.head
        flag = False
        while itr:
            if(itr.data == data_after):
                node = Node(data_to_insert,itr.next)
                itr.next = node
                flag = True
                break
            itr = itr.next
        if(flag == False):
            raise Exception("List doesn't contain given data : ",data_after)
        
    def remove_by_value(self, data):
    # Remove first node that contains data
        if(self.head == None):
            raise Exception("List is already empty")
        itr = self.head
        flag = False
        count = 0
        while itr:
            if(itr.data == data):
                flag = True
                self.remove_at_loc(count)
                break
            count +=1
            itr = itr.next
        if(flag == False):
            raise Exception("List doesn't contain given value : ",data)

    def insert_values(self,list):
        for data in list:
            if(self.head == None):
                self.insert_at_beginning(data)
            else:
                self.insert_at_end(data)
if __name__ == '__main__':
    #its a way to store code that should only run when your file is executed as a script
    
    #LL of Integers
    """ll = LinkedList()
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
    ll.print_length()"""
    #ll.remove_at_loc(67) # this raises exception

    print()
    # LL of Strings
    ls = LinkedList()
    ls.insert_values(["banana","mango","grapes","orange"])
    ls.insert_at_beginning("Banana")
    ls.insert_at_end("Grapes")
    ls.insert_at_loc(2,"Mango")
    ls.insert_at_loc(2,"Apple")
    ls.insert_at_beginning("Papaya")
    ls.insert_at_end("Kiwi")
    ls.insert_at_loc(3,"Avacado")
    ls.print_list()
    ls.print_length()
    ls.remove_by_value("Papaya")
    ls.print_list()
    ls.remove_by_value("Kiwi")
    ls.print_list()
    ls.remove_by_value("Avacado")
    ls.print_list()
    ls.print_length()
    ls.insert_after_value("Grapes","PineApple")
    ls.print_list()
    ls.print_length()
    ls.remove_at_begining()
    ls.remove_at_end()
    ls.remove_at_loc(1)
    ls.print_list()
    ls.print_length()
    