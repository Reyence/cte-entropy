# -------------------------------
# Utility functions
# -------------------------------

def count_adjacency(K):
    """Count higher-dimensional simplices containing each simplex."""
    adj = {sigma: 0 for sigma in K}
    for sigma in K:
        for tau in K:
            if set(sigma).issubset(tau) and sigma != tau:
                adj[sigma] += 1
    return adj

def hypergraph_degree(H):
    """Count overlapping hyperedges for each hyperedge in H."""
    deg = []
    for e in H:
        count = sum(1 for f in H if len(e & f) > 0 and e != f)
        deg.append(count)
    return deg
