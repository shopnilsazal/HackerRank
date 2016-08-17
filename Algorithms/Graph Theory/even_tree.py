n, m = map(int, input().split())
edges = []
for i in range(m):
    u, v = map(int, input().split())
    edges.append([u, v])


def find_children(n):
    children = []
    for i in range(m):
        if edges[i][1] == n:
            children.append(edges[i][0])
            child_n = find_children(edges[i][0])
            for child in child_n:
                children.append(child)
    return children


def generate_tree(tree):
    for i in range(n):
        tree.append([i+1])
    for i in range(n):
        tree[i].append(find_children(i+1))
    return tree

tree = []
gen_tree = generate_tree(tree)

count = 0
for i in range(n):
    if len(gen_tree[i][1]) % 2 == 1:
        count += 1

print(count - 1)
