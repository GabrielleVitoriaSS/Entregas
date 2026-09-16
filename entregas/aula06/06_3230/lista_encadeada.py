# linked_list.py

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if not self.head:
            self.head = Node(value)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(value)

    def __str__(self):
        values = []
        current = self.head
        while current:
            values.append(str(current.value))
            current = current.next
        return ' -> '.join(values)

    def search(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def remove(self, value):
        if self.head.value == value:
            self.head = self.head.next
        else:
            current = self.head
            while current.next:
                if current.next.value == value:
                    current.next = current.next.next
                    return
                current = current.next

def main():
    linked_list = LinkedList()

    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(4)
    linked_list.append(5)

    print(linked_list)  # Output: 1 -> 2 -> 3 -> 4 -> 5

    print(linked_list.search(3))  # Output: True
    print(linked_list.search(6))  # Output: False

    linked_list.remove(3)
    print(linked_list)  # Output: 1 -> 2 -> 4 -> 5
    print(linked_list.search(3))  # Output: False


if __name__ == "__main__":
    main()
