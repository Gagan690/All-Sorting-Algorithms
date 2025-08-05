import matplotlib.pyplot as plt
import numpy as np
import time


def bubble_sort(arr, draw_func , delay=0.001):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            draw_func(arr, j, j+1)
            time.sleep(delay)


def draw_bars(arr, idx1=None, idx2=None, title="Live Bubble Sort Animation"):
    plt.cla()  # Clear the current axes
    bars = plt.bar(range(len(arr)), arr, color='skyblue')
    if idx1 is not None:
        bars[idx1].set_color('red')
    if idx2 is not None:
        bars[idx2].set_color('green')
    plt.title(title)
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.pause(0.001)  # Pause to update the figure


if __name__ == "__main__":
    np.random.seed(0)
    data = [np.random.random() for _ in range(25)]

    plt.ion()  # Turn on interactive mode
    fig = plt.figure(figsize=(10,4))
    draw_bars(data)

    start_time = time.time()
    bubble_sort(data, draw_bars,delay=0.001)
    end_time = time.time()
    elapsed = end_time - start_time

    draw_bars(data, title=f"Sorted! Time taken: {elapsed:.3f} seconds")
    plt.ioff()  # Turn off interactive mode
    plt.show()  # Keep the window open

    print(f"Sorting completed in {elapsed:.3f} seconds.")
