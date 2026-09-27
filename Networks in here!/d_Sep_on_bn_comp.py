#now we will generate a more complex bn
import networkx as nx
import matplotlib.pyplot as plt

#using a directed graph
bn = nx.DiGraph()

#adding edges to the graph
bn.add_edges_from([
    ("Rain", "Wet Grass"),
    ("Rain", "Traffic Jam"),
    ("Sprinkler","Wet Grass"),
    ("Sprinkler","Traffic Jam"),
    ("Sprinkler", "Cost")
])

"""
                 Rain
                /    \
               ↓      ↓
          Wet Grass   Traffic
               ↑        ↑
               │        │
          Sprinkler ────┘
               │
               ↓
             Cost
"""

#plot ting the network
pos = {
    "Rain": (0, 1),
    "Sprinkler": (1, 1),
    "Wet Grass": (0, 0),
    "Traffic Jam": (1, 0),
    "Cost": (0.5, -1)}

#drawing the network
nx.draw(bn,
        pos,
        with_labels=True,
        node_size=2000,
        node_color="red",
        font_size=10,
        font_weight="bold")

plt.title("Bayesian  Network: a more complex example")
plt.savefig("bayesian_network_complex.png")  # Save the figure as a PNG file
plt.show()


#d separation function
def d_separated(bn, x, y, z):

    #11st finding the unidirected path btw x and y
    unidirected_path = bn.to_undirected()

    paths = list(
        nx.all_simple_paths(
            unidirected_path,
            source=x,
            target=y
        )
    )

    #checking  every path
    for road in paths:

        #checking if the path between x and y is blocked by z
        print('Checking path: ', "->".join(road))

        #checking if the middle nodes are contained in z
        middle_nodes = road[1:-1]  # Exclude the start and end nodes

        if middle_nodes in z:
            print(f"Path {road} is blocked by {z}.")
            return True  # Path is blocked
        else:
            print(f"Path {road} is not blocked by {z}.")
            return False  # Path is not blocked

        return False  # If no paths are blocked, return False

    

    
