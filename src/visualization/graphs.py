import sqlite3
import matplotlib.pyplot as plt
import networkx as nx

def get_children(eqdir):
    # Connect to the SQLite database
    conn = sqlite3.connect('JFFEQTracker.db')
    cursor = conn.cursor()
    
    # Query data from the database to fetch children nodes for the given EQDIR
    cursor.execute("SELECT EQDIR FROM Equivalency WHERE EQDIR_Ref = ?", (eqdir,))
    children = cursor.fetchall()
    
    # Close the database connection
    conn.close()
    
    return [child[0] for child in children]

def get_parents(eqdir):
    # Connect to the SQLite database
    conn = sqlite3.connect('JFFEQTracker.db')
    cursor = conn.cursor()
    
    # Query data from the database to fetch parent nodes for the given EQDIR
    cursor.execute("SELECT EQDIR_Ref FROM Equivalency WHERE EQDIR = ?", (eqdir,))
    parents = cursor.fetchall()
    
    # Close the database connection
    conn.close()
    
    return [parent[0] for parent in parents]

# Prompt the user to input an EQDIR
eqdir_input = input("Enter the EQDIR for which you want to generate the graph: ")

# Create a directed graph
G = nx.DiGraph()

# Get all parents and children of the input EQDIR
parents = get_parents(eqdir_input)
children = get_children(eqdir_input)

# Add nodes and edges for all parents and children of the input EQDIR
for parent in parents:
    G.add_node(parent, color='blue')  # Color parents blue
    G.add_edge(parent, eqdir_input)

for child in children:
    G.add_node(child, color='green')  # Color children green
    G.add_edge(eqdir_input, child)

# Add the input EQDIR as a node and color it red
G.add_node(eqdir_input, color='red')

# Plot the graph
plt.figure(figsize=(12, 8))

# Arrange parents horizontally above the input EQDIR and children below it
pos = nx.spring_layout(G)
pos[eqdir_input] = (pos[eqdir_input][0], pos[eqdir_input][1] + 0.2)  # Shift input EQDIR up
for parent in parents:
    pos[parent] = (pos[parent][0], pos[parent][1] + 0.5)  # Shift parents up
for child in children:
    pos[child] = (pos[child][0], pos[child][1] - 0.5)  # Shift children down

# Draw nodes with different colors
node_colors = [G.nodes[node]['color'] for node in G.nodes]
nx.draw(G, pos, with_labels=True, node_size=1000, node_color=node_colors, font_size=10, font_weight='bold')

plt.title('Parents and Children of EQDIR: {}'.format(eqdir_input))
plt.show()
