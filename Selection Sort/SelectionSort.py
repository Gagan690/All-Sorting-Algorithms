import matplotlib.pyplot as plt
import numpy as np
import time

def SelectionSort(arr , draw_func):
    n = len(arr)
    for i in range(n):
        pos = i
        min =i
        for j in range(i+1, n):
            if arr[j] < arr[min]:
                min = j
        arr[pos], arr[min] = arr[min] , arr[pos]
        draw_func(arr , pos , min)
        
    
def draw_bars(arr, idx1= None , idx2=None , title="Live Selection Sort Animation"):
    plt.cla()
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
    data = [np.random.random() for _ in range(100)]
    plt.ion() # Turn on interactive mode
    fig = plt.figure(figsize=(10,4))
    draw_bars(data)
    start_time = time.time()
    SelectionSort(data, draw_bars)
    end_time = time.time()
    elapsed = end_time - start_time
    print(f"Sorting completed in {elapsed:.3f} seconds.")
    
    draw_bars(data, title=f"Sorted! Time taken: {elapsed:.3f} Seconds")
    plt.ioff()
    plt.show()