import igraph as ig
import numpy as np


def analyze_graph(graph: ig.Graph, NUM_ITERATIONS: int = int(1e8)) -> None:
    degree = graph.degree()
    betweenness = graph.betweenness()
    closeness = graph.closeness()
    vids = np.array(graph.random_walk(0, NUM_ITERATIONS))
    freqs = np.bincount(vids) / NUM_ITERATIONS
    R_degree = np.corrcoef(degree, freqs)[0, 1]
    R_betweenness = np.corrcoef(betweenness, freqs)[0, 1]
    R_closeness = np.corrcoef(closeness, freqs)[0, 1]
    print(f"{R_degree=}")
    print(f'{R_betweenness=}')
    print(f'{R_closeness=}')


if __name__ == '__main__':
    graphs = [ig.Graph.Erdos_Renyi(n=1000, m=5000),ig.Graph.Barabasi(n=1000, m=5),ig.Graph.Watts_Strogatz(dim=1, size=1000, nei=5, p=0.1),]
    for i, graph in enumerate(graphs):
        print(f'Analyzing graph {i+1}')
        analyze_graph(graph)
