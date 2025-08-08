import matplotlib.pyplot as plt
import numpy as np
import time
from IPython.display import clear_output

def InsertionSort(arr, draw_func):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        draw_func(arr, i, j)
        
        
def draw_bars(arr, idx1=None, idx2=None, title="Live Insertion Sort Animation"):
    clear_output(wait=True)
    plt.clf()
    bars = plt.bar(range(len(arr)), arr, color='skyblue')
    if idx1 is not None:
        bars[idx1].set_color('red')
    if idx2 is not None:
        bars[idx2].set_color('green')
    plt.title(title)
    plt.xlabel("Index")
    plt.ylabel("Value")
    
    
if __name__ == "__main__":
    np.random.seed(611)
    data = [np.random.randint(0, 100) for _ in range(200)]
    plt.ion()  # Turn on interactive mode
    fig = plt.figure(figsize=(10, 4))
    draw_bars(data)
    start_time = time.time()
    InsertionSort(data, draw_bars)
    end_time = time.time()
    elapsed = end_time - start_time
    print(f"Sorting completed in {elapsed:.3f} seconds.")
    
    draw_bars(data, title=f"Sorted! Time taken: {elapsed:.3f} Seconds")
    plt.ioff()
    plt.show()