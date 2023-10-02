import time

class ArrayDin:
    def __init__(self, initial_size=20):
        self.array = [None] * initial_size
        self.length = 0

    def insert(self, element):
        if self.length == len(self.array):
            self.array += [None] * len(self.array)
        self.array[self.length] = element
        self.length += 1

def conteo(array, num_insert):
    start_time = time.time()
    for i in range(num_insert):
        array.insert(i)
    end_time = time.time()
    return end_time - start_time

dynamic_array = ArrayDin()
num_insertions = 10000
time_taken = conteo(dynamic_array, num_insertions)
print(f"Tiempo tomado para {num_insertions} inserciones: {time_taken} segundos")