tree ={
       'A': {'B','G'},
       'B': {'C','D'},
       'C': {'E'},
       'D': {},
       'E': {'F'},
       'F': {},
       'G': {'H'}
       
       }
print(tree)


#  visited tree    #



tree ={
       'A': {'B','G'},
       'B': {'C','D'},
       'C': {'E'},
       'D': {},
       'E': {'F'},
       'F': {},
       'G': {'H'}
       
       }
print(tree)
visited =set()

def dfs(visited, tree, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for n in tree[node]:
            dfs(visited, tree, n)
            
dfs(visited, tree, 'A')
 