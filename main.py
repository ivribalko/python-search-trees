import random
import tree


def generate_numbers(count):
    for i in range(count):
        yield random.randint(0, 1000)


tree = tree.Tree()

for item in generate_numbers(count=10):
    print(item)
