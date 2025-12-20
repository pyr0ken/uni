class Person:
    def __init__(self, name):
        self.n = name
        # print(self.name)
        
    def show(self):
        print(self.n)
        
        
a = Person(name="ali")
b = Person(name="mohammad")

print(a.n)
print(b.n)

# function: print() list() int()
# method: my_list.append() .test()
# attributes: class.name
