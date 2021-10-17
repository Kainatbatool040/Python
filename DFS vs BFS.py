tree ={
       'Islamabad': ['lahore','rawalpindi'],
       'lahore': ['multan','sukkar'],
       'multan': ['sukkar'],
       'sukkar': ['karachi',],
       'karachi': [],
       'rawalpindi': ['multan','sukkar'],
       'sukkar': ['karachi']
       
       }

visited1 = set()

def dfs(visited1, tree, node):
    if node not in visited1 and 'karachi' not in visited1:
        print(node)
        visited1.add(node)
        for n in tree[node]:
            dfs(visited1, tree, n)
    
print("Following is the depth first search")        
dfs(visited1, tree, 'Islamabad')




visited = []
queue =[]

def bfs(visited, tree, node):
    visited.append(node)
    queue.append(node)
    
    while queue:
        m = queue.pop(0)
        print(m, end= "  ")
        
        for n in tree[m]:
            if n not in visited  and 'karachi' not in visited:
                visited.append(n)
                queue.append(n)
                
print("Following is the breadth-first search")
bfs(visited, tree, 'Islamabad')


if(len(visited1)<len(visited)):
    print("\n Depth first search is more optimal with visited city count "+str(len(visited1)-2))
else:
    print("\n Breadth first search is more optimal with visited city count "+str(len(visited)-2))