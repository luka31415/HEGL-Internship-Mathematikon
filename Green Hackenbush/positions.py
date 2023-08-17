# Import necesarry libraries
import networkx as nx
import ast
import functions as f

G = nx.MultiGraph() # Create a graph to store the edges
edges = ast.literal_eval("[" + input("What are the edges?\n") + "]") # Add the edges to a list
G.add_edges_from(edges) # Add the edges to the graph
G.remove_edges_from(f.fall(G.edges(), G)) # Remove edges not connected to the ground

# Determine the Grundy Value of the position and print it out
position_value = f.value(list(G.edges()))
print(position_value)