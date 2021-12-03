import networkx as nx
import minimizeFeature as mf
import matplotlib.pyplot as plt

gr = nx.Graph()

edge_out = mf.edge_out
edge_out2 = mf.edge_out2
weights = mf.weights

for i in range(len(edge_out)):
    gr.add_edge(edge_out[i], edge_out2[i], weight=weights[i])


print("It is going to show a", nx.info(gr))


def graph(gr):
    pos = nx.spring_layout(gr, seed=7)

    nx.draw_networkx_nodes(gr, pos, node_size=700)

    nx.draw_networkx_edges(gr, pos, width=6)

    nx.draw_networkx_labels(gr, pos, font_size=20, font_family="sans-serif")

    labels = nx.get_edge_attributes(gr, 'weight')
    nx.draw_networkx_edge_labels(gr, pos, font_size=20, edge_labels=labels)

    return plt.show()


graph(gr)