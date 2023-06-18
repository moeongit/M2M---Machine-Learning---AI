from queue import PriorityQueue, Queue

pq = PriorityQueue()
q = Queue()

nums = [6, 7, 5]

for num in nums:
    q.put(num)

for num in nums:
    pq.put(num)

print("Queue")
while not q.empty():
    print(q.get())

print("Priority Queue")
while not pq.empty():
    print(pq.get())