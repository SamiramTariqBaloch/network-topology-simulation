import networkx as nx
import matplotlib.pyplot as plt

# --------------------------------
# Node Failure Function
# --------------------------------
def simulate_node_failure(G, node):
    if node in G:
        G.remove_node(node)
        print(f"Node Failure: Node {node} removed")

    nx.draw(G, with_labels=True, node_color="red")
    plt.show()



# --------------------------------
# Star Topology
# --------------------------------
def star_topology():
    print("\n--- STAR TOPOLOGY ---")
    G = nx.star_graph(5)

    nx.draw(G, with_labels=True, node_color="lightblue")
    plt.title("Star Topology")
    plt.show()

    # Node failure (central node)
    simulate_node_failure(G, 0)


# --------------------------------
# Bus Topology
# --------------------------------
def bus_topology():
    print("\n--- BUS TOPOLOGY ---")
    G = nx.path_graph(6)

    nx.draw(G, with_labels=True, node_color="lightgreen")
    plt.title("Bus Topology")
    plt.show()

    # Node failure
    simulate_node_failure(G, 3,)


# --------------------------------
# Ring Topology
# --------------------------------
def ring_topology():
    print("\n--- RING TOPOLOGY ---")
    G = nx.cycle_graph(6)

    nx.draw(G, with_labels=True, node_color="orange")
    plt.title("Ring Topology")
    plt.show()

    # Node failure
    simulate_node_failure(G, 2,)


# --------------------------------
# Mesh Topology
# --------------------------------
def mesh_topology():
    print("\n--- MESH TOPOLOGY ---")
    G = nx.complete_graph(5)

    nx.draw(G, with_labels=True, node_color="pink")
    plt.title("Mesh Topology")
    plt.show()

    # Node failure
    simulate_node_failure(G, 1,)


# --------------------------------
# Main Function
# --------------------------------
def main():
    print("NETWORK TOPOLOGY SIMULATION STARTED")

    star_topology()
    bus_topology()
    ring_topology()
    mesh_topology()

    print("\nSimulation Completed Successfully!")


# Run Program
main()