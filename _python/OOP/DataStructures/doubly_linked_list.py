class DNode:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DList:

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_in_empty_list(self, data):
        new_node = DNode(data)
        if self.head == None:
            self.head = new_node
            return self
        else:
            print("this is not an empty list")
            return self

    def insert_at_start(self, data):
        new_node = DNode(data)
        if self.head == None:
            self.head = new_node
            return self
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            if self.head.next.next == None:
                self.tail = self.head.next
            # print ("self.tail is", self.tail.data)
            return self

    def insert_at_tail(self, data):
        new_node = DNode(data)
        if self.head == None:
            self.head = new_node
            return self
        elif self.head.next == None:
            self.head.next = new_node
            self.tail = new_node
            return self
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            return self

    def insert_before(self, x, data):
        new_node = DNode(data)
        if self.head == None:
            print("the list is empty")
            return self
        elif self.head.data == x:
            new_node.next = self.head
            self.head = new_node
            return self
        else:
            runner = self.head
            while runner != None:
                runner = runner.next
                if runner.data == x:
                    new_node.prev = runner.prev
                    new_node.next = runner
                    runner.prev.next = new_node
                    runner.prev = new_node
                    # print(new_node.prev.data, new_node.data, new_node.next.data)
                    # print(runner.prev.data, runner.data)
                    return self
                elif runner.next == None:
                    print ("x is not in this list")
                    return self

    def insert_after(self, x, data):
        new_node = DNode(data)
        if self.head == None:
            print("list is empty, node put into list as first item")
            self.head = new_node
            return self
        elif self.head.data == x:
            new_node.prev = self.head
            self.head.next = new_node
        else:
            runner = self.head
            while runner != None:
                runner = runner.next
                if runner.next == None:
                    print ("**********",runner.data)
                    if runner.data == x:
                        new_node.prev = runner
                        runner.next = new_node
                else:
                    new_node.prev = runner
                    new_node.next = runner.next
                    runner.next.prev = new_node
                    runner.next = new_node
                    return self

    def print_list(self):
        runner = self.head
        while runner != None:
            print (runner.data)
            runner = runner.next
        return self

DLL1 = DList()
DLL1.insert_in_empty_list(10).insert_in_empty_list(20).insert_at_start(0).insert_at_start(-10)
DLL1.print_list()
DLL2 = DList()
DLL2.insert_at_start("a")
DLL2.insert_at_tail("b").insert_at_tail("d").insert_before("d", "c").insert_after("d","e")
DLL2.print_list()
DLL3 = DList()
DLL3.insert_in_empty_list(1).print_list()
DLL3.insert_at_tail(4).print_list()
DLL3.insert_after("1","2").insert_after("2","3")
# DLL3.print_list()