class Set:
    def __init__(self):
        self.dict = {}

    def add(self, item):
        self.dict[item] = True 

    def contains(self, item):
        return self.dict.get(item, False)

    def remove(self, item):
        try:
            del self.dict[item]
        except KeyError as e:
            print('Can\'t remove an item not in the set')
        

    def toString(self):
        print(self.dict.keys())

rich = Set()
rich.add(32)
rich.add(21)

rich.toString()

print(rich.remove(24))

rich.toString()
