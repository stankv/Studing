# РЕАЛИЗАЦИЯ ДИНАМИЧЕСКОГО МАССИВА И ЕГО МЕТОДОВ
import ctypes

class DynArray:
    
    def __init__(self):
        self.count = 0    # текущее количество элементов в массиве
        self.capacity = 16    # текущая ёмкость буфера (исходно 16 единиц)
        self.array = self.make_array(self.capacity)    # указатель на блок памяти нужной ёмкости, хранящий элементы PyObject

    # Метод "вычисления" текущей длины массива
    def __len__(self):
        return self.count

    # метод формирования блока памяти нужной емкости
    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    # Метод обеспечения поддержки индексации массива
    def __getitem__(self,i):
        if i < 0 or i >= self.count:    # проверка корректности индекса в рамках границ
            raise IndexError('Index is out of bounds')    # генерация исключения
        return self.array[i]

    # Метод изменения размера внутреннего буфера (формирует через make_array() новый буфер, и копирует в него текущее содержимое)
    def resize(self, new_capacity):
        new_array = self.make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    # Метод добавления нового элемента в конец массива
    def append(self, itm):
        if self.count == self.capacity:
            self.resize(2*self.capacity)    # размер буфера увеличиваем вдвое
        self.array[self.count] = itm
        self.count += 1

    # Метод вставки объекта itm в i-ю позицию, сдвигая вперёд все последующие элементы (при необходимости увеличивая буфер)
    def insert(self, i, itm):
        if i < 0 or i > self.count:
            raise IndexError('Index is out of bounds')
        elif i == self.count:    # если индекс равен длине текущего массива, то элемент добавляем в конец
            self.append(itm)
        else:
            if self.count == self.capacity:
                self.resize(2*self.capacity)    # размер буфера увеличиваем вдвое
            new_array = []
            for j in range(self.count + 1):
                if j < i:
                    new_array.append(self.array[j])
                elif j == i:
                    new_array.append(itm)
                elif j > i:
                    new_array.append(self.array[j - 1])
            self.array = new_array
            self.count += 1


    # Метод удаления объекта i-ой позиции (при необходимости сжимая буфер)
    def delete(self, i):
        # удаляем объект в позиции i"""
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        else:
            new_array = []
            for j in range(self.count):
                if j < i or j > i:
                    new_array.append(self.array[j])
                elif j == i:
                    continue
            self.array = new_array
            self.count -= 1
            filling_percentage = int((self.count / self.capacity) * 100)    # процент заполнения буфера
            if filling_percentage < 50:    # если процент заполнения буфера < 50% то уменьшаем буфер в 1.5 раза
                size = int(self.capacity / 1.5)
                if size < 16:
                    self.resize(16)
                else:
                    self.resize(size)