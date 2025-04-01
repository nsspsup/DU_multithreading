import threading
import time


numbers = []

def find_max():
    maximum = max(numbers)
    print(f"Largest value in the list: {maximum}")


def find_min():
    minimum = min(numbers)
    print(f"Smallest value in the list: {minimum}")


user_input = input("Enter numbers separated by spaces: ")
numbers = list(map(int, user_input.split()))


max_thread = threading.Thread(target=find_max)
min_thread = threading.Thread(target=find_min)

start = time.time()

max_thread.start()
min_thread.start()


max_thread.join()
min_thread.join()

duration = time.time() - start
print(f"Time taken: {duration:.2f} seconds")
