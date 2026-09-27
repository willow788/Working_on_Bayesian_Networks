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

def is_collider(bn, previous_node, current_node, next_node):
    """
    Check if the current node is a collider in the path.
    A node is a collider if both edges point into it.
    """
    return bn.has_edge(previous_node, current_node) and bn.has_edge(next_node, current_node)




#d separation function
def d_separated(bn, x, y, z):
    """Return whether ``x`` and ``y`` are d-separated given ``z``.

    D-separation can be tested by taking the ancestors of X, Y, and Z,
    moralizing that ancestral graph, removing the observed nodes, and
    checking whether X and Y are still connected.
    """
    observed = set(z)
    ancestors = set(observed) | {x, y}

    for node in tuple(ancestors):
        ancestors.update(nx.ancestors(bn, node))

    ancestral_graph = bn.subgraph(ancestors).copy()
    moral_graph = ancestral_graph.to_undirected()

    for node in ancestral_graph:
        parents = list(ancestral_graph.predecessors(node))
        moral_graph.add_edges_from((parent, other_parent)
                                   for index, parent in enumerate(parents)
                                   for other_parent in parents[index + 1:])

    moral_graph.remove_nodes_from(observed)
    return not nx.has_path(moral_graph, x, y)


def main():

    print("D-Separation Check:")
    print('are rain and sprinkler d_separated given nothing?')

    result = d_separated(bn, "Rain", "Sprinkler", [])
    print(f"Result: {result}")

    print('are rain and sprinkler d_separated given wet grass?')
    result = d_separated(bn, "Rain", "Sprinkler", ["Wet Grass"])
    print(f"Result: {result}")

    print('are rain and sprinkler d_separated given traffic jam?')
    result = d_separated(bn, "Rain", "Sprinkler", ["Traffic Jam"])
    print(f"Result: {result}")

    print('are rain and sprinkler d_separated given cost?')
    result = d_separated(bn, "Rain", "Sprinkler", ["Cost"])
    print(f"Result: {result}")


if __name__ == "__main__":
    main()


    
