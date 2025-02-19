#Left-To-Right DFS binary tree implementation with target finding using list and dictionary(with set as value for each key)

import random

#Generating random list of UNIQUE numbers:
def generate_random_list(size, lower_bound=1, upper_bound=30):
    list=[]
    while len(list) < size:
        num = random.randint(lower_bound, upper_bound)
        if num not in list: #ensure only unique numbers to be added to our list
            list.append(num)

    return list

def generate_binary_tree_dfs(nodes):
    tree = {}
    for i in range(len(nodes)):
        left_index = 2*i+1
        right_index = 2*i+2
        children = set()

        if left_index < len(nodes): #to add bounded left child
            children.add(nodes[left_index])
        if right_index <len(nodes): #to add bounded right child
            children.add(nodes[right_index])
        if children: #only adding to the tree if the node has children
            tree[nodes[i]] = children

    return tree

#DFS implementation:
def dfs(tree, node, target, visited=None):
    if visited is None:
        visited = set()

    visited.add(node)
    print(node, end=" ")

    if node == target:
        print(f"\nTarget {target} found!")
        return node

    if node in tree: #if node has children (c-à-d is a key)
        for child in tree[node]:
            if child not in visited:
                result = dfs(tree, child,target, visited) #recursive call
                if result == target:
                    return result

    return None

#Our main:
List = generate_random_list(15)
binary_tree = generate_binary_tree_dfs(List)
Target = 15

print(f"The generated binary tree: {binary_tree}")
print("\nDFS of the binary tree:")

result = dfs(binary_tree, List[0], Target)

if result is None:
    print(f"\nTarget {Target} not found.")
