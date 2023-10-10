#-*- coding: cp1251 -*-
import time

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
        else:
            current = self.head
            while current.next:
                if current.next.data == data:
                    current.next = current.next.next
                    break
                current = current.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

def is_palindrome(input_string):
    input_string = input_string.lower().replace(" ", "")
    stack = Stack()
    mid = len(input_string) // 2
    for char in input_string[:mid]:
        stack.push(char)
    if len(input_string) % 2 != 0:
        mid += 1
    for char in input_string[mid:]:
        if char != stack.pop():
            return False
    return True

def perform_operations(linked_list, num_operations):
    if num_operations <= 0:
        return 0.0
    start_time = time.perf_counter()
    for i in range(1, num_operations + 1):
        linked_list.append(i)
        linked_list.prepend(i)
        linked_list.delete(i)
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    return execution_time

def main():
    linked_list = LinkedList()

    while True:
        try:
            num_elements = int(input("������ ������� �������� ������: "))
            break
        except ValueError:
            print("�������: ������������ ������ �������� �����. ������ ���� �����.")

    for _ in range(num_elements):
        while True:
            try:
                element = int(input("������ ������� ��� ��������� �� ������: "))
                linked_list.append(element)
                break
            except ValueError:
                print("�������: ������������ ������ �������� �����. ������ ���� �����.")

    print("\n����:")
    print("1. ������ ������� � ����� ������")
    print("2. ������ ������� �� ������� ������")
    print("3. �������� ������� � ������")
    print("4. ������� ������")
    print("5. ��������� ������ �� ��������")
    print("6. �������� ����� ���� ��������� �������� ��� �������")
    print("0. �����")

    while True:
        try:
            choice = int(input("������� ��������: "))

            if choice == 0:
                break
            elif choice == 1:
                element = int(input("������ ������� ��� ��������� � ����� ������: "))
                linked_list.append(element)
            elif choice == 2:
                element = int(input("������ ������� ��� ��������� �� ������� ������: "))
                linked_list.prepend(element)
            elif choice == 3:
                element = int(input("������ ������� ��� ��������� � ������: "))
                linked_list.delete(element)
            elif choice == 4:
                print("������:")
                linked_list.display()
            elif choice == 5:
                input_string = input("������ ������ ��� �������� �� ��������: ")
                if is_palindrome(input_string):
                    print("�� ������ � ����������.")
                else:
                    print("�� ������ �� � ����������.")
            elif choice == 6:
                num_operations = int(input("������ ������� �������� ��� ������: "))
                execution_time = perform_operations(linked_list, num_operations)
                print(f"��� ��������� {num_operations} ��������: {execution_time:.6f} ������")
            else:
                print("������� ����. ��������� �� ���.")
        except ValueError:
            print("�������: ������������ ������ �������� �����. ������ ���� �����.")

if __name__ == "__main__":
    main()

