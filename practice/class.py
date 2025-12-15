class Calculator():
    def __init__(self, nums):
        self.nums = nums
    
    def jame(self):
        summer = sum(map(int, self.nums.split()))
        print(summer)
        
    def menha(self):
        ...
        
    def zarb(self):
        self.zarb = 1
        for i in self.nums.split():
            self.zarb *= int(i)
        print(self.zarb)
        
    def taghsim(self):
        ...
        
    
num = Calculator("1 2 3 55 8")

num.jame("5 8 6 9")
num.zarb()

