# Import necesarry libraries
import networkx as nx
import matplotlib.pyplot as plt
import functions

# Create graphs to store the edges in the game
G = nx.MultiGraph()
H = nx.MultiDiGraph()
G.add_node(0)

end_game = False # Variable to determine if the game should end
valid_turn = False # Variable to determine if the turn the player wants to make is valid
player = 1 # Player currently to move
num_of_edges = int(input("How many edges should there be? ")) # Input the number of edges in the game
edges = [] # List of edges
options = { # Options for the visualization
    'edge_color': 'green'
}

# Generate edges
for i in range(0, num_of_edges):
    # Input the end points of the edge
    point1 = int(input(f"What should the first point of the {i+1}. edge be? "))
    point2 = int(input(f"What should the second point of the {i+1}. edge be? "))
    # Add the points as nodes to the graph if necessary
    if not point1 in G.nodes():
        G.add_node(point1)
    if not point2 in G.nodes():
        G.add_node(point2)

    edges.append((point1, point2))

# Add the edge to the graph
for edge in edges:
    edge1 = edge[0]
    edge2 = edge[1]
    G.add_edge(edge1, edge2)

# Remove edges and nodes not connected to the ground
G.remove_edges_from(functions.fall(G.edges(), G))
G.remove_nodes_from(functions.fall_nodes(G.nodes(), G))

while not end_game:
    valid_turn = False
    # Draw the graph
    pos = nx.random_layout(G)
    nx.draw_networkx_nodes(G, pos, node_color='black', node_size=50, alpha = 1)
    ax = plt.gca()
    for e in G.edges:
        ax.annotate("",
            xy=pos[e[0]], xycoords='data',
            xytext=pos[e[1]], textcoords='data',
            arrowprops=dict(arrowstyle="-", color="green", linewidth=3,
                shrinkA=5, shrinkB=5,
                patchA=None, patchB=None,
                connectionstyle="arc3,rad=rrr".replace('rrr',str(0.3*e[2])
                ),
                ),
                )
    plt.axis('off')
    plt.show()

    # End game if there are no edges left
    if list(G.edges()) == []:
        break

    # Input the edge the player wants to remove
    while not valid_turn:
        edge = (int(input("What should the first point of the edge be? ")), int(input("What should the second point of the edge be? ")))
        if edge in list(G.edges()):
            valid_turn = True
        elif (edge[1], edge[0]) in list(G.edges()):
            valid_turn = True
            edge = (edge[1], edge[0])
        else:
            print("Edge not in graph. Please try again!")
    
    try:
        # Remove edges not connected to the ground
        new_edges = functions.turn(G.edges(), edge)
        G.clear()
        G.add_edges_from(new_edges)
        player += 1
    except:
        # End game if no edges are left
        end_game = True
        break

print("")

# Print the winner
if player % 2 == 0:
    print("Player 1 won!")
else:
    print("Player 2 won!")