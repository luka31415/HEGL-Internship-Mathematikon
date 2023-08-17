# Import necessary libraries
import networkx as nx
import functions as f
import ast

G = nx.MultiGraph() # Create graph to store the edges

while True:
    edges = ast.literal_eval("[" + input("What are the edges in the graph?\n") + "]") # Add the edges to a list
    if edges == []:
        break
    # Add the edges to the graph and remove any edges not connected to the ground
    G.clear()
    G.add_edges_from(edges)
    G.remove_edges_from(f.fall(G.edges(), G))

    followers = f.followers(G) # Generate all the following positions reachable from the current one
    follower_values = []
    edge_to_remove = ()

    # Calculate all the Grundy Values for the following positions
    for follower in followers:
        follower_values.append(f.value(follower))

    if 0 in follower_values: # Position is winning for the current player
        edge_to_remove = list(G.edges())[follower_values.index(0)] # Edge to remove to reach the losing position for the opposing player
    else:
        edge_to_remove = list(G.edges())[follower_values.index(max(follower_values))] # Remove the edge with the least winning moves for the opponent

    print(edge_to_remove, 0 in follower_values) # Print the edge to remove