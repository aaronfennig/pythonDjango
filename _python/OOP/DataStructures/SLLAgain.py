class SLNode:

    def __init__(self, data):
        self.data = data
        self.next = None

class SList:

    def __init__(self):
        self.head = None

    def add_to_front(self, data):
        new_node = SLNode(data)
        new_node.next = self.head
        self.head = new_node
        return self

    def print_list(self):
        runner = self.head
        while runner != None:
            print (runner.data)
            runner = runner.next
        return self

    def add_to_tail(self, data):
        new_node = SLNode(data)
        if self.head == None:
            self.add_to_front(data)
            return self
        else:
            runner = self.head
            while runner.next != None:
                runner = runner.next
            runner.next = new_node

    def remove_from_front(self):
        if self.head == None:
            print("The list you are referring to is empty")
            return self
        else:
            self.head =self.head.next
            return self

    def remove_from_tail(self):
        runner = self.head
        if runner == None:
            print("The list you are referring to is empty")
            return self
        elif runner.next == None:
            # print("runner is", runner.data)
            self.head = None
            return self
        else:
            while runner.next.next != None:
                runner = runner.next
            runner.next = None
            return self

    def remove_val(self, data):
        if self.head == None:
            print("The list you are referring to is empty")
            return self
        runner = self.head
        if self.head.data == data:
            self.head = self.head.next
            return self
        else:
            while runner.next.data != data:
                runner = runner.next
                if runner.next == None:
                    print ("the data you seek to delete does not appear to be in this list")
                    return self
            print ("runner is:", runner.data)
            runner.next = runner.next.next
            return self

    def insert_at_nth(self, data, n):
        new_node = SLNode(data)
        runner = self.head
        if n == 0:
            new_node.next = self.head
            self.head = new_node
            return self
        i = 0
        runner = self.head
        prev = None
        while i != n:
            prev = runner
            runner = runner.next
            if runner == None:
                print ("The list is too short for the position you've entered")
                return self
            i = i+1
        print("runner is", runner.data)
        prev.next = new_node
        new_node.next = runner
        return self



SLL1 = SList()
SLL1.add_to_front(30).add_to_front(20).add_to_front(10).add_to_front(5).add_to_tail(40)
SLL1.remove_from_front()
# SLL1.remove_from_tail().remove_val(30)
SLL1.insert_at_nth(35,3)
SLL1.print_list()

SLL2 = SList()
SLL2.add_to_tail(1)
# SLL2.remove_from_front().remove_from_front()
SLL2.remove_from_tail()
SLL2.print_list()
