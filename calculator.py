import math
from . import utils

class CTECalculator:
    """Compute Combinatorial-Topological Entropy (CTE) for various structures."""
    
    def __init__(self, log_base=2):
        self.log_base = log_base

    # -------------------------------
    # Simplicial Complex CTE
    # -------------------------------
    def compute_simplicial(self, K, alpha=1.0, beta=1.0):
        adj = utils.count_adjacency(K)
        weights = [(len(sigma)**alpha) * ((adj[sigma]+1)**beta) for sigma in K]
        Z = sum(weights)
        weights_norm = [w/Z for w in weights]
        cte = -sum(w * math.log(w, self.log_base) for w in weights_norm)
        return cte

    # -------------------------------
    # Hypergraph CTE
    # -------------------------------
    def compute_hypergraph(self, H, alpha=1.0, beta=1.0):
        deg = utils.hypergraph_degree(H)
        weights = [(len(e)**alpha) * ((deg[i]+1)**beta) for i,e in enumerate(H)]
        Z = sum(weights)
        weights_norm = [w/Z for w in weights]
        cte = -sum(w * math.log(w, self.log_base) for w in weights_norm)
        return cte

    # -------------------------------
    # Parameter Sweep
    # -------------------------------
    def parameter_sweep(self, structure, alphas, betas, structure_type='simplicial'):
        """
        Sweep over alpha and beta parameters and return results as a list of dicts.
        structure_type: 'simplicial' or 'hypergraph'
        """
        results = []
        for a in alphas:
            for b in betas:
                if structure_type=='simplicial':
                    val = self.compute_simplicial(structure, a, b)
                elif structure_type=='hypergraph':
                    val = self.compute_hypergraph(structure, a, b)
                else:
                    raise ValueError("structure_type must be 'simplicial' or 'hypergraph'")
                results.append({"alpha": a, "beta": b, "CTE": val})
        return results
