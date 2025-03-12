import os
import heapq

class KthMaximum:
    def __init__(self):
        self.elements = set()
        self.max_heap = []

    def add(self, key):
        if key not in self.elements:
            self.elements.add(key)
            heapq.heappush(self.max_heap, -key)

    def remove(self, key):
        if key in self.elements:
            self.elements.remove(key)

    def get_kth_maximum(self, k):
        temp_heap = []
        for _ in range(k):
            while True:
                max_elem = -heapq.heappop(self.max_heap)
                if max_elem in self.elements:
                    temp_heap.append(max_elem)
                    break

        kth_maximum = temp_heap[-1]

        for elem in temp_heap:
            heapq.heappush(self.max_heap, -elem)

        return kth_maximum

def task_scheduler(input_file='input.txt', output_file='output.txt'):
    input_path = os.path.join('..', 'txtf', input_file)
    output_path = os.path.join('..', 'txtf', output_file)

    with open(input_path, 'r') as f:
        n = int(f.readline().strip())
        kth_maximum = KthMaximum()
        results = []

        for _ in range(n):
            command = list(map(int, f.readline().strip().split()))
            c, k = command[0], command[1]

            if c == 1:
                kth_maximum.add(k)
            elif c == 0:
                result = kth_maximum.get_kth_maximum(k)
                results.append(result)
            elif c == -1:
                kth_maximum.remove(k)

    with open(output_path, 'w') as f:
        for result in results:
            f.write(f"{result}\n")

if __name__ == "__main__":
    task_scheduler()
