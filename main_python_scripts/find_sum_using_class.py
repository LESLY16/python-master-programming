class Solution:
    def getdata(self):
        self.num1 = int(input("Enter a number"))
        self.num2 = int(input("Enter another number"))
    def sum(self):
        self.total = self.num1+self.num2
    def display(self):
        print(f"Sum is {self.total}")
obj = Solution()
obj.getdata()
obj.sum()
obj.display()