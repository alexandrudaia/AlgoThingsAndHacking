
# coding: utf-8

# In[5]:

EX_GRAPH0={0:set([1,2]),1:set(),2:set()}


# In[12]:

EX_GRAPH1={
    
    0:set([1,4,5]),
    1:set([2,6]),
    2:set([3]),
    3:set([0]),
    4:set([1]),
    5:set([2]),
    6:set()
    
}


# In[109]:

EX_GRAPH2={
    0:set([1,4,5]),
    1:set([2,6]),
    2:set([3,7]),
    3:set([7]),
    4:set([1]),
    5:set([2]),
    6:set(),
    7:set([3]),
    8:set([1,2]),
    9:set([0,4,5,6,7,3])
}


# In[42]:

def  make_complete_graph(num_nodes):
    complete_graph={}
    for  node in range(num_nodes):
        complete_graph[node]=set(range(num_nodes))-{node}
    return complete_graph
        


# In[76]:

def compute_in_degrees(digraph):
    in_degrees={}
    for   node in  digraph.keys():
        degree=0
        #compute    in degreee for particular node
        for out_degree in digraph.values():
            for element in out_degree:
                if element==node:
                    degree+=1
        in_degrees[node]=degree
    return in_degrees


# In[100]:

def in_degree_distribution(digraph):
    """How many different indegrees we have in the graph"""
    in_degrees=compute_in_degrees(digraph)
    in_degree_distro={}
    for in_degree in set(in_degrees.values()):
        current_degree=0
        for node,degree in in_degrees.items():
            if in_degree==degree:
                current_degree+=1
        in_degree_distro[in_degree]=current_degree
    return in_degree_distro
    
 

