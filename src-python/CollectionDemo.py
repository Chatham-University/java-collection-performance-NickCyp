import random
import time
import array
from collections import deque
import statistics


HOW_MANY_NUMS = 10**7
NUM_RUNS = 10


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

def run_test(test_class, how_many_nums, rand):
    start = time.time()
    test_class(how_many_nums, rand)
    end = time.time()
    return end - start


def measure_variance(test_class, how_many_nums, rand, num_runs):
    """Run the test multiple times and calculate statistics."""
    times = []
    for _ in range(num_runs):
        elapsed_time = run_test(test_class, how_many_nums, rand)
        times.append(elapsed_time)

    mean_time = statistics.mean(times)
    std_dev = statistics.stdev(times)
    min_time = min(times)
    max_time = max(times)

    return {
        "mean": mean_time,
        "std_dev": std_dev,
        "min": min_time,
        "max": max_time,
        "times": times
    }

def main():
    rand = random.Random()

    print("Running ArrayDemo tests...")
    array_stats = measure_variance(ArrayDemo, HOW_MANY_NUMS, rand, NUM_RUNS)
    print(f"ArrayDemo - Mean: {array_stats['mean']:.3f} seconds, Std Dev: {array_stats['std_dev']:.3f}, "
          f"Min: {array_stats['min']:.3f}, Max: {array_stats['max']:.3f}")

    print("\nRunning VectorDemo tests...")
    vector_stats = measure_variance(VectorDemo, HOW_MANY_NUMS, rand, NUM_RUNS)
    print(f"VectorDemo - Mean: {vector_stats['mean']:.3f} seconds, Std Dev: {vector_stats['std_dev']:.3f}, "
          f"Min: {vector_stats['min']:.3f}, Max: {vector_stats['max']:.3f}")

    print("\nRunning LinkedListDemo tests...")
    linked_list_stats = measure_variance(LinkedListDemo, HOW_MANY_NUMS, rand, NUM_RUNS)
    print(f"LinkedListDemo - Mean: {linked_list_stats['mean']:.3f} seconds, Std Dev: {linked_list_stats['std_dev']:.3f}, "
        f"Min: {linked_list_stats['min']:.3f}, Max: {linked_list_stats['max']:.3f}")


if __name__ == "__main__":
    main()