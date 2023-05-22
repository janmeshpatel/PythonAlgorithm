# Queue is based on First In First Out 

def isEmpty(queue):
    if not queue:
        return True
    else :
        return False
    
def insertQueue(queue,n):
    queue.append(n)
    return queue

def deQueue(queue):
    if isEmpty(queue):
        print("Queue is Empty")
        return False
    else :
        queue.pop(0)
        return queue

queue = []

insertQueue(queue,1)
insertQueue(queue,2)
insertQueue(queue,3)
insertQueue(queue,4)
print(queue)

deQueue(queue)
print(queue)
deQueue(queue)
print(queue)




