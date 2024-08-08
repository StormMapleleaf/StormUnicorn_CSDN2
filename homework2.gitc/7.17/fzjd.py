class Item:
    def __init__(self, weight, value):
        self.weight = weight 
        self.value = value   

def kbb(items, capacity):
    items.sort(key=lambda item: item.weight, reverse=True) 
    return kbr(items, capacity, 0, 0, 0, 0)

def kbr(items, capacity, currentIndex, currentValue, currentWeight, maxvalue):
    #print(currentIndex, currentValue, currentWeight, maxvalue)

    if currentWeight > capacity or currentIndex >= len(items): 
        return maxvalue 
    if currentValue > maxvalue: 
        maxvalue = currentValue 

    maxvalue = kbr(items, capacity, currentIndex + 1,
            currentValue + items[currentIndex].value,
            currentWeight + items[currentIndex].weight, maxvalue) 

    maxvalue = kbr(items, capacity, currentIndex + 1,
            currentValue, currentWeight, maxvalue) 
    return maxvalue

items = [Item(10, 60), Item(20, 110), Item(30, 180)]
capacity = 50
max_value = kbb(items, capacity)
print(f"最大价值: {max_value}")
