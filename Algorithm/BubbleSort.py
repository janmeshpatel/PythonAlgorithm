# Bullble Sort Algorithm

def bubbleSort(data):
    for i in range(len(data)):
        for j in range(len(data)-i-1):
            if data[j] > data[j+1]:
                data[j],data[j+1] = data[j+1],data[j]
                 
    return data



data = [1,6,2,5,3,4]
print(bubbleSort(data))
