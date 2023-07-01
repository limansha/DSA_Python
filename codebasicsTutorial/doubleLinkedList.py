class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoubleLL:
    def __init__(self):
        self.head = None

    def insert_at_beg(self,data):
        if(self.head == None):
            self.head = Node(data,None,None)
        else:
            node = Node(data,self.head,None)
            self.head.prev = node
            self.head = node

    def insert_at_end(self,data):
        if(self.head == None):
            self.insert_at_beg(data)
            return
        itr = self.head
        while itr.next != None:
            itr = itr.next
        itr.next = Node(data,None,itr)

    def insert_at_loc(self,pos,data):
        count = 1
        itr = self.head
        if pos < 0 or pos > self.get_length():
            raise Exception("Invalid Index")
        if pos == 0:
            self.insert_at_beg(data)
            
        elif pos == self.get_length():
            self.insert_at_end(data)
            
        else:    
            while itr:
                if(count == pos):
                    node = Node(data,itr.next,itr)
                    itr.next.prev = node
                    itr.next = node
                    break 
                count = count + 1
                itr = itr.next
            
    def remove_at_beg(self):
        if(self.head == None):
            raise Exception("List is empty")
        self.head = self.head.next # the node is automatically Garbage Collected
    def get_length(self):
        count =0
        itr = self.head
        while itr:
            count +=1
            itr = itr.next
        return count
    def print_forward(self):
    # This method prints list in forward direction. Use node.next
        itr = self.head
        listStrBeg = ''
        while itr:
            listStrBeg += str(itr.data) +' '
            itr = itr.next
        print("forward LL : ",listStrBeg)

    def print_backward(self):
    # Print linked list in reverse direction. Use node.prev for this.
        itr = self.head
        while itr.next != None:
            itr = itr.next
        #once u are in last node
        itr1 = itr
        listStrEnd = ''
        while itr1:
            listStrEnd += str(itr1.data)+' '
            itr1 = itr1.prev
        print("Backward List : ",listStrEnd)

if __name__ == '__main__':
    ll = DoubleLL()
    ll.insert_at_beg("Apple")
    ll.insert_at_beg("Banana")
    print("length is : ",ll.get_length())
    ll.print_forward()
    ll.print_backward()
    ll.insert_at_loc(1,"Orange")
    ll.insert_at_end("PineApple")
    print("length of DLL : ",ll.get_length())
    ll.print_forward()
    ll.print_backward()
    ll.remove_at_beg()
    ll.print_forward()
    print("length of DLL : ",ll.get_length())
    