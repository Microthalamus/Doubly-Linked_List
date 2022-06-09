#Code used in project is in refernece to a video called Python:Doubly Linked from Joe James (link : https://www.youtube.com/watch?v=sDP_pReYNEc)

class Node (object):
    def __init__(self,d):
        self.data = d
        self.next_node = None
        self.prev_node = None

    def get_next (self):
        return self.next_node

    def set_next (self, n):
        self.next_node = n

    def get_prev (self):
        return self.prev_node

    def set_prev (self, p):
        self.prev_node = p

    def get_data (self):
        return self.data

    def set_data (self, d):
        self.data = d

class linked_list (object):
    def __init__(self):
        self.head = None
        self.size = 0

    def insert(self,d):
#Funtion that inserts data to the end of end of the linked list
        new_node = Node (d, self.head)
        if self.head:
            self.head.set_prev(new_node)
        self.head = new_node
        self.size +=1

    def remove (self, d):
#Function that removes the node specified by pointer/reference from the Linked List.
        new_node = self.head
        while new_node:
            if new_node.get_data == d:
                nxt = new_node.get_next()
                prv = new_node.get_prev()

                if nxt:
                    next.set_prev(prv)
                if prv:
                    prv.set_next(nxt)
                else:
                    self.head = new_node
                self.size -=1
                return True  #Outcome for when data is removed
            else:
                new_node = new_node.get_next()
        return False  #Outcome for when there is no data found to remove

    def find(self,d):
#Finds the node in the Linked List containing specified data.
        cur_N = self.head
        while cur_N:
            if cur_N.get_data() == d:
                return d
            else:
                cur_N = cur_N.get_next()
        return None

    def print(self):
#Function that prints the contents/data (or a representation of the data) in the Linked List to the screen
        cur_N = self.head
        while cur_N:
            print(cur_N.data)
            cur_N = cur_N.next_node

dllist = linked_list()