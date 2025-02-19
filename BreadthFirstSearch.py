#Left-To-Right BFS binary tree implementation with target finding using list and dictionnary

import random

#Generating random list of UNIQUE numbers:
def generate_random_list(size, lower_bound=1, upper_bound=30):
    list=[]
    while len(list) < size:
        num = random.randint(lower_bound, upper_bound)
        if num not in list: #ensure only unique numbers to be added to our list
            list.append(num)

    return list

def generate_binary_tree_bfs(nodes):
    tree = {}
    for i in range(len(nodes)):
        left_index = 2*i+1
        right_index = 2*i+2
        children = []

        if left_index < len(nodes): #to add bounded left child
            children.append(nodes[left_index])
        if right_index <len(nodes): #to add bounded right child
            children.append(nodes[right_index])
        if children: #only adding to the tree if the node has children
            tree[nodes[i]] = children

    return tree

#BFS implementation:
def bfs(tree, root, target):
    visited = []
    queue = [root]

    while queue:
        node = queue.pop(0)

        if node == target:
            print(f"\nTarget {target} found!")
            return node

        if node not in visited:
            print(node, end = " ")
            visited.append(node)


            if node in tree:
                for child in tree[node]:
                    if child not in visited:
                        queue.append(child)

    print(f"\nTarget {target} not found.")
    return

#Our main:
List = generate_random_list(15)
binary_tree = generate_binary_tree_bfs(List)
Target = 10

print(f"The generated binary tree: {binary_tree}")

print("\nBFS of the binary tree:")
bfs(binary_tree, List[0], Target)