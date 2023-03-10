class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None

    def insert_at_begining(self,data):
        node=Node(data,self.head)
        self.head=node

    def insert_at_end(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return
        
        itr=self.head

        while itr.next:
            itr=itr.next
        
        itr.next=Node(data,None)
    
    def insert_values(self,data_list):
        self.head=None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count=0

        itr=self.head
        while itr:
            count+=1
            itr=itr.next

        return count

    def insert_at(self,index,data):
        if index <0 or index >self.get_length():
            raise Exception("Invalid index")
        
        if(index == 0 ):
            self.insert_at_begining(data)
            return

        count=0
        itr=self.head
        while itr:
            if count==index-1:
                node=Node(data,itr.next)
                itr.next=node
                break
            itr=itr.next
            count+=1

    def remove_at(self, index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count+=1

    def insert_after_value(self,data_after,data_to_insert):
        count=0
        itr=self.head
        while itr:
            if itr.data==data_after:
                index=count+1
                break
            itr=itr.next
            count+=1
        else:
            raise Exception("value not present")
        
        self.insert_at(index,data_to_insert)



    def remove_by_value(self,data):
        count=0
        itr=self.head
        while itr:
            if itr.data==data:
                index=count
                break
            itr=itr.next
            count+=1
        else:
            raise Exception("value not present")

        self.remove_at(index)      

        

    def print(self):
        if self.head is None:
            print("list is empty")
            return

        itr=self.head
        listr=" "
        while itr:
            listr+= str(itr.data) + " --> "
            itr = itr.next

        print(listr)



if __name__ == '__main__':
    ll = LinkedList()
    #ll.insert_values(["banana","mango","grapes","orange"])
    #ll.print()
    #ll.insert_at(1,"blueberry")
    #ll.print()
    #ll.remove_at(1)
    #ll.print()

    #ll.insert_values([45,7,12,567,99])
    #ll.insert_at_end(67)
    #ll.print()
    #print(ll.get_length())

    ll.insert_values(["banana","mango","grapes","orange"])
    #ll.remove_by_value("grapes")
    ll.insert_after_value("mango","apple")
    ll.print()
    print(ll.get_length())


        