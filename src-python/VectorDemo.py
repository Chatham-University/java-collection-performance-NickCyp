import random

class VectorDemo:
    def __init__(self, how_many_nums):
        self.nums = []
        for _ in range(how_many_nums):
            self.nums = [random.randint(0, how_many_nums - 1) for _ in range(how_many_nums)]

        print("The first few numbers are: ")
        for i in range(min(6, how_many_nums)):
            print(self.nums[i])