import random
import tree

min_max = (0, 1000)


def generate_numbers(count):
    for i in range(count):
        yield random.randint(min_max[0], min_max[1])


root = int(sum(min_max) / 2)
data = tree.BinaryTree(root=tree.Node(root))

for item in generate_numbers(count=10):
    data.add(tree.Node(item))

for item in data:
    print(item)
