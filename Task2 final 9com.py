# Import the necessary libraries
import networkx as nx  # for graph operations
import matplotlib.pyplot as plt  # for plotting graphs

# Define the graph edges along with their weights
edges = [
    ('A', 'B', 4), ('A', 'E', 1), ('A', 'C', 16), ('A', 'D', 3),
    ('B', 'C', 5), ('B', 'D', 8), ('E', 'D', 1), ('B', 'F', 9),
    ('C', 'F', 5), ('D', 'F', 12), ('F', 'Z', 1)
]

# Create a NetworkX graph object and add the edges to the graph
G = nx.Graph()
G.add_weighted_edges_from(edges)

# Define positions for nodes to make sure they are always in the same spots for consistency
pos = nx.spring_layout(G)

# Draw the graph using NetworkX and Matplotlib
nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='black')  # Draws the nodes and edges
edge_labels = nx.get_edge_attributes(G, 'weight')  # Get the weights for all the edges
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)  # Draws the edge labels (weights)
plt.title('Original Graph')  # Title for the plot
plt.show()  # Display the plot

# Define a Disjoint Set class to help in detecting cycles during the algorithm
class DisjointSet:
    def __init__(self, vertices):
        self.vertices = vertices  # Initialize vertices
        self.parent = {v: v for v in vertices}  # Parent for each vertex
        self.rank = {v: 0 for v in vertices}  # Rank for each vertex to help in union by rank

    def find(self, item):
        # Find the root parent of the item. If the item is its own parent, it is the root
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])  # Path compression
        return self.parent[item]

    def union(self, set1, set2):
        # Union by rank to merge two sets. Attach the tree with lower rank to the one with higher rank
        root1 = self.find(set1)
        root2 = self.find(set2)
        if root1 != root2:
            if self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            elif self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            else:
                self.parent[root2] = root1  # If ranks are same, make one as root and increment its rank by one
                self.rank[root1] += 1

# Define Kruskal's algorithm function to construct the MST
def kruskal(graph, edges):
    sorted_edges = sorted(edges, key=lambda item: item[2])  # Sort edges by weight
    ds = DisjointSet(graph.nodes())  # Create a disjoint set with all graph nodes
    mst = []  # List to store MST edges
    mst_weight = 0  # Variable to store the total weight of the MST

    # Loop through all edges, starting with the smallest
    for edge in sorted_edges:
        u, v, weight = edge
        # Check if adding the edge creates a cycle
        if ds.find(u) != ds.find(v):
            ds.union(u, v)  # If it doesn't create a cycle, add it to the MST
            mst.append(edge)
            mst_weight += weight  # Add weight to total MST weight
            
            # Draw the current MST
            mst_graph = nx.Graph()
            mst_graph.add_weighted_edges_from(mst)
            plt.figure()
            nx.draw(mst_graph, pos, with_labels=True, node_color='lightblue', edge_color='black')
            mst_edge_labels = nx.get_edge_attributes(mst_graph, 'weight')
            nx.draw_networkx_edge_labels(mst_graph, pos, edge_labels=mst_edge_labels)
            plt.title(f'MST Step-by-Step: Total Weight {mst_weight}')
            plt.show()
            
            # If we have added V-1 edges, we can stop; the MST is complete
            if len(mst) == len(graph.nodes()) - 1:
                break

    # Return the completed MST and its total weight
    return mst, mst_weight

# Call the Kruskal's algorithm function and pass the graph and edges
mst, total_weight = kruskal(G, edges)

# Print the edges that are in the MST and the total weight of the MST
print(f"The edges in the MST are: {mst}")
print(f"The total weight of the MST is: {total_weight}")
