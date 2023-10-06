class dynamicArray:
    def __init__(self, arrayLength):
        try:
            self.collection = [None] * arrayLength
            self.capacity = arrayLength
            self.length = 0
        except TypeError:
            return "Invalid size"

    def size(self):
        return self.length
    
    def isEmpty(self):
        return self.size() == 0
    
    def get(self, index):
        try:
            return self.collection[index]
        except IndexError: 
            return "Not a valic index"

    def set(self, index, element):
        try: 
            if (self.collection[index]):
                self.collection[index] = element
                return "element added"
            else:
                return "Not a valid index"
        except IndexError:
            return "Not a valid index"
        
    def clear(self):
        self.collection = [None] * self.capacity
        self.length = 0
    
    def add(self, element):
        if (self.length + 1 >= self.capacity):
            if (self.capacity == 0):
                self.capacity = 1
            else:
                self.capacity *= 2
            newCollection = [None] * self.capacity
            for index, item in enumerate(self.collection):
                newCollection[index] = item
            self.collection = newCollection
        self.collection[self.length] = element
        self.length += 1    
    
    def toString(self):
        if self.length == 0:
            return "[]"
        else:
            collectionString = "["
            for item in self.collection:
                collectionString += str(item) + ", "
            collectionString += "]"
            return collectionString
    
    def removeAt (self, index):
        if (index <= self.capacity):
            i = 0
            newCollection = []
            for item in self.collection:
                if (i != index or item == None):
                    newCollection.append(item)
                i += 1
            self.collection = newCollection
            self.length =- 1
        else:
            return "invalid index"

    def remove (self, element):
        newCollection = []
        for item in self.collection:
            if (item != element or item == None):
                newCollection.append(item)
        self.collection = newCollection
    
    def indexOf (self, element):
        return self.collection.index(element)

    def contains (self, element):
        return self.collection.count(element) > 0
    

def main():
    dyArr = dynamicArray(0)
    print("Size: ", dyArr.size(), dyArr.toString())
    print("isEmpty: ", dyArr.isEmpty())
    dyArr = dynamicArray(1)
    print("isEmpty: ", dyArr.isEmpty(), dyArr.toString())
    print("get 0: ", dyArr.get(0))
    print("get 1: ", dyArr.get(1))
    print("set 0, 4: ", dyArr.set(0, 4), dyArr.toString())
    dyArr.add(5)
    print("add 5: ", dyArr.toString())
    dyArr.add(6)
    print("add 6: ", dyArr.toString())
    dyArr.add(7)
    print("add 7: ", dyArr.toString())
    dyArr.removeAt(1)
    print("remove at 1: ", dyArr.toString())
    dyArr.remove(7)
    print("remove 7: ", dyArr.toString())
    print("indexOf 5: ", dyArr.indexOf(5))
    print("contains 6: ", dyArr.contains(6))


if __name__ == "__main__":
    main()