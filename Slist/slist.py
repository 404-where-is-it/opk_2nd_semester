class Node :

    def __init__(self, data=None) :
        self.data = data
        self.next = None

class Slist :

    def __init__(self) :
        self.head = None    # указывает на первый элемент
        self._length = 0    # длина списка
        self.tail = None    # указывает на последний элемент


    # Вернуть количество узлов в списке
    def length(self) :

        return self._length


    # Добавить новый узел в конец списка.
    def append(self, data) :
        new_node = Node(data)
        if self.head is None :       # и начало и конец будут равны новому узлу
            self.head = new_node
            self.tail = new_node
            self._length += 1

            return


        self.tail.next = new_node   # теперь следующий после последнего есть новый узел
        if self.head == self.tail :
            self.head.next = self.tail.next
        self.tail = self.tail.next  # теперь хвост будет последним
        self._length += 1


    # Добавить новый узел в начало списка.
    def prepend(self, data) :
        new_node = Node(data)
        self._length += 1           # увеличиваем длину
        if self.head is None :       # и начало и конец будут равны новому узлу
            self.head = new_node
            self.tail = new_node
            return

        new_node.next = self.head   # ставим новый узел в начало
        self.head = new_node        # делаем его начальным


    # Вернуть данные элемента по индексу
    def get(self, index) :
        if self.head is None :
            return None

        curr = self.head
        for i in range(index):   # идём по элементам до индекса
            if curr.next is not None :
                curr = curr.next
            else:
                return None
        return curr.data


   # Удалить узел по индексу. Вернуть его значение
    def remove(self, index) :
        if self.head is None :
            return None

        prev = self.head
        curr = self.head
        count = 0
        while curr is not None :
            if index == count :
                if index == 0 :
                    self.head = curr.next
                else:
                    prev.next = curr.next
                self._length -= 1
                return curr.data
            count += 1
            prev = curr
            curr = curr.next
        # если вышли из цикла, значит count < index
        return None


    # Вернуть последний элемент.
    def get_last(self) :
        if self.head is None :
            return None
        return self.tail.data

    # Найти data в списке, если имеется.
    # Вернуть индекс
    def find(self, data) :
        curr = self.head
        if curr is None :
            return -1

        index = 0
        while curr is not None :
            if curr.data == data :
                return index
            curr = curr.next
            index += 1

        # Если мы прошли весь список и не вышли из функции, значит, ничего не нашли
        return -1

    # Удалить первый элемент со значением data
    def remove_first(self, data) :
        if self.head is None :
            return None

        prev = self.head
        curr = self.head
        count = 0
        while curr:
            if data == curr.data :
                if curr == self.head :
                    self.head = curr.next
                else:
                    prev.next = curr.next
                self._length -= 1
                return
            count += 1
            prev = curr
            curr = curr.next


    # Удалить все элементы со значением data
    def remove_all(self, data) :
        if self.head is None:
            return None

        prev = self.head
        curr = self.head
        count = 0
        while curr:
            if data == curr.data :
                if curr == self.head :
                    self.head = curr.next
                else:
                    prev.next = curr.next
                self._length -= 1
            count += 1
            prev = curr
            curr = curr.next

    # Скопировать список. Вернуть копию
    def copy(self) :
        curr = self.head
        dest = Slist()
        if curr is None :
            return dest
        while curr is not None :
            dest.append(curr.data)
            curr = curr.next
        return dest

    # Применить функцию к каждому узлу (данным в нём)
    def foreach(self, func) :
        if self.head is None :
            return

        curr = self.head
        while curr:
            curr.data = func(curr.data)
            curr = curr.next


    # Найти первый узел, если данные в нём
    # удовлетворяют предикату.
    def find_custom(self, predicate) :
        if self.head is None :
            return

        curr = self.head
        index = 0
        while curr:
            if predicate(curr.data) :
                return curr.data, index
            curr = curr.next
            index += 1

        # Если мы прошли весь список и не вышли из функции, значит, ничего не нашли
        return -1

    def concat(self, list2) :
        if list2.head is None :
            return self
        if self.head is None :
            self.head = list2.head
            self.tail = list2.tail
            self._length = list2.length()
            return self

        self.tail.next = list2.head
        self.tail = list2.tail
        self._length = self.length() + list2.length()
        return self


def my_predicate(x) : # предикат
    if x % 2 == 0 :
        return 1
    else:
        return 0

def my_print(a) :
    print(f"{a}  ", end='')
    return a

def main() :
    x = Slist()
    x.append(1)
    x.append(0)
    x.append(8)
    x.append(0)
    x.foreach(my_predicate)
    x.foreach(my_print)

if __name__ == "__main__":
    main()

