class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Другие методы класса LinkedList ...

    def __len__(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def remove_first(self):
        if self.head:
            self.head = self.head.next
        else:
            raise ValueError("Невозможно удалить из пустого списка")

    def remove_last(self):
        if not self.head:
            raise ValueError("Невозможно удалить из пустого списка")
        if not self.head.next:
            self.head = None
            return
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None

    def remove_at(self, index):
        if index < 0 or (index >= len(self)):
            raise ValueError("Индекс выходит за пределы диапазона")
        if index == 0:
            self.remove_first()
            return
        current = self.head
        for _ in range(index - 1):
            current = current.next
        current.next = current.next.next

    def remove_first_value(self, value):
        current = self.head
        previous = None
        while current:
            if current.data == value:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                return
            previous = current
            current = current.next
        raise ValueError("Индекс выходит за пределы диапазона")

    def remove_last_value(self, value):
        current = self.head
        previous = None
        last_match = None
        while current:
            if current.data == value:
                last_match = current
            previous = current
            current = current.next
        if last_match:
            if previous:
                previous.next = last_match.next
            else:
                self.head = last_match.next
        else:
            raise ValueError("Число не найдено!")



#Создаем экземпляр класса LinkedList
my_list = LinkedList()

# Добавляем элементы в список (для примера)
my_list.add(1)
my_list.add(2)
my_list.add(3)

# Используем метод __len__ для получения количества элементов
print(len(my_list))  # Выведет: 3

# Удаляем первый элемент
my_list.remove_first()

# Удаляем последний элемент
my_list.remove_last()

# Удаляем элемент по индексу
my_list.remove_at(0)  # Удалит первый (единственный) элемент

# Удаляем первое найденное значение
my_list.remove_first_value(2)

# Удаляем последнее найденное значение
my_list.remove_last_value(4)
