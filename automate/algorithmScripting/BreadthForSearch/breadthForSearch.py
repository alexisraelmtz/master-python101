from collections import deque

queue = deque([9, 8])
print(queue)
graph = [0, 1, 2, 3, 4]
queue.appendleft(5)
print(queue.popleft())
