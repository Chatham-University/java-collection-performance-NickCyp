import random
import time
import array
from collections import deque


HOW_MANY_NUMS = 10**7


class ArrayDemo:
    def __init__(self, how_many_nums, rand):
        self.nums = array.array('i', [rand.randint(0, how_many_nums - 1) for _ in range(how_many_nums)])

        print("The first few numbers are: ")
        for i in range(min(6, how_many_nums)):
            print(self.nums[i])

class VectorDemo:
    def __init__(self, how_many_nums, rand):
        self.nums = [rand.randint(0, how_many_nums - 1) for _ in range(how_many_nums)]

        print("The first few numbers are: ")
        for i in range(min(6, how_many_nums)):
            print(self.nums[i])

class LinkedListDemo:
    def __init__(self, how_many_nums, rand):
        self.nums = deque([rand.randint(0, how_many_nums - 1) for _ in range(how_many_nums)])

        print("The first few numbers are: ")
        for i in range(min(6, how_many_nums)):
            print(self.nums[i])

def main():
    rand = random.Random()

    start = time.time()
    ArrayDemo(HOW_MANY_NUMS, rand)
    end = time.time()
    print(f"Array Time: {end - start:.3f} seconds")


    start = time.time()
    VectorDemo(HOW_MANY_NUMS, rand)
    end = time.time()
    print(f"Vector Time: {end - start:.3f} seconds")


    start = time.time()
    LinkedListDemo(HOW_MANY_NUMS, rand)
    end = time.time()
    print(f"LinkedList Time: {end - start:.3f} seconds")


if __name__ == "__main__":
    main()