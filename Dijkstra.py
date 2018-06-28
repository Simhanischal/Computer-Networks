
# coding: utf-8

# In[3]:



infinity = 99 #Node with infinte value implies the link is broken
startnode = 0 #Initialize the startnode to zero

#Number of rows and columns for the cost matrix(rows=columns) 
no_of_vertices = int(input("Enter the number of vertices  \n"))

#Cost Matrix -> 
cost_matrix = [[0 for j in range(no_of_vertices)] for i in range(no_of_vertices)] #List Comprehension to initialize the 2D cost matrix with zeros 
for i in range(no_of_vertices):
    for j in range(no_of_vertices):
        inp = int(input("enter the element")) #Taking input from the user
        cost_matrix[i][j] = inp
        
#A function to implement the algorithm
def dijkstra(cost,nv):
    pred = []
    distance = []
    visited = []
    count = 0
    nextnode = 0
    mindistance = 0
    for i in range(nv):
        distance.append(cost[startnode][i])
        pred.append(startnode)
        visited.append(0)
    distance[startnode] = 0
    visited[startnode] = 1
    count = 1
    while(count < nv-1):
        mindistance = infinity
        for i in range(nv):
            if distance[i]< mindistance and visited[i]==0:
                mindistance = distance[i]
                nextnode = i
            visited[nextnode] = 1
        for i in range(nv):
            if visited[i]==0:
                if mindistance + cost[nextnode][i] < distance[i]:
                    distance[i] = mindistance + cost[nextnode][i]
                    pred[i] = nextnode
        count += 1
    for i in range(nv):
        if i != startnode:
            print("\nDistance of node %d = %d " %(i,distance[i]))
            print("\nPath = %d" %(i))
            j = i
            
            #Do while loop
            while(True):
                j = pred[j]
                print("<-%d" %(j))
                if j==startnode:
                    break
    
                    
            


# dijkstra(cost_matrix , no_of_vertices)

# In[4]:


dijkstra(cost_matrix , no_of_vertices)

