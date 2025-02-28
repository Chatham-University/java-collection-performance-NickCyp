from _collections import deque
import random

class LinkedListDemo:
    def __init__(self, how_many_nums):
        self.nums = deque()
        for _ in range(how_many_nums):
            self.nums.append(random.randint(0, how_many_nums -1))

        print("The first few numbers are: ")
        for i in range(min(6, how_many_nums)):
            print(self.nums[i])