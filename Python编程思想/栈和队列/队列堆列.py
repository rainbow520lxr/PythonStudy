import collections

#创建一个队列
queue = collections.deque()
print(queue)

#进队
queue.append("A")
print(queue)
queue.append("B")
print(queue)
queue.append("C")
print(queue)

#出队（取数据）
res1 = queue.popleft()
print(queue)
print(res1)
res1 = queue.popleft()
print(queue)
res1 = queue.popleft()
print(queue)