import random 
import time 
import matplotlib.pyplot as plt
import numpy as np

def counting_sort_for_radix(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    for i in range(n):
        arr[i] = output[i]
    draw_func(arr)
    return arr

def draw_func(arr, title="Live Radix Sort Animation"):
    plt.cla()
    bars = plt.bar(range(len(arr)), arr, color='skyblue')
    plt.title(title)
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.pause(0.01)
class RadixSort:
    def __get_num_digits(self, arr):
        max_num = max(arr)
        num_digits = 0
        while max_num > 0:
            max_num //= 10
            num_digits += 1
        return num_digits

    def radix(self, arr, num_digits):
        exp = 1
        for _ in range(num_digits):
            arr = counting_sort_for_radix(arr, exp)
            exp *= 10
        return arr

    def sort(self, A):
        if not A or len(A) <= 1:
            return A
        plt.ion()
        fig = plt.figure(figsize=(10, 4))
        draw_func(A, title="Initial Array")
        num_digits = self.__get_num_digits(A)
        A = self.radix(A, num_digits)
        plt.ioff()
        plt.show()
        return A


random.seed(0)

random_list = [random.randint(1, 1000) for _ in range(100)]
start = time.time()
sorter = RadixSort()  # Create an instance of the class
sorted_list = sorter.sort(random_list)
end = time.time()
elapsed = end - start
print(f"Sorting completed in {elapsed:.3f} seconds.")


