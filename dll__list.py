class Node:
    def __init__(self, prev=None, item=None, next=None):
        self.prev = prev
        self.item = item
        self.next = next


class dll:
    def __init__(self, start=None):
        self.start = start

    def is_empty(self):
        return self.start is None

    def insert_at_first(self, data):
        n = Node(None, data, None)
        if self.start is None:
            self.start = n
        else:
            n.next = self.start
            self.start.prev = n
            self.start = n

    def insert_at_last(self, data):
        n = Node(None, data, None)
        if self.start is None:
            self.start = n
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            n.prev = temp
            temp.next = n

    def insert_after(self, tempd, data):
        if self.start is None:
            return
        temp = self.start
        while temp is not None:
            if tempd == temp.item:
                n = Node(temp, data, temp.next)
                if temp.next is not None:
                    temp.next.prev = n
                temp.next = n
                return
            temp = temp.next

    def delete_first(self):
        if self.start is None:
            return
        if self.start.next is None:
            self.start = None
        else:
            self.start = self.start.next
            self.start.prev = None

    def delete_last(self):
        if self.start is None:
            return
        if self.start.next is None:
            self.start = None
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.prev.next = None

    def delete_item(self, data):
        if self.start is None:
            return
        if self.start.item == data:
            self.delete_first()
            return
        temp = self.start
        while temp is not None:
            if temp.item == data:
                if temp.next is not None:
                    temp.next.prev = temp.prev
                if temp.prev is not None:
                    temp.prev.next = temp.next
                return
            temp = temp.next

    def print_list(self):
        if self.start is None:
            print("List is empty")
            return
        temp = self.start
        while temp is not None:
            print(temp.item, end=" <> ")
            temp = temp.next
        print("None")

    def __iter__(self):
        return dlliterator(self.start)


class dlliterator:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        data = self.current.item
        self.current = self.current.next
        return data


# Example usage
q = dll()
q.insert_at_first(40)
q.insert_at_first(50)
q.insert_at_last(70)
q.insert_at_first(50)
q.insert_after(70, 80)
q.insert_after(50, 90)
q.delete_item(80)

# Iterate through the list and print items
for item in q:
    print(item)

# Print the list
q.print_list()
