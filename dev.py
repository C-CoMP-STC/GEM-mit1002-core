# A function that takes an adjacency matrix that counts the number of
# feed forward loops and 3-node feedback loops in a given network. 
# It uses the rapid method for the enumeration of 3-node subgraphs that
# is described in S. Itzkovitz. Et.al, (“Subgraphs in random networks“ 
# PHYSICAL REVIEW E 68, 026127 .2003), which is based on adjacency 
# matrix operations. A network adjacency matrix is denoted by M, where 
# M(i,j) = 1 if a directed edge exists from node i to node j and 0 
# otherwise. For example, the number of self-loops can be easily counted
# by summing up the diagonal of M.
def count_loops(M):
    