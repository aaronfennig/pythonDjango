class SLNode:

    def __init__(self, val):
        self.value = val
        self.next = None


class SList:

    def __init__(self):
        self.head = None

    def add_to_front(self, val):
        new_node = SLNode(val)
        current_head = self.head
        new_node.next = current_head
        self.head = new_node
        return self

    def print_values(self):
        runner = self.head
        while(runner != None):
            print(runner.value)
            runner = runner.next
        return self

    def add_to_tail(self, val):
        new_node = SLNode(val)
        runner = self.head
        # print(runner.value)
        while(runner.next != None):
            runner = runner.next
            # print(runner.value)
        runner.next = new_node
        return self

    def remove_from_front(self):
        current_head = self.head
        self.head = current_head.next
        current_head = None
        return self

    def remove_from_tail(self):
        temp = self.head
        while(temp.next.next != None):
            temp = temp.next
        temp.next = None
        return self

    def remove_val(self, val):
        runner = self.head
        if(runner.value == val):
            self.remove_from_front()
            return self
        else:
            while (runner != None):
                if runner.value == val:
                    break
                prev = runner
                runner = runner.next
            if(runner == None):
                return self
            prev.next = runner.next
            return self

    def insert_at(self, val, n):
        new_node = SLNode(val)
        if self.head == None:
            if n != 0:
                print("Nth positon does not exist in current list")
                return self
            else:
                self.head = new_node
        if self.head != None and n == 0:
            self.add_to_front(val)
            return self
        current = self.head
        previous = None
        i = 0
        while (i < n):
            previous = current
            current = current.next
            if current == None:
                print("Nth positon does not exist in current list...")
                break
            i = i +1
        # print(i, previous.value, current.value)
        previous.next = new_node
        new_node.next = current
        return self


# SLL1 = SList().add_to_front(3).add_to_front(2).add_to_front(1).add_to_tail(4).remove_from_front(
# ).print_values().add_to_front(1).remove_from_tail().add_to_tail(4).print_values()
# my_list = SList()  # create a new instance of a list
# my_list.add_to_front("are").add_to_front("Linked lists").add_to_tail(
#     "fun!").remove_from_tail().add_to_tail("fun!").print_values()
# SLL1.print_values()
# SLL1.remove_val(2)
# SLL1.print_values()
# SLL1.insert_at(25, 0)
# SLL1.print_values()
# SLL2 = SList()
# SLL2.insert_at(25, 0)
# SLL2.print_values()
# SLL2.insert_at(15, 1)
# SLL2.print_values()
mySLL = SList()
mySLL.add_to_front(0).add_to_tail(10).add_to_tail(30).add_to_tail(40).print_values()
mySLL.insert_at(20,2).insert_at(-10,0).insert_at(50,6)
mySLL.print_values()
