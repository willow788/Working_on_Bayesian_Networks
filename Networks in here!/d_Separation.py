import networkx as nx
import matplotlib.pyplot as plt     

#creating the directed graph

bx = nx.DiGraph() #this is a directed graph

bx.add_edges_from([
    ("Rain", "Wet Grass"),
    ("Sprinkler", "Wet Grass"),

])

#drawing the network
pos = {
    "Rain": (0, 1),
    "Sprinkler": (1, 1),
    "Wet Grass": (0.5, 0)
}

nx.draw(
    bx,
    pos,
    with_labels=True,
    node_size=2000,
    node_color="lightblue",
    font_size=10,
    font_weight="bold",
)

plt.title("Bayesian Network: Rain, Sprinkler, Wet Grass")
plt.savefig("bayesian_network.png")  # Save the figure as a PNG file
plt.show()

#now we will be implementing the d separation on this graph

def d_separated(bx, x, y, z):

    #1st finding the unidirected path btw x and y

    undirected_path = bx.to_undirected()

    paths = list(
        nx.all_simple_paths(
            undirected_path,
            source=x,
            target=y,

        )
    )

    #checking  every path
    for road in paths:

        #checking if the apth between x and y is blocked by z

        print('checking path: ', "->".join(road))

        middle_nodes = road[1:-1]  # Exclude the start and end nodes

        #if the middle is contained in z then the path is blocekd
        if middle_nodes in z :
            
            print(f"Path {road} is blocked by {z}.")
            return True  # Path is blocked

        else:
            
            print(f"Path {road} is not blocked by {z}.")
            return False  # Path is not blocked

    return True  # If all paths are blocked, return True


    #defining the main function to test the d_separation function
def main():
    print("Testing d-separation:")
    print("Are 'Rain' and 'Sprinkler' d-separated given 'Wet Grass'?")
    res = d_separated(
        bx,
         "Rain",
        "Sprinkler",
        ["Wet Grass"]
    )
    print(f"Result: {res}")

    print("\nAre 'Wet Grass' and 'Sprinkler' d-separated given 'Rain'?")

    another_res = d_separated(
        bx,
        "Wet Grass",
        "Sprinkler",
        ["Rain"]
    )

    
    print(f"Result: {another_res}")

    


if __name__ == "__main__":
    main()