# Import necessary libraries
import networkx as nx
import ast

# Mex function that returns the smallest number that is not in a given list of numbers
def mex(K):
    for i in range(0, max(K)+2):
        if not i in K:
            return i

# Determine the edges not connected to the ground
def fall(edges, G):
    falling = []
    edges = list(edges)

    for edge in edges:
        try:
            if not nx.has_path(G, 0, edge[0]):
                falling.append(edge)
        except:
            return edges
    return falling

# Determine the nodes not connected to the ground
def fall_nodes(nodes, G):
    falling = []
    nodes = list(nodes)

    for node in nodes:
        try:
            if not nx.has_path(G, 0, node):
                falling.append(node)
        except:
            return nodes
    return falling

# Remove a given edge and all edges not connected to the ground
def turn(edges, edge): 
    G = nx.MultiGraph()
    edges = list(edges)
    edges.remove(edge)
    G.add_edges_from(edges)
    G.remove_edges_from(fall(G.edges(), G))
    G.remove_nodes_from(fall_nodes(G.nodes(), G))
    return list(G.edges())

# Determine all following positions reachable from removing each edge
def followers(G):
    next = []
    try:
        test = list(G.edges()).copy()
    except:
        test = G
    for edge in test:
        edges = test.copy()
        next.append(turn(edges, edge))
    return next

# Return edges that come up mulitple times
def double_edges(edges):
    for edge in edges:
        e = edges.copy()
        e.remove(edge)
        if edge in e:
            edges.remove(edge)
            edges.append((edge[1], edge[0]))
    return edges

# Determine the Grundy Value of a given position
def value(edges):
    followers_list = followers(edges)
    with open("positions.txt", "r") as value_file:
        values = []
        for v in value_file:
            values.append(ast.literal_eval(v.strip()))
    
    for v in values:
        if v[0] == edges:
            return v[1]

    mex_values = []
    for follower in followers_list:
        found_value = False
        for v in values:
            if v[0] == follower:
                mex_values.append(v[1])
                found_value = True
        if not found_value:
            mex_values.append(value(follower))
            values.append([follower, mex_values[-1]])
    position_value = mex(mex_values)
    values.append([edges, position_value])
    with open("positions.txt", "w") as value_file:
        for v in values:
            values[values.index(v)] = str(v) + "\n"
        value_file.writelines(values)

    return position_value