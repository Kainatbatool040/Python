graph ={
       '5': ['3','7'],
       '3': ['2','4'],
       '7': ['8'],
       '2': [],
       '4': ['8'],
       '8': []
      
       
       }

visited = []
queue =[]

def dfs(visited, graph, node):
    visited.append(node)
    queue.append(node)
    
    while queue:
        m = queue.pop(0)
        print(m, end= "  ")
        
        for n in graph[m]:
            if n not in visited:
                visited.append(n)
                queue.append(n)
                
                
                
print("Following is the breadth-first search")
dfs(visited, graph, '5')
        
        
        